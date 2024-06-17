USE netflow;

CREATE TABLE tabela_netflow (
	    id INT NOT NULL AUTO_INCREMENT,
        `timestamp` BIGINT NOT NULL,
        src_ip VARCHAR(255) NOT NULL,
        dst_ip VARCHAR(255) NOT NULL,
        proto INT NOT NULL,
        packets INT NOT NULL,
        bytes BIGINT NOT NULL,
        duration INT NOT NULL
	    PRIMARY KEY (id)
);

-- Crie o usuário
CREATE USER 'pythonConnector'@'%' IDENTIFIED BY 'Python@connect123';

-- Conceda privilégios ao usuário no banco de dados currentTS
GRANT ALL PRIVILEGES ON netflow.* TO 'pythonConnector'@'%';

-- Atualize os privilégios
FLUSH PRIVILEGES;
