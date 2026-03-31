-- 1. LOCATION
CREATE TABLE LOCATION (
    location_id     NUMBER(3,0) PRIMARY KEY,
    regional_group  VARCHAR2(20)
);

-- 2. DEPARTMENT
CREATE TABLE DEPARTMENT (
    department_id   NUMBER(2,0) PRIMARY KEY,
    name            VARCHAR2(14),
    location_id     NUMBER(3,0),
    CONSTRAINT fk_department_location
        FOREIGN KEY (location_id)
        REFERENCES LOCATION(location_id)
);

-- 3. JOB
CREATE TABLE JOB (
    job_id          NUMBER(3,0) PRIMARY KEY,
    job_function    VARCHAR2(30)
);

-- 4. EMPLOYEE
CREATE TABLE EMPLOYEE (
    employee_id      NUMBER(4,0) PRIMARY KEY,
    last_name        VARCHAR2(15),
    first_name       VARCHAR2(15),
    middle_initial   VARCHAR2(1),
    manager_id       NUMBER(4,0),
    job_id           NUMBER(3,0),
    hire_date        DATE,
    salary           NUMBER(7,2),
    commission       NUMBER(7,2),
    department_id    NUMBER(2,0),
    CONSTRAINT fk_employee_job
        FOREIGN KEY (job_id)
        REFERENCES JOB(job_id),
    CONSTRAINT fk_employee_department
        FOREIGN KEY (department_id)
        REFERENCES DEPARTMENT(department_id)
);

-- Самоссылка для начальника
ALTER TABLE EMPLOYEE
ADD CONSTRAINT fk_employee_manager
    FOREIGN KEY (manager_id)
    REFERENCES EMPLOYEE(employee_id);

-- 5. CUSTOMER
CREATE TABLE CUSTOMER (
    customer_id       NUMBER(6,0) PRIMARY KEY,
    name              VARCHAR2(45),
    address           VARCHAR2(40),
    city              VARCHAR2(30),
    state             VARCHAR2(2),
    zip_code          VARCHAR2(9),
    area_code         NUMBER(3,0),
    phone_number      NUMBER(7,0),
    salesperson_id    NUMBER(4,0),
    credit_limit      NUMBER(9,2),
    comments          LONG,
    CONSTRAINT fk_customer_salesperson
        FOREIGN KEY (salesperson_id)
        REFERENCES EMPLOYEE(employee_id)
);

-- 6. PRODUCT
CREATE TABLE PRODUCT (
    product_id     NUMBER(6,0) PRIMARY KEY,
    description    VARCHAR2(30)
);

-- 7. PRICE
CREATE TABLE PRICE (
    product_id     NUMBER(6,0) NOT NULL,
    list_price     NUMBER(8,2),
    min_price      NUMBER(8,2),
    start_date     DATE NOT NULL,
    end_date       DATE,
    CONSTRAINT pk_price
        PRIMARY KEY (product_id, start_date),
    CONSTRAINT fk_price_product
        FOREIGN KEY (product_id)
        REFERENCES PRODUCT(product_id)
);

-- 8. SALES_ORDER
CREATE TABLE SALES_ORDER (
    order_id       NUMBER(4,0) PRIMARY KEY,
    order_date     DATE,
    customer_id    NUMBER(6,0),
    ship_date      DATE,
    total          NUMBER(8,2),
    CONSTRAINT fk_sales_order_customer
        FOREIGN KEY (customer_id)
        REFERENCES CUSTOMER(customer_id)
);

-- 9. ITEM
CREATE TABLE ITEM (
    order_id        NUMBER(4,0) NOT NULL,
    item_id         NUMBER(4,0) NOT NULL,
    product_id      NUMBER(6,0),
    actual_price    NUMBER(8,2),
    quantity        NUMBER(8,0),
    total           NUMBER(8,2),
    CONSTRAINT pk_item
        PRIMARY KEY (order_id, item_id),
    CONSTRAINT fk_item_order
        FOREIGN KEY (order_id)
        REFERENCES SALES_ORDER(order_id),
    CONSTRAINT fk_item_product
        FOREIGN KEY (product_id)
        REFERENCES PRODUCT(product_id)
);


-- =========================
-- LOCATION
-- =========================
INSERT INTO LOCATION (location_id, regional_group) VALUES (1, 'Bishkek');
INSERT INTO LOCATION (location_id, regional_group) VALUES (2, 'Osh');
INSERT INTO LOCATION (location_id, regional_group) VALUES (3, 'Almaty');
INSERT INTO LOCATION (location_id, regional_group) VALUES (4, 'Astana');

