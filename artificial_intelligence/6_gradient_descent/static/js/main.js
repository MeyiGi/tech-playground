/* ═══════════════════════════════════════════════════════
   main.js  —  Gradient Descent 3D Visualizer
   Взаимодействует с Flask API, рисует 3D через Plotly
═══════════════════════════════════════════════════════ */

"use strict";

// ──────────── GLOBALS ────────────
let currentFn    = "sphere";
let surfaceData  = null;   // {xs, ys, zs, range, minima, label}
let pathData     = null;   // [{x,y,f,iter,grad}, ...]
let animIndex    = 0;
let animTimer    = null;
let running      = false;
let paused       = false;
let plotInited   = false;

// ──────────── DOM helpers ────────────
const $ = id => document.getElementById(id);

function setStatus(s) {
  const dot   = $("status-dot");
  const label = $("status-label");
  dot.className = "status-indicator " + s;
  const labels = { idle:"ожидание", running:"выполняется", paused:"пауза", done:"готово" };
  label.textContent = labels[s] || s;
}

function updateStats(item, total) {
  $("s-iter").textContent  = item.iter;
  $("s-fval").textContent  = item.f.toFixed(5);
  $("s-x").textContent     = item.x.toFixed(4);
  $("s-y").textContent     = item.y.toFixed(4);
  $("s-grad").textContent  = item.grad != null ? item.grad.toFixed(5) : "—";
  $("s-total").textContent = total;
  $("progress").style.width = (item.iter / parseInt($("iters").value) * 100) + "%";
}

function addLog(item, converged = false) {
  const box = $("log");
  box.querySelectorAll(".current").forEach(e => e.classList.remove("current"));
  const el = document.createElement("div");
  el.className = "log-entry " + (converged ? "converged" : "current");
  if (converged) {
    el.textContent = `[${String(item.iter).padStart(4,"0")}] ✓ Сходимость! f=${item.f.toFixed(6)}`;
  } else {
    el.textContent = `[${String(item.iter).padStart(4,"0")}] f=${item.f.toFixed(5)}  x=${item.x.toFixed(3)}  y=${item.y.toFixed(3)}`;
  }
  box.appendChild(el);
  box.scrollTop = box.scrollHeight;
  $("log-count").textContent = `(${box.children.length})`;
}

function clearLog() {
  $("log").innerHTML = "";
  $("log-count").textContent = "";
}

// ──────────── PLOTLY HELPERS ────────────

const COLORSCALE = [
  [0.00, "#081528"],
  [0.15, "#0d3b5e"],
  [0.30, "#0e7c7b"],
  [0.45, "#17c99e"],
  [0.60, "#ffe66d"],
  [0.80, "#ff6b6b"],
  [1.00, "#c0392b"]
];

const LAYOUT_BASE = {
  paper_bgcolor: "rgba(0,0,0,0)",
  plot_bgcolor:  "rgba(0,0,0,0)",
  margin: { l:0, r:0, t:0, b:0 },
  scene: {
    bgcolor: "#07090f",
    xaxis: { gridcolor:"#1a2235", zerolinecolor:"#1a2235", tickfont:{color:"#364060",size:9}, title:{text:"x",font:{color:"#4a5a80"}} },
    yaxis: { gridcolor:"#1a2235", zerolinecolor:"#1a2235", tickfont:{color:"#364060",size:9}, title:{text:"y",font:{color:"#4a5a80"}} },
    zaxis: { gridcolor:"#1a2235", zerolinecolor:"#1a2235", tickfont:{color:"#364060",size:9}, title:{text:"f(x,y)",font:{color:"#4a5a80"}} },
    camera: { eye:{x:1.5, y:1.5, z:1.2} },
    aspectratio: {x:1, y:1, z:0.6}
  },
  showlegend: false
};

