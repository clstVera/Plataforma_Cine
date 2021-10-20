CREATE TABLE Pelicula (
    idPelicula      INTEGER PRIMARY KEY AUTOINCREMENT
                            NOT NULL,
    titulo          TEXT    NOT NULL,
    titulo_original TEXT    NOT NULL,
    genero          TEXT    NOT NULL,
    clasificacion   TEXT    NOT NULL,
    duracion        TEXT    NOT NULL,
    estreno         DATE    NOT NULL,
    director        TEXT    NOT NULL,
    actores         TEXT    NOT NULL,
    pais_origen     TEXT    NOT NULL,
    descripcion     TEXT    NOT NULL,
    imagen          TEXT    NOT NULL,
    trailer         TEXT    NOT NULL,
    calificacion    TEXT,
    votos           TEXT
);

CREATE TABLE Funcion (
    idFuncion    INTEGER PRIMARY KEY AUTOINCREMENT
                         NOT NULL,
    fecha        TEXT    NOT NULL,
    horario      TEXT    NOT NULL,
    formato      TEXT    NOT NULL,
    idioma       TEXT    NOT NULL,
    sala         TEXT    NOT NULL,
    calificacion TEXT,
    idPelicula   INTEGER NOT NULL
                         REFERENCES Pelicula (idPelicula) MATCH SIMPLE
);