-- =========================
-- DEPARTMENT
-- =========================
INSERT INTO DEPARTMENT (department_id, name, location_id) VALUES (10, 'Sales', 1);
INSERT INTO DEPARTMENT (department_id, name, location_id) VALUES (20, 'IT', 1);
INSERT INTO DEPARTMENT (department_id, name, location_id) VALUES (30, 'HR', 2);
INSERT INTO DEPARTMENT (department_id, name, location_id) VALUES (40, 'Finance', 3);
INSERT INTO DEPARTMENT (department_id, name, location_id) VALUES (50, 'Logistics', 4);

-- =========================
-- JOB
-- =========================
INSERT INTO JOB (job_id, job_function) VALUES (1, 'Director');
INSERT INTO JOB (job_id, job_function) VALUES (2, 'Manager');
INSERT INTO JOB (job_id, job_function) VALUES (3, 'Salesperson');
INSERT INTO JOB (job_id, job_function) VALUES (4, 'Developer');
INSERT INTO JOB (job_id, job_function) VALUES (5, 'Accountant');
INSERT INTO JOB (job_id, job_function) VALUES (6, 'HR Specialist');
INSERT INTO JOB (job_id, job_function) VALUES (7, 'Logistics Specialist');

-- =========================
-- EMPLOYEE
-- =========================
INSERT INTO EMPLOYEE (employee_id, last_name, first_name, middle_initial, manager_id, job_id, hire_date, salary, commission, department_id)
VALUES (1001, 'Asanov', 'Timur', 'T', NULL, 1, DATE '2015-01-12', 9500, NULL, 10);

INSERT INTO EMPLOYEE (employee_id, last_name, first_name, middle_initial, manager_id, job_id, hire_date, salary, commission, department_id)
VALUES (1002, 'Ibragimov', 'Nurlan', 'N', 1001, 2, DATE '2017-03-10', 6500, NULL, 10);

INSERT INTO EMPLOYEE (employee_id, last_name, first_name, middle_initial, manager_id, job_id, hire_date, salary, commission, department_id)
VALUES (1003, 'Sadykov', 'Emil', 'E', 1001, 2, DATE '2018-06-21', 6200, NULL, 20);

INSERT INTO EMPLOYEE (employee_id, last_name, first_name, middle_initial, manager_id, job_id, hire_date, salary, commission, department_id)
VALUES (1004, 'Ismailov', 'Bakyt', 'B', 1002, 3, DATE '2019-02-15', 3800, 500, 10);

INSERT INTO EMPLOYEE (employee_id, last_name, first_name, middle_initial, manager_id, job_id, hire_date, salary, commission, department_id)
VALUES (1005, 'Omurov', 'Azamat', 'A', 1002, 3, DATE '2019-04-18', 3700, 450, 10);

INSERT INTO EMPLOYEE (employee_id, last_name, first_name, middle_initial, manager_id, job_id, hire_date, salary, commission, department_id)
VALUES (1006, 'Toktogulov', 'Marat', 'M', 1002, 3, DATE '2020-01-11', 3600, 400, 10);

INSERT INTO EMPLOYEE (employee_id, last_name, first_name, middle_initial, manager_id, job_id, hire_date, salary, commission, department_id)
VALUES (1007, 'Ryskulov', 'Daniyar', 'D', 1002, 3, DATE '2021-07-05', 3500, 350, 10);

INSERT INTO EMPLOYEE (employee_id, last_name, first_name, middle_initial, manager_id, job_id, hire_date, salary, commission, department_id)
VALUES (1008, 'Kim', 'Alex', 'A', 1003, 4, DATE '2019-08-01', 4200, NULL, 20);

INSERT INTO EMPLOYEE (employee_id, last_name, first_name, middle_initial, manager_id, job_id, hire_date, salary, commission, department_id)
VALUES (1009, 'Lee', 'Roman', 'R', 1003, 4, DATE '2020-09-14', 4100, NULL, 20);

INSERT INTO EMPLOYEE (employee_id, last_name, first_name, middle_initial, manager_id, job_id, hire_date, salary, commission, department_id)
VALUES (1010, 'Petrov', 'Ivan', 'I', 1003, 4, DATE '2021-11-09', 4000, NULL, 20);

INSERT INTO EMPLOYEE (employee_id, last_name, first_name, middle_initial, manager_id, job_id, hire_date, salary, commission, department_id)
VALUES (1011, 'Smirnova', 'Elena', 'E', 1003, 4, DATE '2022-02-03', 3900, NULL, 20);

