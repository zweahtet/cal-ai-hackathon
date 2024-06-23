import asyncio
from hume import HumeStreamClient
from hume.models.config import LanguageConfig


positive_emotions = ["Admiration", "Adoration", "Aesthetic Appreciation", "Amusement", "Awe", "Ecstasy", "Enthusiasm", "Excitement", "Gratitude", "Joy", "Interest", "Satisfaction", "Surprise (positive)", "Triumph"]


async def calculate_rating(post):
    client = HumeStreamClient("texVIA2o5o60QaXUxvXGnrv3DHKKOoiQr7d5EHE3SYBAKGVg")
    config = LanguageConfig()
    async with client.connect([config]) as socket:
            result = await socket.send_text(post)
            emotions = result["language"]["predictions"][0]["emotions"]
            rating = 0
            for expression in emotions:
                 key = expression["name"]
                 value = expression["score"]
                 if key in positive_emotions:
                      rating += value
            return rating

# asyncio.run(main())
print(asyncio.run(calculate_rating("🌟 Huge shoutout to @Google for constantly pushing the boundaries of technology! 🚀 Your innovative solutions in AI, search, and cloud services continue to transform our world, making information more accessible and life more convenient. Keep up the phenomenal work! 👏👏 #Innovation #TechGiant #Google")))
