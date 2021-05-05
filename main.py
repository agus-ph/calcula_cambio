import tkinter as tk
import tipo_cambio


class VentanaExchange:
    """
    Esta clase despliega una pequeña ventana donde se muestra
    el tipo de cambio oficial y blue. Y ademas se pueden hacer
    calculos de conversión de divisas
    """

    def __init__(
        self,
        mi_ventana,
    ):

        self.mi_ventana = mi_ventana
        self.mi_ventana.title("Tipo de Cambio USD")
        self.mi_ventana.geometry("300x300")

        self.var_ofi_compra = tk.StringVar()
        self.var_ofi_venta = tk.StringVar()
        self.var_blue_compra = tk.StringVar()
        self.var_blue_venta = tk.StringVar()

        # ------ llamadas a metodos de modulo TipoDeCambio---------
        self.oficial_compra = tipo_cambio.dolaroficial_compra()
        self.oficial_venta = tipo_cambio.dolaroficial_venta()
        self.blue_compra = tipo_cambio.dolarblue_compra()
        self.blue_venta = tipo_cambio.dolarblue_venta()

        # -------------------- Frame ---------------------------

        self.mi_frame = tk.Frame(self.mi_ventana)
        self.mi_frame.pack(fill="both", expand=1)

        # ----------------------------------------------------------
        # ----- SECCIÓN DONDE SE MUESTRAN LOS TIPOS DE CAMBIO ------
        # ----------------------------------------------------------

        # ------------------- Labels ----------------------

        label_oficial = tk.Label(self.mi_frame, text="Dolar Oficial")
        label_oficial.grid(row=0, column=0, padx=10, pady=10)

        label_ofi_compra = tk.Label(self.mi_frame, text="Compra:")
        label_ofi_compra.grid(row=0, column=1, padx=10, pady=10)

        self.valor_ofi_compra = tk.Label(
            self.mi_frame, textvariable=self.var_ofi_compra
        )
        self.valor_ofi_compra.grid(row=0, column=2, padx=10, pady=10)
        self.var_ofi_compra.set(self.oficial_compra)

        label_ofi_venta = tk.Label(self.mi_frame, text="Venta:")
        label_ofi_venta.grid(row=1, column=1, padx=10, pady=5)

        self.valor_ofi_venta = tk.Label(self.mi_frame, textvariable=self.var_ofi_venta)
        self.valor_ofi_venta.grid(row=1, column=2, padx=10, pady=5)
        self.var_ofi_venta.set(self.oficial_venta)

        label_blue = tk.Label(self.mi_frame, text="Dolar Blue")
        label_blue.grid(row=2, column=0, padx=10, pady=10)

        label_blue_compra = tk.Label(self.mi_frame, text="Compra:")
        label_blue_compra.grid(row=2, column=1, padx=10, pady=10)

        self.valor_blue_compra = tk.Label(
            self.mi_frame, textvariable=self.var_blue_compra
        )
        self.valor_blue_compra.grid(row=2, column=2, padx=10, pady=10)
        self.var_blue_compra.set(self.blue_compra)

        label_blue_venta = tk.Label(self.mi_frame, text="Venta:")
        label_blue_venta.grid(row=3, column=1, padx=10, pady=5)

        self.valor_blue_venta = tk.Label(
            self.mi_frame, textvariable=self.var_blue_venta
        )
        self.valor_blue_venta.grid(row=3, column=2, padx=10, pady=5)
        self.var_blue_venta.set(self.blue_venta)

        # ----------------------------------------------------------
        # ------------------ SECCIÓN CALCULADORA -------------------
        # ----------------------------------------------------------

        label_calcu = tk.Label(self.mi_frame, text="Calculadora")
        label_calcu.grid(row=4, column=0, padx=10, pady=10)

        # -------------- Menú desplegables --------------

        self.opciones = ["Peso", "Dólar", "Blue"]

        self.selector1 = tk.StringVar()
        self.selector1.set(self.opciones[0])

        self.selector2 = tk.StringVar()
        self.selector2.set(self.opciones[1])

        self.convertir_de = tk.OptionMenu(self.mi_frame, self.selector1, *self.opciones)
        self.convertir_de.grid(row=5, column=1, padx=10, pady=2)

        self.convertir_a = tk.OptionMenu(self.mi_frame, self.selector2, *self.opciones)
        self.convertir_a.grid(row=6, column=1, padx=10, pady=2)

        # ------------------- Entry ------------------

        self.campo1 = tk.Entry(self.mi_frame, width="10")
        self.campo1.grid(row=5, column=2, padx=10, pady=2)

        # --- Label donde se muestra el resultado ----

        self.convertido = tk.StringVar()
        self.campo2 = tk.Label(self.mi_frame, textvariable=self.convertido)
        self.campo2.grid(row=6, column=2, padx=10, pady=2)

        # ------------------ Boton --------------------

        self.boton_convertir = tk.Button(
            self.mi_frame,
            text="convertir",
            command=lambda: self.convertido.set(self.convertir()),
        )
        self.boton_convertir.grid(row=7, column=2, padx=10, pady=2)

    # ------------------------------------------------------------
    # ------------------------- METODO ---------------------------
    # ------------------------------------------------------------

    def convertir(
        self,
    ):
        """
        Este metodo calcula el valor relativo de las monedas
        dependiendo de las opciones de conversión elegidas
        por el usuario
        """
        convertir_de = self.selector1.get()
        convertir_a = self.selector2.get()
        if convertir_de == "Peso" and convertir_a == "Dólar":
            try:
                peso = float((self.campo1.get()).replace(",", "."))
            except:
                return "Ingrese \nun número"
            dolar = float((self.var_ofi_compra.get()).replace(",", "."))
            valor = round((peso / dolar), 2)
            return str(valor)
        elif convertir_de == "Peso" and convertir_a == "Blue":
            try:
                peso = float((self.campo1.get()).replace(",", "."))
            except:
                return "Ingrese \nun número"
            dolar = float((self.var_blue_compra.get()).replace(",", "."))
            valor = round((peso / dolar), 2)
            return str(valor)
        elif convertir_de == "Dólar" and convertir_a == "Peso":
            try:
                dolar = float((self.campo1.get()).replace(",", "."))
            except:
                return "Ingrese \nun número"
            peso = float((self.var_ofi_compra.get()).replace(",", "."))
            valor = round((dolar * peso), 2)
            return str(valor)
        elif convertir_de == "Blue" and convertir_a == "Peso":
            try:
                dolar = float((self.campo1.get()).replace(",", "."))
            except:
                return "Ingrese \nun número"
            peso = float((self.var_blue_compra.get()).replace(",", "."))
            valor = round((dolar * peso), 2)
            return str(valor)
        else:
            return "Operación \ninválida"


if __name__ == "__main__":

    root = tk.Tk()

    app_exchange = VentanaExchange(root)

    root.mainloop()
