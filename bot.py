import logging
import os
from dotenv import load_dotenv
from interactions import Client, SlashContext, File, slash_command
import random
from PIL import Image, ImageDraw, ImageFilter
from io import BytesIO

load_dotenv()
logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("DISCORD_BOT_TOKEN not set in environment")
bot = Client(token=TOKEN)

# Dot positions for 150x150 image
DOTS = {
    1: [(75, 75)],
    2: [(37, 37), (112, 112)],
    3: [(37, 37), (75, 75), (112, 112)],
    4: [(37, 37), (37, 112), (112, 37), (112, 112)],
    5: [(37, 37), (37, 112), (75, 75), (112, 37), (112, 112)],
    6: [(37, 37), (37, 75), (37, 112), (112, 37), (112, 75), (112, 112)],
}


def draw_rounded_dice(draw, size, radius, fill):
    """Draw a rounded rectangle for the dice."""
    x0, y0 = 0, 0
    x1, y1 = size, size
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill)


@slash_command(
    name="tileraceroll",
    description="Roll a 6-sided dice for DarkAuroraaa's duo tile race event",
)
async def roll(ctx: SlashContext):
    result = random.randint(1, 6)

    size = 150
    img = Image.new("RGBA", (size, size), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Draw rounded dice
    draw_rounded_dice(draw, size=size, radius=20, fill="#fde8ff")

    dot_radius = 12
    shadow_offset = 3  # slightly larger offset for softer effect

    for x, y in DOTS[result]:
        # Create shadow layer
        shadow_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow_layer)

        # Draw shadow ellipse
        shadow_draw.ellipse(
            (
                x - dot_radius + shadow_offset,
                y - dot_radius + shadow_offset,
                x + dot_radius + shadow_offset,
                y + dot_radius + shadow_offset,
            ),
            fill="grey",
        )

        # Blur shadow
        shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(3))

        # Paste shadow onto main image
        img = Image.alpha_composite(img, shadow_layer)

        # Redefine draw after compositing
        draw = ImageDraw.Draw(img)

        # Draw main colored dot on top
        draw.ellipse(
            (x - dot_radius, y - dot_radius, x + dot_radius, y + dot_radius),
            fill="#96419e",
        )

    # Save to memory
    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    await ctx.send(
        f"<@{ctx.author_id}> rolled a **{result}**!",
        file=File(file=img_bytes, file_name="dice.png"),
    )


bot.start()
