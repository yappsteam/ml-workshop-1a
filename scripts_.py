import matplotlib.pyplot as plt
import seaborn as sea
import pandas as pd

def plot_data_results(pred1, pred2, y_test):
    '''
    Plots models
    '''
    modelos_1 = []
    modelos_2 = []
    for k in range(0, pred1.shape[0]):
        modelos_1.append('modelo1')
        modelos_2.append('modelo2')
    plt_data_test_1 = pd.DataFrame()
    plt_data_test_1['y_test'] = y_test
    plt_data_test_1['y_hat'] = pred1
    plt_data_test_1['modelo'] = modelos_1

    plt_data_test_2 = pd.DataFrame()
    plt_data_test_2['y_test'] = y_test
    plt_data_test_2['y_hat'] = pred2
    plt_data_test_2['modelo'] = modelos_2
    plot_test = pd.concat([plt_data_test_1, plt_data_test_2], axis = 0)
    return plot_test

def result_table(y, y_hat, y_hat_norm):
    results = pd.DataFrame()
    results['valores y originales'] = y
    results['y_hat'] = y_hat
    results['y_hat_norm'] = y_hat_norm
    return results


def coef_info(cols, coef_1, coef_2):
    '''
    Return a data frame with the coefs from the models
    '''
    c = pd.DataFrame()
    c['features'] = cols
    c['coef_modelo1'] = coef_1
    c['coef_modelo2'] = coef_2
    return c