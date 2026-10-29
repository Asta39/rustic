# STRIPPED showreel plan

Modelled on the WRN Essentials reel. 9:16, 1080×1920, 30 fps, 8.0 s, using the supplied audio track (8.06 s).

## How the reference is built

The tiny wordmark stays locked at the exact centre of the frame for the whole video. It never moves or scales. Every image behind it is framed so its subject sits under that point.

It's a flicker cut that slows down to a stop, timed to the audio:

| Time | What happens | Cut rhythm |
|---|---|---|
| 0.00–1.67 s | Flicker of about 25 images: logo embroidery close-up, fabric folds, model back and front, hang tag, gradient, colour swatches, white and grey flats | A new image every 2 frames (15 per second) |
| 1.67–5.00 s | The same image pool, slowing down. Cuts land on the music hits | Gaps grow 3, 4, 5, 6, 7, 8, 9 frames |
| 5.00–5.73 s | Black fabric with the tagline "DESIGNED TO / FEEL DIFFERENT" in spaced serif capitals above the logo | Hold |
| 5.73–6.77 s | Dark-to-light gradient while the large wordmark "WRNESSENTIALS" slides in from the right beside the small logo | Hold plus slide |
| 6.77–8.00 s | Brand colour sheet: PRIMARY, LIGHT, DARK and DEEP swatch cards with HEX, RGB and CMYK values; flips from dark to light | Hold, ends on the beat |

Look: monochrome only (black, charcoal, grey, off-white), soft studio light, lots of empty space. Image types alternate between macro texture, full-body model, product flat-lay, packaging and flat colour fields.

## Our version

**Centre mark:** the white STRIPPED wave-S logomark, about 70 px wide, locked at the centre. It switches to the black version on light frames.

**Image pool:** about 30 frames, all 9:16, all with the subject under the centre point. "Have" means the shot already exists and will be reframed for 9:16.

| Type | Source |
|---|---|
| Model shots (the five homepage poses, the black polo, the anorak) | Have, reframed to 9:16 on a grey studio background |
| Club macros (Rescue sole, SLDR badge, M11 putter, iron cavity) | Have, cropped close |
| PGM bag detail and wave-S embroidery close-up | New: a black knit with the wave-S embroidered on it, to match the opening "WRN" embroidery shot |
| Fabric folds: black, taupe knit, camel nylon | New, Nano Banana |
| STRIPPED hang tag on a cord, with care icons | New, Nano Banana, with our logo pasted on |
| Gradients and flat fields: black, #1A1A1A charcoal, grey, off-white | Built in code |
| Colour sheet: PRIMARY, LIGHT, DARK, DEEP with HEX, RGB and CMYK values | Built in code from our palette |

**Ending (same beats as the reference):**
- **5.00 s:** black fabric with "PLAY IT / STRIPPED BACK" as the tagline. The wording is a placeholder until you confirm it.
- **5.73 s:** gradient while "STRIPPED GOLF" slides in beside the logomark.
- **6.77 s:** the STRIPPED colour sheet, dark version flipping to light.

**Build:**
1. Generate the new stills.
2. Reframe everything to 1080×1920.
3. Assemble with ffmpeg on the exact cut frame list taken from the reference, overlay the centred logo, and add the audio.
4. Check the result frame by frame.

**Cost:** about 8 new stills × 150 credits, so roughly 1,200 credits. Everything else is reused or built in code.
