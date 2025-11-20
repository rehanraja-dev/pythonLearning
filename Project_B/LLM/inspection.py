result = {
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Hello! How can I help you today?\n"
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "avgLogprobs": -0.007071088254451752
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 2,
    "candidatesTokenCount": 10,
    "totalTokenCount": 12,
    "promptTokensDetails": [
      {
        "modality": "TEXT",
        "tokenCount": 2
      }
    ],
    "candidatesTokensDetails": [
      {
        "modality": "TEXT",
        "tokenCount": 10
      }
    ]
  },
  "modelVersion": "gemini-2.0-flash",
  "responseId": "AyL6aP_iA_6n1e8PoffP-Qs"
}

print(result["candidates"][0]['content']['parts'][0]['text'])