for config_variable in dictToSave:
    if config_variable["clef"] in locals():
        config_variable["valeur"] = locals()[config_variable["clef"]]

TADA