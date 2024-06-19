USE netflow;

CREATE TABLE tabela_netflow (
    ts DATETIME,
    te DATETIME,
    td FLOAT,
    sa VARCHAR(15),
    da VARCHAR(15),
    sp INT,
    dp INT,
    pr VARCHAR(10),
    flg VARCHAR(10),
    fwd VARCHAR(10),
    stos INT,
    ipkt INT,
    ibyt INT,
    opkt INT,
    obyt INT,
    inbound INT,
    outbound INT,
    sas VARCHAR(20),
    das VARCHAR(20),
    smk VARCHAR(20),
    dmk VARCHAR(20),
    dtos VARCHAR(20),
    dir VARCHAR(10),
    nh VARCHAR(15),
    nhb VARCHAR(15),
    svln INT,
    dvln INT,
    ismc VARCHAR(20),
    odmc VARCHAR(20),
    idmc VARCHAR(20),
    osmc VARCHAR(20),
    mpls1 VARCHAR(10),
    mpls2 VARCHAR(10),
    mpls3 VARCHAR(10),
    mpls4 VARCHAR(10),
    mpls5 VARCHAR(10),
    mpls6 VARCHAR(10),
    mpls7 VARCHAR(10),
    mpls8 VARCHAR(10),
    mpls9 VARCHAR(10),
    mpls10 VARCHAR(10),
    cl FLOAT,
    sl FLOAT,
    al FLOAT,
    ra VARCHAR(15),
    eng VARCHAR(5),
    exid INT,
    tr DATETIME
);

-- CREATE TABLE tabela_summary (
--     flows INT,
--     bytes INT,
--     packets INT,
--     avg_bps INT,
--     avg_pps INT,
--     avg_bpp INT
-- );


CREATE USER 'pythonConnector'@'%' IDENTIFIED BY 'Python@connect123';

GRANT ALL PRIVILEGES ON netflow.* TO 'pythonConnector'@'%';

FLUSH PRIVILEGES;
