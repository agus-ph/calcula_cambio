import tkinter as tk
import tipo_cambio


class VentanaExchange:
    """
    Esta clase despliega una pequeña ventana donde se muestra
    el tipo de cambio oficial y
    """

    def __init__(
        self,
        mi_ventana,
    ):

        self.mi_ventana = mi_ventana
        self.mi_ventana.title("Tipo de Cambio USD")
        self.mi_ventana.geometry("300x200")

        self.var_ofi_compra = tk.StringVar()
        self.var_ofi_venta = tk.StringVar()
        self.var_blue_compra = tk.StringVar()
        self.var_blue_venta = tk.StringVar()

        # ------ llamadas a metodos de modulo TipoDeCambio---------
        self.oficial_compra = tipo_cambio.dolaroficial_compra()
        self.oficial_venta = tipo_cambio.dolaroficial_venta()
        self.blue_compra = tipo_cambio.dolarblue_compra()
        self.blue_venta = tipo_cambio.dolarblue_venta()
        # ---------------------------------------------------------

        self.mi_frame = tk.Frame(self.mi_ventana)
        self.mi_frame.pack(fill="both", expand=1)

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
        label_ofi_venta.grid(row=1, column=1, padx=10, pady=10)

        self.valor_ofi_venta = tk.Label(self.mi_frame, textvariable=self.var_ofi_venta)
        self.valor_ofi_venta.grid(row=1, column=2, padx=10, pady=10)
        self.var_ofi_venta.set(self.oficial_venta)

        label_blue = tk.Label(self.mi_frame, text="Dolar Blue:")
        label_blue.grid(row=2, column=0, padx=10, pady=10)

        label_blue_compra = tk.Label(self.mi_frame, text="Compra:")
        label_blue_compra.grid(row=2, column=1, padx=10, pady=10)

        self.valor_blue_compra = tk.Label(
            self.mi_frame, textvariable=self.var_blue_compra
        )
        self.valor_blue_compra.grid(row=2, column=2, padx=10, pady=10)
        self.var_blue_compra.set(self.blue_compra)

        label_blue_venta = tk.Label(self.mi_frame, text="Venta:")
        label_blue_venta.grid(row=3, column=1, padx=10, pady=10)

        self.valor_blue_venta = tk.Label(
            self.mi_frame, textvariable=self.var_blue_venta
        )
        self.valor_blue_venta.grid(row=3, column=2, padx=10, pady=10)
        self.var_blue_venta.set(self.blue_venta)


if __name__ == "__main__":

    root = tk.Tk()

    app_exchange = VentanaExchange(root)

    root.mainloop()
