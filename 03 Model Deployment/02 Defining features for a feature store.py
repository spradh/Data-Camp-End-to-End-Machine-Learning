# Define entity and selected features
patient = Entity(name="patient", join_keys=["patient_id"])
cp = Field(name='cp', dtype=Float32)
thalach = Field(name='thalach', dtype=Int32)
ca = Field(name='ca', dtype=Int32)
thal = Field(name='thal', dtype=Int32)
