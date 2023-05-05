import os
import cowsay

phrase = os.environ.get("PHRASE")
cowsay.cow(phrase)

