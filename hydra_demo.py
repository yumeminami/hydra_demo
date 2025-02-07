import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base="1.3", config_path="config", config_name="config")
def main(cfg: DictConfig):
    print("\n=== Full Configuration ===")
    print(OmegaConf.to_yaml(cfg))
    
    print("=== Database Config ===")
    print(f"DB Type: {cfg.db.type}")
    if cfg.db.type == "mysql":
        print(f"MySQL Connection: {cfg.db.user}@{cfg.db.host}:{cfg.db.port}")
    else:
        print(f"SQLite Path: {cfg.db.path}")
    
    print("\n=== Cache Config ===")
    print(f"Cache Type: {cfg.cache.type}")
    print(f"Cache Host: {cfg.cache.host}")
    print(f"Cache Port: {cfg.cache.port}")
    print(f"Cache DB: {cfg.cache.db}")
    
    print("\n=== Application Config ===")
    print(f"App Name: {cfg.app_name}")
    print(f"Debug Mode: {cfg.app.debug}")
    print(f"Active Features: {', '.join(cfg.app.features)}")

if __name__ == "__main__":
    main()