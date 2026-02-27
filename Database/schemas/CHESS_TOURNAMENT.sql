-- 1. CHESS PLAYER
CREATE TABLE ChessPlayer (
    player_id NUMBER PRIMARY KEY,
    full_name VARCHAR2(100) NOT NULL,
    gender VARCHAR2(10),
    age NUMBER
);

-- 2. TOURNAMENT
CREATE TABLE Tournament (
    tournament_id NUMBER PRIMARY KEY,
    name VARCHAR2(100) NOT NULL,
    start_date DATE,
    end_date DATE
);

-- 3. ORGANIZER
CREATE TABLE Organizer (
    organizer_id NUMBER PRIMARY KEY,
    name VARCHAR2(100) NOT NULL,
    address VARCHAR2(200)
);

-- 4. GAME
CREATE TABLE Game (
    game_id NUMBER PRIMARY KEY,
    tournament_id NUMBER NOT NULL,
    white_player_id NUMBER NOT NULL,
    black_player_id NUMBER NOT NULL,
    result VARCHAR2(20),
    
    CONSTRAINT fk_game_tournament
        FOREIGN KEY (tournament_id)
        REFERENCES Tournament(tournament_id),
        
    CONSTRAINT fk_game_white
        FOREIGN KEY (white_player_id)
        REFERENCES ChessPlayer(player_id),
        
    CONSTRAINT fk_game_black
        FOREIGN KEY (black_player_id)
        REFERENCES ChessPlayer(player_id)
);

-- 5. PLAYER_TOURNAMENT (M:N)
CREATE TABLE Player_Tournament (
    player_id NUMBER,
    tournament_id NUMBER,
    
    PRIMARY KEY (player_id, tournament_id),
    
    FOREIGN KEY (player_id)
        REFERENCES ChessPlayer(player_id),
        
    FOREIGN KEY (tournament_id)
        REFERENCES Tournament(tournament_id)
);

-- 6. TOURNAMENT_ORGANIZER (M:N)
CREATE TABLE Tournament_Organizer (
    tournament_id NUMBER,
    organizer_id NUMBER,
    
    PRIMARY KEY (tournament_id, organizer_id),
    
    FOREIGN KEY (tournament_id)
        REFERENCES Tournament(tournament_id),
        
    FOREIGN KEY (organizer_id)
        REFERENCES Organizer(organizer_id)
);

INSERT INTO ChessPlayer VALUES (1, 'Magnus Carlsen', 'Male', 33);
INSERT INTO ChessPlayer VALUES (2, 'Hikaru Nakamura', 'Male', 36);
INSERT INTO ChessPlayer VALUES (3, 'Hou Yifan', 'Female', 30);
INSERT INTO Tournament VALUES (1, 'World Championship', DATE '2025-03-01', DATE '2025-03-20');
INSERT INTO Tournament VALUES (2, 'Grand Prix', DATE '2025-04-10', DATE '2025-04-25');
INSERT INTO Organizer VALUES (1, 'FIDE', 'Lausanne, Switzerland');
INSERT INTO Organizer VALUES (2, 'Chess Federation', 'New York, USA');
INSERT INTO Player_Tournament VALUES (1, 1);
INSERT INTO Player_Tournament VALUES (2, 1);
INSERT INTO Player_Tournament VALUES (3, 2);
INSERT INTO Tournament_Organizer VALUES (1, 1);
INSERT INTO Tournament_Organizer VALUES (2, 1);
INSERT INTO Tournament_Organizer VALUES (2, 2);
INSERT INTO Game VALUES (1, 1, 1, 2, '1-0');
INSERT INTO Game VALUES (2, 1, 2, 1, '0-1');
INSERT INTO Game VALUES (3, 2, 3, 1, '1/2-1/2');

SELECT 
    t.name AS tournament,
    p.full_name
FROM Player_Tournament pt
JOIN ChessPlayer p ON pt.player_id = p.player_id
JOIN Tournament t ON pt.tournament_id = t.tournament_id
ORDER BY t.name;



