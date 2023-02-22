from Core.utils import Utils
from Core.models import Models


def main():
    models = Models()

    df = Utils.load_from_csv("Data/Felicidad_2019.csv")
    data, target = Utils.feature_target(dataset=df, drop_cols=['Country or region', 'Overall rank' ,'Score'], y='Score')
    best_model, score = models.get_best_model(X=data, y=target)
    print(best_model, score)
    Utils.model_export(clf=best_model, score=score, path="Models")


if __name__ == '__main__':
    main()