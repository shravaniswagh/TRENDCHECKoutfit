import yaml

def load_class_names(yaml_path):
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f)
        return {int(k): v for k, v in data["names"].items()}

# Load class names from your YAML file
class_names = load_class_names(
    "c:/Users/shrav/outfit-detect-recs/data-processing/clothing_data.yaml"
)

# Define rating rules for combinations
fashion_rules = {
    ("long sleeve top", "skirt"): {
        "style_score": 9,
        "season": "Autumn",
        "trendiness": "High",
        "comment": "Elegant and stylish for cooler weather."
    },
    ("short sleeve top", "shorts"): {
        "style_score": 7,
        "season": "Summer",
        "trendiness": "Medium",
        "comment": "Perfect for hot days."
    },
    ("long sleeve dress",): {
        "style_score": 8,
        "season": "Spring",
        "trendiness": "High",
        "comment": "Chic and versatile."
    }
    # Add more combinations as needed
}

def rate_outfit(class_ids):
    # Convert detected class IDs to names
    detected_names = [class_names.get(cid) for cid in class_ids if cid in class_names and cid != 0]
    key = tuple(sorted(detected_names))
    return fashion_rules.get(key, {
        "style_score": 5,
        "season": "Any",
        "trendiness": "Unknown",
        "comment": "No specific rating for this combo."
    })