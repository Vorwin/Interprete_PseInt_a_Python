PROCESO principal
    ESCRIBIR "Ingrese primer numero: ";
    DEFINIR num1 COMO REAL;
    LEER num1;
    ESCRIBIR "Ingrese segundo numero: ";
    DEFINIR num2 COMO REAL;
    LEER num2;
    ESCRIBIR "Ingrese tercer numero: ";
    DEFINIR num3 COMO REAL;
    LEER num3;
    SI ((num1 >= num2) Y (num1 >= num3))
        ESCRIBIR_LINEA num1;
        SI (num2 >= num3)
            ESCRIBIR_LINEA num2;
            ESCRIBIR_LINEA num3;
        SINO
            ESCRIBIR_LINEA num2;
            ESCRIBIR_LINEA num3;
        FINSI
    SINO
        SI ((num2 >= num1) Y (num2 >= num3))
            ESCRIBIR_LINEA num2;
            SI (num1 >= num3)
                ESCRIBIR_LINEA num1;
                ESCRIBIR_LINEA num3;
            SINO
                ESCRIBIR_LINEA num3;
                ESCRIBIR_LINEA num1;
        SINO
            SI ((num3 >= num1) Y (num3 >= num2))
                ESCRIBIR_LINEA num3;
                SI (num1 >= num2) 
                    ESCRIBIR_LINEA num1;
                    ESCRIBIR_LINEA num2;
                SINO
                    ESCRIBIR_LINEA num2;
                    ESCRIBIR_LINEA num1;
                FINSI
            FINSI
        FINSI
    FINSI
FINPROCESO