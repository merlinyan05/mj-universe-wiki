# Documentation maintenance conventions

- Read README.md and CONTRIBUTING.md first; this is a documentation repository that can be cloned, maintained and read on its own.
- Character material is maintained in characters/, and characters are not duplicated per universe; source observations live in sources/. Universes and story patterns live in universes/; a shared pattern is maintained only once and other pages reference it by link.
- Keep the different versions of creators, branches, single episodes and comment co-creation; a name appearing does not mean a kinship is confirmed.
- State the evidence type and the actual scope checked; editorial proposals, inferences and original expansions must not be presented as verified in-video facts.
- When adding or renaming an entry, update the README index and references in that directory at the same time.
- Images and short GIFs serve the understanding of a specific entry or the Wiki display; note the related entry, purpose, source, version and rights status. Generic reaction images, wallpapers and sticker packs are introduced as text indexes and external links only, with the whole package kept outside, as detailed in CONTRIBUTING.md.
- Do not add private information, local paths, credentials, private conversations, dependencies of other projects or media production configuration.
- Run python3 scripts/check_docs.py; the check uses only the Python standard library and does not access the network.
- Contributions follow CC BY-SA 4.0; third-party content and this repository's original editing are attributed separately.
