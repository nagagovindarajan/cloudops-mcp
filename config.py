import time
import toml
import os

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        # If the config file doesn't exist, copy from the sample
        if not os.path.exists("config.toml"):
            with open("sample.config.toml", "r") as f_in, open("config.toml", "w+") as f_out:
                f_out.write(f_in.read())
                f_out.seek(0)
                self.config = toml.load(f_out)
        else:
            # check if all the keys are present in the config file
            with open("sample.config.toml", "r") as f:
                sample_config = toml.load(f)
            
            with open("config.toml", "r+") as f:
                config = toml.load(f)
            
                # Update the config with any missing keys and their keys of keys
                for key, value in sample_config.items():
                    config.setdefault(key, value)
                    if isinstance(value, dict):
                        for sub_key, sub_value in value.items():
                            config[key].setdefault(sub_key, sub_value)
            
                f.seek(0)
                toml.dump(config, f)
                f.truncate()
        
            self.config = config
            
    def get_config(self):
        return self.config

    def get_bing_api_endpoint(self):
        return self.config["API_ENDPOINTS"]["BING"]

    def get_google_search_api_endpoint(self):
        return self.config["API_ENDPOINTS"]["GOOGLE"]

    def get_ollama_api_endpoint(self):
        return self.config["API_ENDPOINTS"]["OLLAMA"]

    def get_lmstudio_api_endpoint(self):
        return self.config["API_ENDPOINTS"]["LM_STUDIO"]

    def get_openai_api_base_url(self):
        return self.config["API_ENDPOINTS"]["OPENAI"]

    def get_sqlite_db(self):
        return self.config["STORAGE"]["SQLITE_DB"]

    def get_screenshots_dir(self):
        return self.config["STORAGE"]["SCREENSHOTS_DIR"]

    def get_pdfs_dir(self):
        return self.config["STORAGE"]["PDFS_DIR"]

    def get_projects_dir(self):
        return self.config["STORAGE"]["PROJECTS_DIR"]

    def get_logs_dir(self):
        return self.config["STORAGE"]["LOGS_DIR"]

    def get_repos_dir(self):
        return self.config["STORAGE"]["REPOS_DIR"]

    def get_logging_rest_api(self):
        return self.config["LOGGING"]["LOG_REST_API"] == "true"

    def get_logging_prompts(self):
        return self.config["LOGGING"]["LOG_PROMPTS"] == "true"
    
    def get_timeout_inference(self):
        return self.config["TIMEOUT"]["INFERENCE"]

    def set_bing_api_endpoint(self, endpoint):
        self.config["API_ENDPOINTS"]["BING"] = endpoint
        self.save_config()

    def set_google_search_api_endpoint(self, endpoint):
        self.config["API_ENDPOINTS"]["GOOGLE_SEARCH"] = endpoint
        self.save_config()

    def set_ollama_api_endpoint(self, endpoint):
        self.config["API_ENDPOINTS"]["OLLAMA"] = endpoint
        self.save_config()

    def set_lmstudio_api_endpoint(self, endpoint):
        self.config["API_ENDPOINTS"]["LM_STUDIO"] = endpoint
        self.save_config()

    def set_openai_api_endpoint(self,endpoint):
        self.config["API_ENDPOINTS"]["OPENAI"] = endpoint
        self.save_config()

    def set_logging_rest_api(self, value):
        self.config["LOGGING"]["LOG_REST_API"] = "true" if value else "false"
        self.save_config()

    def set_logging_prompts(self, value):
        self.config["LOGGING"]["LOG_PROMPTS"] = "true" if value else "false"
        self.save_config()

    def set_timeout_inference(self, value):
        self.config["TIMEOUT"]["INFERENCE"] = value
        self.save_config()
    
    def get_aws_profile(self):
        return self.config["AWS"]["PROFILE"]

    def get_chroma_path(self):
        return self.config["CHROMA"]["PATH"]

    def get_chroma_embedding(self):
        return self.config["CHROMA"]["EMBEDDING_MODEL"]
    
    def get_drone_api_baseurl(self):
        return self.config["DRONE"]["API_BASE_URL"]
    
    def get_model_tiny(self):
        return self.config["MODEL"]["TINY"]

    def get_model_lite(self):
        return self.config["MODEL"]["LITE"]

    def get_model_base(self):
        return self.config["MODEL"]["BASE"]

    def get_model_think(self):
        return self.config["MODEL"]["THINK"]

    def get_model_vision(self):
        return self.config["MODEL"]["VISION"]

    def get_model_image_gen(self):
        return self.config["MODEL"]["IMAGE_GEN"]

    def get_model_audio_gen(self):
        return self.config["MODEL"]["AUDIO_GEN"]

    def get_model_video_gen(self):
        return self.config["MODEL"]["VIDEO_GEN"]

    def get_model_pro(self):
        return self.config["MODEL"]["PRO"]
    
    def get_model_live(self):
        return self.config["MODEL"]["LIVE"]

    def get_weather_api_key(self):
        return self.config["WEATHER"]["API_KEY"]

    def get_weather_api_base_url(self):
        return self.config["WEATHER"]["API_BASE_URL"]
    
    def get_alpha_vantage_api_key(self):
        return self.config["ALPHA_VANTAGE"]["API_KEY"]

    def get_alpha_vantage_api_base_url(self):
        return self.config["ALPHA_VANTAGE"]["API_BASE_URL"]
    
    def get_google_use_vertexai(self):
        return self.config["GOOGLE"]["USE_VERTEXAI"]
    
    def get_google_cloud_project(self):
        return self.config["GOOGLE"]["CLOUD_PROJECT"]
    
    def get_google_cloud_location(self):
        return self.config["GOOGLE"]["CLOUD_LOCATION"]

    def set_google_use_vertexai(self, value):
        self.config["GOOGLE"]["USE_VERTEXAI"] = value
        self.save_config()
    
    def set_google_cloud_project(self, value):
        self.config["GOOGLE"]["CLOUD_PROJECT"] = value
        self.save_config()
    
    def set_google_cloud_location(self, value):
        self.config["GOOGLE"]["CLOUD_LOCATION"] = value
        self.save_config()

    def save_config(self):
        with open("config.toml", "w") as f:
            toml.dump(self.config, f)

    def update_config(self, data):
        for key, value in data.items():
            if key in self.config:
                with open("config.toml", "r+") as f:
                    config = toml.load(f)
                    for sub_key, sub_value in value.items():
                        self.config[key][sub_key] = sub_value
                        config[key][sub_key] = sub_value
                    f.seek(0)
                    toml.dump(config, f)