function buildSurfaceTrace(sd) {
  return {
    type:  "surface",
    x:     sd.xs,
    y:     sd.ys,
    z:     sd.zs,
    colorscale: COLORSCALE,
    opacity: 0.88,
    showscale: false,
    contours: {
      z: { show:true, usecolormap:true, highlightcolor:"#3bffb8", project:{z:true}, width:1 }
    },
    hovertemplate: "x=%{x:.3f}<br>y=%{y:.3f}<br>f=%{z:.4f}<extra></extra>"
  };
}

function buildMinimaTrace(sd) {
  if (!sd.minima || sd.minima.length === 0) return null;
  const fn_info = sd;
  const xs = [], ys = [], zs = [];
  sd.minima.forEach(([mx, my]) => {
    xs.push(mx); ys.push(my);
    // Find closest z value
    const R = sd.range;
    const N = sd.xs.length - 1;
    const gi = Math.round((mx + R) / (2*R) * N);
    const gj = Math.round((my + R) / (2*R) * N);
    const z  = sd.zs[Math.max(0,Math.min(N,gj))][Math.max(0,Math.min(N,gi))];
    zs.push(z + 0.1);
  });
  return {
    type: "scatter3d", mode: "markers",
    x: xs, y: ys, z: zs,
    marker: { size:8, color:"#ffc73a", symbol:"diamond",
              line:{width:2, color:"#fff8dc"} },
    hovertemplate: "Минимум<br>x=%{x:.3f}<br>y=%{y:.3f}<extra></extra>"
  };
}

function buildPathTrace(pts) {
  if (!pts || pts.length === 0) return null;
  // Line
  const N = pts.length;
  const colors = pts.map((_, i) => i / Math.max(N-1,1));
  return {
    type:"scatter3d", mode:"lines",
    x: pts.map(p=>p.x),
    y: pts.map(p=>p.y),
    z: pts.map(p=>p.f),
    line: { width:5, color:colors, colorscale:[
      [0,"rgba(59,255,184,0.2)"],
      [0.5,"rgba(59,255,184,0.7)"],
      [1,"#3bffb8"]
    ]},
    hoverinfo: "skip"
  };
}

function buildPointTrace(pt, isStart=false) {
  return {
    type: "scatter3d", mode: "markers",
    x: [pt.x], y: [pt.y], z: [pt.f],
    marker: {
      size: isStart ? 6 : 10,
      color: isStart ? "#ffc73a" : "#3bffb8",
      symbol: "circle",
      opacity: isStart ? 0.8 : 1,
      line: { width: isStart ? 1 : 2, color: isStart ? "#fff" : "#ffffff" }
    },
    hovertemplate: (isStart?"Старт":"Текущая точка") + "<br>x=%{x:.4f}<br>y=%{y:.4f}<br>f=%{z:.5f}<extra></extra>"
  };
}

// ──────────── FETCH SURFACE ────────────
async function fetchSurface(fnKey) {
  setStatus("idle");
  const resp = await fetch("/api/surface", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({ fn: fnKey, steps: 55 })
  });
  surfaceData = await resp.json();
  renderSurface();
}

function renderSurface() {
  const sd = surfaceData;
  const traces = [buildSurfaceTrace(sd)];
  const mt = buildMinimaTrace(sd);
  if (mt) traces.push(mt);

  if (!plotInited) {
    Plotly.newPlot("plot3d", traces, LAYOUT_BASE, {
      responsive: true,
      displayModeBar: true,
      modeBarButtonsToRemove: ["toImage","resetScale2d"],
      displaylogo: false
    });
    plotInited = true;

    // Click on surface to set start point
    const plotEl = $("plot3d");
    plotEl.on("plotly_click", data => {
      if (!data.points || data.points.length === 0) return;
      const pt = data.points[0];
      if (pt.x == null || pt.y == null) return;
      $("start-x").value = pt.x.toFixed(3);
      $("start-y").value = pt.y.toFixed(3);
    });
  } else {
    Plotly.react("plot3d", traces, LAYOUT_BASE);
  }
}