INSERT INTO EMPLOYEE (employee_id, last_name, first_name, middle_initial, manager_id, job_id, hire_date, salary, commission, department_id)
VALUES (1012, 'Abdyldaev', 'Ulan', 'U', 1001, 2, DATE '2018-12-12', 5800, NULL, 40);

INSERT INTO EMPLOYEE (employee_id, last_name, first_name, middle_initial, manager_id, job_id, hire_date, salary, commission, department_id)
VALUES (1013, 'Saparova', 'Aida', 'A', 1012, 5, DATE '2019-05-20', 3400, NULL, 40);

INSERT INTO EMPLOYEE (employee_id, last_name, first_name, middle_initial, manager_id, job_id, hire_date, salary, commission, department_id)
VALUES (1014, 'Mamatova', 'Cholpon', 'C', 1012, 5, DATE '2021-04-17', 3300, NULL, 40);

INSERT INTO EMPLOYEE (employee_id, last_name, first_name, middle_initial, manager_id, job_id, hire_date, salary, commission, department_id)
VALUES (1015, 'Bekturov', 'Erkin', 'E', 1001, 2, DATE '2018-10-01', 3900, NULL, 30);

INSERT INTO EMPLOYEE (employee_id, last_name, first_name, middle_initial, manager_id, job_id, hire_date, salary, commission, department_id)
VALUES (1016, 'Kalieva', 'Amina', 'A', 1015, 6, DATE '2020-06-23', 3200, NULL, 30);

INSERT INTO EMPLOYEE (employee_id, last_name, first_name, middle_initial, manager_id, job_id, hire_date, salary, commission, department_id)
VALUES (1017, 'Sultanaliev', 'Mirlan', 'M', 1001, 2, DATE '2020-03-08', 4100, NULL, 50);

INSERT INTO EMPLOYEE (employee_id, last_name, first_name, middle_initial, manager_id, job_id, hire_date, salary, commission, department_id)
VALUES (1018, 'Usenova', 'Gulzat', 'G', 1017, 7, DATE '2022-06-16', 3000, NULL, 50);

-- =========================
-- PRODUCT
-- =========================
INSERT INTO PRODUCT (product_id, description) VALUES (300001, 'Laptop');
INSERT INTO PRODUCT (product_id, description) VALUES (300002, 'Monitor');
INSERT INTO PRODUCT (product_id, description) VALUES (300003, 'Keyboard');
INSERT INTO PRODUCT (product_id, description) VALUES (300004, 'Mouse');
INSERT INTO PRODUCT (product_id, description) VALUES (300005, 'Printer');
INSERT INTO PRODUCT (product_id, description) VALUES (300006, 'Router');
INSERT INTO PRODUCT (product_id, description) VALUES (300007, 'SSD');
INSERT INTO PRODUCT (product_id, description) VALUES (300008, 'Desk');
INSERT INTO PRODUCT (product_id, description) VALUES (300009, 'Chair');
INSERT INTO PRODUCT (product_id, description) VALUES (300010, 'Paper A4');
INSERT INTO PRODUCT (product_id, description) VALUES (300011, 'Notebook');
INSERT INTO PRODUCT (product_id, description) VALUES (300012, 'Pen Set');
INSERT INTO PRODUCT (product_id, description) VALUES (300013, 'Server');
INSERT INTO PRODUCT (product_id, description) VALUES (300014, 'UPS');
INSERT INTO PRODUCT (product_id, description) VALUES (300015, 'Webcam');
INSERT INTO PRODUCT (product_id, description) VALUES (300016, 'Headset');
INSERT INTO PRODUCT (product_id, description) VALUES (300017, 'Phone');
INSERT INTO PRODUCT (product_id, description) VALUES (300018, 'Tablet');
INSERT INTO PRODUCT (product_id, description) VALUES (300019, 'Projector');
INSERT INTO PRODUCT (product_id, description) VALUES (300020, 'Scanner');

