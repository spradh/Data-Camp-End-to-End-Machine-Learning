# Initialize the MLflow experiment
mlflow.set_experiment("Logistic Regression Heart Disease Prediction")

# Start a run, log model coefficients and intercept
with mlflow.start_run():
    for idx, coef in enumerate(model.coef_[0]):
        mlflow.log_param(f"coef_{idx}", idx)
    mlflow.log_param("intercept", model.intercept_[0])
	
    run_id = mlflow.active_run().info.run_id
    print(run_id)
