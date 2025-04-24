from memory.aimodel import AIModel

GEMINI_MODELS = [
    AIModel(
        name="Gemini 2.5 Flash",
        model_id="gemini-2.5-flash-preview-04-17",
        inputs=["text", "image", "audio", "video"],
        function_calling=True,
        search=True,
        code_execution=True
    ),
    AIModel(
        name="Gemini 2.0 Flash",
        model_id="gemini-2.0-flash", 
        inputs=["text", "image", "audio", "video"],
        outputs=["text", "image", "audio"],
        function_calling=True,
        search=True,
        code_execution=True
    ),
    AIModel(
        name="Gemini 2.0 Flash Lite",
        model_id="gemini-2.0-flash-lite",
        inputs=["text", "image", "audio", "video"], 
    ),
    AIModel(
        name="Gemini 2.0 Flash Think",
        model_id="gemini-2.0-flash-thinking-exp-01-21",
        inputs=["text", "image"],
        function_calling=True,
        search=True,
        code_execution=True
    ),
    AIModel(
        name="Gemini 2.0 Flash Img Gen",
        model_id="gemini-2.0-flash-exp-image-generation", 
        inputs=["text", "image", "audio", "video"],
        outputs=["text", "image"],
    ),
    AIModel(
        name="Gemini 2.5 Pro",
        model_id="gemini-2.5-pro-exp-03-25",
        inputs=["text", "image", "audio", "video"],
        function_calling=True,
        search=True,
        code_execution=True
    ),
    AIModel(
        name="Gemini 2.5 Pro Preview",
        model_id="gemini-2.5-pro-preview-03-25",
        inputs=["text", "image", "audio", "video"],
        structured_output=True,
        function_calling=True,
        search=True,
        code_execution=True
    ),
    AIModel(
        name="Gemini 1.5 Pro Learn",
        model_id="learnlm-1.5-pro-experimental",
        structured_output=True
    ),
    AIModel(
        name="Gemini 1.5 Flash-8B",
        model_id="gemini-1.5-flash-8b",
        inputs=["text", "image", "audio", "video"],
        structured_output=True,
        function_calling=True,
        search=True,
        code_execution=True
    ),
    AIModel(
        name="Gemini Imagegen 3",
        model_id="imagen-3.0-generate-002",
        inputs=["text"],
        outputs=["image"],
    ),
    AIModel(
        name="Gemma 3",
        model_id="gemma-3-27b-it",
        inputs=["text", "image"],
        structured_output=True,
        function_calling=False,
        search=False,
        code_execution=False
    ),
    AIModel(
        name="Gemini 2.0 Flash Live",
        model_id="gemini-2.0-flash-live-001",
        inputs=["text", "audio", "video"],
        outputs=["text", "audio"],
        structured_output=True,
        function_calling=True,
        search=True,
        code_execution=True,
        think=False,
        live=True
    )
]