-- =========================
-- PRICE
-- =========================
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300001, 950, 900, DATE '2025-01-01', NULL);
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300002, 220, 200, DATE '2025-01-01', NULL);
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300003, 25, 20, DATE '2025-01-01', NULL);
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300004, 18, 15, DATE '2025-01-01', NULL);
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300005, 180, 160, DATE '2025-01-01', NULL);
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300006, 75, 65, DATE '2025-01-01', NULL);
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300007, 120, 100, DATE '2025-01-01', NULL);
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300008, 160, 145, DATE '2025-01-01', NULL);
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300009, 110, 95, DATE '2025-01-01', NULL);
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300010, 6, 5, DATE '2025-01-01', NULL);
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300011, 3, 2, DATE '2025-01-01', NULL);
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300012, 8, 6, DATE '2025-01-01', NULL);
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300013, 2500, 2300, DATE '2025-01-01', NULL);
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300014, 140, 125, DATE '2025-01-01', NULL);
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300015, 45, 38, DATE '2025-01-01', NULL);
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300016, 35, 28, DATE '2025-01-01', NULL);
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300017, 320, 290, DATE '2025-01-01', NULL);
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300018, 280, 250, DATE '2025-01-01', NULL);
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300019, 650, 600, DATE '2025-01-01', NULL);
INSERT INTO PRICE (product_id, list_price, min_price, start_date, end_date) VALUES (300020, 150, 130, DATE '2025-01-01', NULL);

-- =========================
-- CUSTOMER
-- =========================
INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200001, 'Alpha Trade', 'Chui 101', 'Bishkek', 'BK', '720001', 312, 5551001, 1004, 15000, 'Regular customer');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200002, 'Beta Market', 'Manas 22', 'Bishkek', 'BK', '720002', 312, 5551002, 1005, 12000, 'Office goods');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200003, 'Gamma Office', 'Lenin 15', 'Osh', 'OS', '723500', 322, 5551003, 1006, 14000, 'Wholesale buyer');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200004, 'Delta Tech', 'Abay 11', 'Almaty', 'AL', '050010', 727, 5551004, 1007, 30000, 'IT equipment');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200005, 'Epsilon Retail', 'Turan 44', 'Astana', 'AS', '010000', 717, 5551005, 1004, 18000, 'Retail partner');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200006, 'Orion LLC', 'Chui 120', 'Bishkek', 'BK', '720003', 312, 5551006, 1005, 9000, 'Small business');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200007, 'Nomad Group', 'Kurmanjan 9', 'Osh', 'OS', '723501', 322, 5551007, 1006, 11000, 'Fast payment');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200008, 'Vector Plus', 'Satpaev 17', 'Almaty', 'AL', '050011', 727, 5551008, 1007, 20000, 'Corporate client');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200009, 'Silk Road Shop', 'Toktogul 88', 'Bishkek', 'BK', '720004', 312, 5551009, 1004, 10000, 'Buys monthly');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200010, 'East Service', 'Republic 31', 'Astana', 'AS', '010001', 717, 5551010, 1005, 13000, 'Delivery required');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200011, 'West Supplies', 'Navoi 23', 'Osh', 'OS', '723502', 322, 5551011, 1006, 12500, 'Stationery buyer');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200012, 'Crystal Trade', 'Jibek Jolu 77', 'Bishkek', 'BK', '720005', 312, 5551012, 1007, 16000, 'Pays on time');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200013, 'Golden Line', 'Dostyk 19', 'Almaty', 'AL', '050012', 727, 5551013, 1004, 17000, 'Electronics buyer');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200014, 'Prime Solutions', 'Kenesary 56', 'Astana', 'AS', '010002', 717, 5551014, 1005, 22000, 'Project purchases');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200015, 'Horizon Partners', 'Bokonbaeva 14', 'Bishkek', 'BK', '720006', 312, 5551015, 1006, 14500, 'Mixed products');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200016, 'Mega Commerce', 'Alymbekov 18', 'Osh', 'OS', '723503', 322, 5551016, 1007, 15500, 'Retail chain');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200017, 'Standard Office', 'Seifullin 29', 'Almaty', 'AL', '050013', 727, 5551017, 1004, 9500, 'Office furniture');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200018, 'City Distribution', 'Gorky 65', 'Bishkek', 'BK', '720007', 312, 5551018, 1005, 21000, 'Distribution center');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200019, 'Region Market', 'Turan 61', 'Astana', 'AS', '010003', 717, 5551019, 1006, 11500, 'Regional partner');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200020, 'Optima Sales', 'Masalieva 42', 'Osh', 'OS', '723504', 322, 5551020, 1007, 12500, 'Sales network');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200021, 'AkNiet Store', 'Ibraimov 12', 'Bishkek', 'BK', '720008', 312, 5551021, 1004, 10200, 'Local shop');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200022, 'Tech Vision', 'Al Farabi 100', 'Almaty', 'AL', '050014', 727, 5551022, 1005, 24000, 'Technology focus');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200023, 'Smart Choice', 'Saryarka 90', 'Astana', 'AS', '010004', 717, 5551023, 1006, 13500, 'General supplies');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200024, 'Office Point', 'Toktogul 52', 'Bishkek', 'BK', '720009', 312, 5551024, 1007, 11800, 'Office equipment');

