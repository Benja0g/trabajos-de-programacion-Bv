CREATE TABLE IF NOT EXISTS docentes(
    id INT NOT NULL AUTO_INCREMENT,
    rut VARCHAR(12) NOT NULL,
    nombre VARCHAR(250) NOT NULL,
    email VARCHAR(250) NULL

    CONSTRAINT pk_docente PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS asignaturas(
    id INT NOT NULL AUTO_INCREMENT,
    codigo_asig VARCHAR(12) NOT NULL,
    nombre VARCHAR(250) NOT NULL,
    descripción VARCHAR(250) NULL

    CONSTRAINT pk_asignaturas PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS docentes_asignaturas(
    id INT NOT NULL AUTO_INCREMENT,
    rut_docente INT NOT NULL,
    id_asignatura INT NOT NULL,
   
    CONSTRAINT pk_docente_asignaturas PRIMARY KEY (id)
    CONSTRAINT fk_docentes FOREIGN KEY (id_docente) REFERENCE docentes(id)
);

CREATE TABLE IF NOT EXISTS docentes_asignaturas(
    id INT NOT NULL AUTO_INCREMENT,
    rut_docente INT NOT NULL,
    id_asignatura INT NOT NULL,
   
    CONSTRAINT pk_docente_asignaturas PRIMARY KEY (id)
    CONSTRAINT fk_docentes FOREIGN KEY (id_docente) REFERENCES docentes(id)
    CONSTRAINT fk_asignaturas FOREIGN KEY (id_asignatura) REFERENCES asignaturas (id)
);
