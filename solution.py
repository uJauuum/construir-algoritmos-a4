
import pandas as pd
import numpy as np

def solution(arquivo):
    df = pd.read_csv(arquivo)

    area = df["area_util_m2"].to_list()
    quartos = df["quantidade_quartos"].to_list()
    preco = df["preco_venda"].to_list()

    X = np.array([
        [1, area[i], quartos[i]]
        for i in range(len(area))
    ])

    Y = np.array(preco)

    beta = np.linalg.lstsq(X, Y, rcond=None)[0]

    return beta.tolist()


if __name__ == "__main__":
    print(solution("imoveis_lar_perfeito.csv"))
