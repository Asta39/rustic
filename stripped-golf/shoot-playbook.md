# STRIPPED Golf shoot playbook

Every decision that got our product and model shoots to an approved standard. Follow it for every new shoot. The model's appearance is described in `model-reference.md`.

## 1. Output standard (every image)

- Square, 1:1 aspect ratio.
- 4K: 4096×4096. Website hero banners are the one exception: 16:9 at 5504×3072.
- Must not look AI-made. Write prompts as "real e-commerce photograph" and "natural skin texture". Never add "editorial", "film grain", "cinematic" or similar style words.
- Send every image separately, with a one-line caption.
- Commit and push the finals to `stripped-golf/pgm-shoot/<shoot-name>/`.

## 2. Which AI model to use

| Job | Model (Magnific) | Cost per 4K image |
|---|---|---|
| Anything with our model (his face, skin, build) | Seedream 4.5 (`seedream-4-5`) | 50 credits |
| Products only: logos, printed text, numbers | Nano Banana Pro (`imagen-nano-banana-2`) | 150 credits |
| Background removal for transparent PNGs | `images_remove_background` | 3 credits |

- Never use Nano Banana Pro for the model's face, or Seedream for small printed text.
- Ideogram precise-edit was tested on the putter and rejected: it redrew the head shape.

## 3. Shoots with our model

**The method that works:** an edit, not a fresh generation.

1. **Image 1** is always his real golf-outfit photo. Start the prompt with "Edit image 1: keep the exact same young man from image 1 and image 2…".
2. **Image 2** is always his face close-up.
3. After those, attach tight crops of the clothing or product, plus close-up crops of each logo.
4. Change only the clothes and the pose. Describe the pose in words.
5. Always include "very deep brown skin, do not lighten or warm skin" and "one person only, no jewellery".

**Never:**
- Generate him from scratch. This is what made the face drift and the images look fake.
- Build from an earlier generated image of him. Always go back to the original photos.
- Attach a photo of another person as a pose or outfit reference without cropping their face out. The model copies their hair, earrings and backdrop.
- Let other brands' logos through (swoosh, TaylorMade glove marks). Add "no brand logos anywhere", and reject and regenerate any image that still has one.

**Checking:** compare the face side by side with his face photo. Reject any change to skin tone, hair length or face width.

## 4. Product-only shoots

**Set:** seamless pure white background, with monochrome podiums and stages (black, charcoal, grey or white) under the product. Soft diffused light and a soft natural shadow. No model, no props.

**Two methods:**

- **Generate from references:** use for simple single items, such as one club head, a bag or a ball box. Attach the product photo plus a close-up crop of every logo or label. In the prompt, list every visible detail: colours, text, numbers, stitching and wear.
- **Edit the real photo:** use when the exact layout matters, such as a full set, everything in a bag, or an oddly shaped item like the M11 putter. Prompt: "Edit image 1 … keep every club exactly as it is … only replace the floor/room/hand with a white studio and podium." Generation from scratch dropped clubs, mirrored text and invented a putter.

**Rules:**
- **Keep the real condition.** These are used items, so keep the scuffs, chips and scratches. Say so in every prompt.
- **Remove shop barcode and price stickers.**
- **Draw nothing that isn't in the photos.** No golf balls, head covers, trolley handles, quilting or straps unless they're actually there.
- **Matching sets** (such as irons): generate the first club, approve it, then edit that approved image to change only the number. Every club in the set ends up in the same pose.
- **Ambiguous numbers:** spell out the shape. Example: "an upright 6, closed loop at the BOTTOM, cannot be mistaken for a nine".

## 5. Logos

- **Our wave-S logo:** never trust the AI to draw it. Generate the item with a plain badge, then paste the real `logo-system/stripped-logomark-white.png` (or the black version) on with code, and zoom-check it.
- **PGM and other printed text:** use Nano Banana Pro, attach a close-up crop of the logo, and quote the exact text in the prompt.
- **If one small line of text comes out garbled:** copy that line from a correct image onto the others with an ink-mask paste, then check for visible patch edges.

## 6. Quality check before sending (every image)

1. **Size:** confirm 4096×4096 (or 5504×3072 for heroes).
2. **Contact sheet:** view all candidates side by side and reject obvious failures.
3. **Zoom:** crop into every logo, number and line of text, and into the face. Compare each against the source photo.
4. **Inventions:** look for added parts, missing parts, duplicated text and mirrored text.
5. **Cutouts:** place transparent PNGs on a coloured background to check the edges, then centre them on a 4096 square canvas with a 4% margin.
6. **Keep going:** regenerate until the image is right. Never send a "close enough" image. Report what was rejected and the credits spent.

## 7. Reference IDs (Magnific)

| Reference | ID |
|---|---|
| Model base photo (golf outfit) | `xS0NnVJjfW` |
| Model face close-up | `gOpZTpKSXO` |
| Model, white tee full body | `jUT6YVELD0` |
| Wave-S logo | `jUnOyMOLD0` |
| White golf shoe, field style | `DosP6MBpcl` |
| White golf shoe, saddle | `JN8uq7DOq4` |
