create database automatizacion;
USE automatizacion;

CREATE TABLE estudiantes (
    numero_control INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT NOT NULL,
    correo VARCHAR(100) NOT NULL,
    carrera VARCHAR(100) NOT NULL,
    semestre INT NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    ciudad VARCHAR(100) NOT NULL,
    genero VARCHAR(10) NOT NULL,
    promedio DECIMAL(3, 1) NOT NULL,
    contrasena VARCHAR(100) NOT NULL
);

INSERT INTO estudiantes (numero_control, nombre, edad, correo, carrera, semestre, telefono, ciudad, genero, promedio, contrasena)
VALUES
    (1220100603, 'ANZO AVALOS MARIA CITLALLI', 21, 'citlanzo@gmail.com', 'Ingeniería en Redes Inteligentes y Ciberseguridad', 9, '418-123-4567', 'Dolores Hidalgo', 'Femenino', 9.2, 'Linux123'),
    (1219100524, 'ARREDONDO GONZALEZ DANIEL ENRIQUE', 24, 'danielarredondo@gmail.com', 'Ingeniería en Redes Inteligentes y Ciberseguridad', 9, '418-987-6543', 'Dolores Hidalgo', 'Masculino', 9.2, 'Kali456'),
    (1220100317, 'DUARTE VELAZQUEZ DANIEL', 20, 'danyduart@gmail.com', 'Ingeniería en Redes Inteligentes y Ciberseguridad', 9, '418-567-8901', 'San Luis de la Paz', 'Masculino', 9.4, 'Black789'),
    (1220100629, 'GUTIERREZ MARTINEZ VALERIA IVONNE', 21, 'valeriaivonne@gmail.com', 'Ingeniería en Redes Inteligentes y Ciberseguridad', 9, '418-234-5678', 'San Luis de la Paz', 'Femenino', 9.0, 'Valeria123'),
    (1220100632, 'LUNA CANTERO ANGEL IVAN', 21, 'angelivan@gmail.com', 'Ingeniería en Redes Inteligentes y Ciberseguridad', 9, '418-678-9012', 'San Miguel de Allende', 'Masculino', 9.6, 'Angel456'),
    (1220100209, 'MARTINEZ RAMIREZ GUADALUPE MONSERRAT', 21, 'monse@gmail.com', 'Ingeniería en Redes Inteligentes y Ciberseguridad', 9, '418-345-6789', 'San Miguel de Allende', 'Femenino', 9.2, 'Monse789'),
    (1220100053, 'REYES MORALES SALVADOR', 21, 'salvador@gmail.com', 'Ingeniería en Redes Inteligentes y Ciberseguridad', 9, '418-789-0123', 'Dolores Hidalgo', 'Masculino', 9.8, 'Salvador123'),
    (1220100597, 'SALAZAR LEON MARIA GUADALUPE', 21, 'mleon@gmail.com', 'Ingeniería en Redes Inteligentes y Ciberseguridad', 9, '418-890-1234', 'San Luis de la Paz', 'Femenino', 9.6, 'Maria456'),
    (1220100596, 'TADEO MARTINEZ ALEJANDRO', 23, 'tadeo.alejandro.cbtis75@gmail.com', 'Ingeniería en Redes Inteligentes y Ciberseguridad', 9, '418-901-2345', 'Dolores Hidalgo', 'Masculino', 9.7, 'Alejandro789'),
    (1220100075, 'TORRES GARCIA JOSE ROGELIO', 22, 'joserogtoga@gmail.com', 'Ingeniería en Redes Inteligentes y Ciberseguridad', 9, '418-012-3456', 'San Luis de la Paz', 'Masculino', 9.0, 'Jose123'),
    (1220100595, 'TRANQUEÑO HERNANDEZ OSCAR ARMANDO', 20, 'armasacre@gmail.com', 'Ingeniería en Redes Inteligentes y Ciberseguridad', 9, '418-123-4567', 'Dolores Hidalgo', 'Masculino', 9.4, 'Oscar456');

 SELECT * FROM estudiantes;   
 drop table estudiantes;
 
 