INSERT INTO CUSTOMER (customer_id, name, address, city, state, zip_code, area_code, phone_number, salesperson_id, credit_limit, comments)
VALUES (200025, 'Profi Supply', 'Kurmanjan 45', 'Osh', 'OS', '723505', 322, 5551025, 1004, 17500, 'Large orders');

-- =========================
-- SALES_ORDER
-- =========================
INSERT INTO SALES_ORDER (order_id, order_date, customer_id, ship_date, total)
VALUES (4001, DATE '2026-01-10', 200001, DATE '2026-01-15', 1390);

INSERT INTO SALES_ORDER (order_id, order_date, customer_id, ship_date, total)
VALUES (4002, DATE '2026-01-12', 200002, DATE '2026-01-18', 810);

INSERT INTO SALES_ORDER (order_id, order_date, customer_id, ship_date, total)
VALUES (4003, DATE '2026-01-15', 200003, DATE '2026-01-19', 430);

INSERT INTO SALES_ORDER (order_id, order_date, customer_id, ship_date, total)
VALUES (4004, DATE '2026-01-18', 200004, DATE '2026-01-24', 2780);

INSERT INTO SALES_ORDER (order_id, order_date, customer_id, ship_date, total)
VALUES (4005, DATE '2026-01-20', 200005, DATE '2026-01-27', 1840);

INSERT INTO SALES_ORDER (order_id, order_date, customer_id, ship_date, total)
VALUES (4006, DATE '2026-02-01', 200006, DATE '2026-02-05', 360);

INSERT INTO SALES_ORDER (order_id, order_date, customer_id, ship_date, total)
VALUES (4007, DATE '2026-02-03', 200007, DATE '2026-02-08', 375);

INSERT INTO SALES_ORDER (order_id, order_date, customer_id, ship_date, total)
VALUES (4008, DATE '2026-02-05', 200008, DATE '2026-02-09', 720);

INSERT INTO SALES_ORDER (order_id, order_date, customer_id, ship_date, total)
VALUES (4009, DATE '2026-02-07', 200009, DATE '2026-02-11', 300);

INSERT INTO SALES_ORDER (order_id, order_date, customer_id, ship_date, total)
VALUES (4010, DATE '2026-02-09', 200010, DATE '2026-02-14', 120);

INSERT INTO SALES_ORDER (order_id, order_date, customer_id, ship_date, total)
VALUES (4011, DATE '2026-02-11', 200011, DATE '2026-02-16', 160);

INSERT INTO SALES_ORDER (order_id, order_date, customer_id, ship_date, total)
VALUES (4012, DATE '2026-02-15', 200012, DATE '2026-02-20', 225);

INSERT INTO SALES_ORDER (order_id, order_date, customer_id, ship_date, total)
VALUES (4013, DATE '2026-02-18', 200013, DATE '2026-02-23', 175);

INSERT INTO SALES_ORDER (order_id, order_date, customer_id, ship_date, total)
VALUES (4014, DATE '2026-02-21', 200014, DATE '2026-02-28', 1300);

INSERT INTO SALES_ORDER (order_id, order_date, customer_id, ship_date, total)
VALUES (4015, DATE '2026-02-25', 200015, DATE '2026-03-02', 450);

-- =========================
-- ITEM
-- =========================
INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4001, 1, 300001, 950, 1, 950);

INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4001, 2, 300002, 220, 2, 440);

INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4002, 1, 300008, 160, 3, 480);

INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4002, 2, 300009, 110, 3, 330);

INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4003, 1, 300003, 25, 10, 250);

INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4003, 2, 300004, 18, 10, 180);

INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4004, 1, 300013, 2500, 1, 2500);

INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4004, 2, 300014, 140, 2, 280);

INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4005, 1, 300017, 320, 4, 1280);

INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4005, 2, 300018, 280, 2, 560);

INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4006, 1, 300005, 180, 2, 360);

INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4007, 1, 300006, 75, 5, 375);

INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4008, 1, 300007, 120, 6, 720);

INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4009, 1, 300010, 6, 50, 300);

INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4010, 1, 300011, 3, 40, 120);

INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4011, 1, 300012, 8, 20, 160);

INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4012, 1, 300015, 45, 5, 225);

INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4013, 1, 300016, 35, 5, 175);

INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4014, 1, 300019, 650, 2, 1300);

INSERT INTO ITEM (order_id, item_id, product_id, actual_price, quantity, total)
VALUES (4015, 1, 300020, 150, 3, 450);

COMMIT;