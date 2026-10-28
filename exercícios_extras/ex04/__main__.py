from pagamentos import *

def main():
    p1 = Pix(0)
    p2 = CartaoCredito(0)
    p3 = Boleto()
    #p4 = Pagamento(100)
    pagamentos = [p1, p2, p3]
    
    for pagamento in pagamentos:
        pagamento.exibir_recibo()
    

if __name__ == "__main__":
    main()