// ──────────── RUN GRADIENT DESCENT ────────────
async function fetchRun() {
  const payload = {
    fn:       currentFn,
    algo:     $("algo").value,
    start_x:  parseFloat($("start-x").value),
    start_y:  parseFloat($("start-y").value),
    lr:       parseFloat($("lr").value),
    max_iter: parseInt($("iters").value),
    dx:       Math.pow(10, parseFloat($("dx-exp").value)),
    beta:     parseFloat($("beta").value),
  };

  const resp = await fetch("/api/run", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify(payload)
  });
  const result = await resp.json();
  return result.path;
}

// ──────────── ANIMATION LOOP ────────────
function animateStep() {
  if (!running || paused) return;
  if (animIndex >= pathData.length) {
    running = false;
    setStatus("done");
    addLog(pathData[pathData.length-1], true);
    return;
  }

  const currentPts = pathData.slice(0, animIndex + 1);
  const cur        = pathData[animIndex];
  const start      = pathData[0];

  // Rebuild only moving traces (indices 2,3,4 = path, start dot, current dot)
  const pathTrace  = buildPathTrace(currentPts) || { type:"scatter3d", x:[], y:[], z:[] };
  const startDot   = buildPointTrace(start, true);
  const curDot     = buildPointTrace(cur, false);

  const sd     = surfaceData;
  const traces = [buildSurfaceTrace(sd)];
  const mt     = buildMinimaTrace(sd);
  if (mt) traces.push(mt);
  traces.push(pathTrace, startDot, curDot);

  Plotly.react("plot3d", traces, LAYOUT_BASE);

  updateStats(cur, pathData.length - 1);
  if (animIndex % 5 === 0 || animIndex === pathData.length-1) addLog(cur);

  animIndex++;

  const delay = parseInt($("spd").value);
  animTimer = setTimeout(animateStep, delay);
}

// ──────────── PUBLIC CONTROLS ────────────
window.startRun = async function () {
  if (running && !paused) return;
  if (paused) {
    paused = false;
    setStatus("running");
    animateStep();
    return;
  }

  clearLog();
  $("plot-overlay").classList.add("hidden");
  setStatus("running");
  running = true;
  paused  = false;
  animIndex = 0;

  pathData = await fetchRun();

  if (!pathData || pathData.length === 0) {
    setStatus("idle");
    return;
  }

  addLog(pathData[0]);
  animateStep();
};

window.pauseRun = function () {
  if (!running) return;
  paused = !paused;
  setStatus(paused ? "paused" : "running");
  if (!paused) animateStep();
};

window.resetRun = function () {
  clearTimeout(animTimer);
  running = false; paused = false;
  pathData = null; animIndex = 0;
  clearLog();
  $("s-iter").textContent  = "—";
  $("s-fval").textContent  = "—";
  $("s-x").textContent     = "—";
  $("s-y").textContent     = "—";
  $("s-grad").textContent  = "—";
  $("s-total").textContent = "—";
  $("progress").style.width = "0%";
  $("plot-overlay").classList.remove("hidden");
  setStatus("idle");
  renderSurface();
};

window.selectFn = function (key, btn) {
  if (running) return;
  currentFn = key;
  document.querySelectorAll(".fn-btn").forEach(b => b.classList.remove("active"));
  btn.classList.add("active");
  plotInited = false;
  fetchSurface(key);
  resetRun();
};

window.updateDx = function () {
  const exp  = parseFloat($("dx-exp").value);
  const dx   = Math.pow(10, exp);
  const nice = dx < 1e-3 ? dx.toExponential(0) : dx.toFixed(4);
  $("dx-val").textContent     = nice;
  $("dx-display").textContent = "Δx = " + nice;
};

// Show/hide Momentum beta slider
$("algo").addEventListener("change", () => {
  $("beta-row").classList.toggle("hidden", $("algo").value !== "momentum");
});

// ──────────── INIT ────────────
fetchSurface("sphere");
