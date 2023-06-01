PROCESO principal
	DEFINIR radio COMO REAL;
	ESCRIBIR "Ingrese radio: ";
    LEER radio;
    DEFINIR cond COMO LOGICO;
    cond <- (radio > 10);
    DEFINIR perimetro COMO REAL;
    perimetro <- 0;
    DEFINIR area COMO REAL;
    area <- 0;
    SI (cond)
        perimetro <- ((2 * 3.1416) * radio);
        ESCRIBIR_LINEA "El perimetro es: " + perimetro;
    SINO
        area <- (3.1416 * ( sqrt radio ));
        ESCRIBIR_LINEA "El area es: " + area;
    FINSI
FINPROCESO
	