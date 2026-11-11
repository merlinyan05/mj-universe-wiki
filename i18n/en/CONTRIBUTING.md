# Contributing Guide

You are welcome to add a name, a comment, a video timestamp, or correct a single character. New comment-section versions are also accepted; you do not have to become "recognized canon" first.

## You can participate without knowing Git

### Just provide a lead

Open **Issues → New issue** in the GitHub repository and choose "add a setting or source" or "corrections and version differences". Explain what you saw, where you saw it and who is involved; attach the original link and timestamp or comment context if possible.

If you cannot find the original link yet, you can still open an Issue and mark it "pending verification". Maintainers will treat it as a lead first and will not write it as verified in-video canon.

### Edit directly on the web

1. Open the relevant character or other entry `.md` file and click the edit button.
2. If you do not have write access, follow GitHub's prompt to fork and edit your own copy.
3. When done, write a short commit message and open a Pull Request.
4. In the PR, explain what you changed and what the source is; wait for maintainer review.

You do not need Python installed to edit documents. Automatic check results appear in the PR.

## Contribute with Git

First click **Fork** on GitHub and copy the clone URL of your fork. Replace `YOUR-USERNAME` in the addresses below with your account; if you renamed your fork, replace the repository name too.

```bash
git clone https://github.com/YOUR-USERNAME/mj-universe-wiki.git
cd mj-universe-wiki
git switch -c docs/add-character-detail
# Edit the relevant entry; when adding files, update the matching README index
python3 scripts/check_docs.py
git add characters/ sources/
git commit -m "docs: add a source for the character relationship"
git push -u origin docs/add-character-detail
```

Then on your fork page choose **Contribute → Open pull request** and confirm the target is the original repository's `main`.

Before contributing to a project for the first time, you can check your `noreply` address in GitHub under Settings → Emails and configure it for the local repository:

```bash
git config user.name "Your public name"
git config user.email "the noreply address copied from GitHub settings"
```

Please fill in real, working values before committing; do not use the example text as-is. This lets you contribute under a public name without exposing your private email.

GitHub reference: [Fork and PR workflow](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project), [commit email settings](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

## Where content goes

| Content | Location | When adding an entry |
| --- | --- | --- |
| Characters, parents, descendants, aliases, identity versions | `characters/character-name.md` | Copy the character template and update the character index |
| Partners, teachers and students, CP, names with unclear relationships | `relationships/` | State the direction of the relationship and the applicable version; update the index |
| World rules and universe differences | `universes/universe-name/README.md` | Link to character files; do not duplicate characters per universe |
| Classic memes, catchphrases and who uses them | `memes/` | State who says it to whom and in what situation |
| Universe-specific story patterns | `universes/universe-name/patterns/` | Explain trigger, escalation and consequence, attach video examples and update the index |
| Patterns reusable across universes | `universes/patterns/` | Mark the typical universe, reuse scope and differences; other universes only link |
| Observations of original videos, comments and danmaku | `sources/` | Copy the source template, assign an unused number and update the source index |

Source numbers increase from the existing ones; never renumber old entries. If two people pick the same new number, coordinate during PR review. Character names are maintained in one place only — the character file — and other pages link to it to avoid conflicting lists.

Character positioning, personality, habits, speech style and behavior in different universes are also welcome; attach concrete video examples to every summary instead of empty labels such as "smart" or "scheming". For cameos, state which character version is used; a cameo does not automatically inherit all of that version's relationships.

Templates: [universe](templates/宇宙模板.md) · [story pattern](templates/故事模式模板.md) · [character](templates/人物模板.md) · [source](templates/来源模板.md) · [single setting](templates/设定模板.md). If you are only adding one line to an existing entry, you do not need to copy a whole template.

## How to submit images and memes

### Character three-view sheets and appearance references

See the [appearance reference in the character files](characters/README.md#appearance-reference) for the current entry. In the "Appearance reference (external links)" section of the matching `characters/<name>.md`, add the source page, the author or publisher (when known), the film/game/fan/MJ creator version, the actual viewpoints, the verification date and scope, and whether permission has been confirmed. Prefer linking to official or author pages; when using a gallery entry, state that it is a gallery collection and do not treat the gallery as the original author. Write three-view sheets and general multi-angle displays separately.

When permission is unconfirmed, add only a plain text link; do not download images into the repository or embed remote originals with Markdown image syntax. Do not claim free reposting, commercial use or AI generation rights; a reference link is not proof of permission, nor is it evidence for MJ original-video appearance or character relationships. If you later submit self-drawn or AI-generated reference images, state the community-created version, the creation method and the boundary of third-party character rights, and review them under the image rules below.

### First explain what the image helps readers understand

This repository organizes MJ universe settings, and images serve the understanding of characters, relationships, worldlines and classic memes, or wiki presentation. When submitting, answer: **which setting does this image help the reader understand, or what clear presentation purpose does it serve?**

| Can be included with an entry | How to state the purpose |
| --- | --- |
| README cover, character identification image, relationship chart, worldline diagram | State the display position or related entry; note self-drawn and AI-generated diagrams separately from original-video evidence |
| Screenshots supporting a specific setting or classic meme | Link the related entry and record the original link, time point or comment context, creator version and actual verification scope |
| A short GIF that can only be understood through motion | Explain the motion that a static image cannot express, and keep only the segment needed for that entry |

Generic Marvel reaction images, wallpapers, chibi stickers and other general asset collections are introduced through text indexes and external links. Even with reposting permission, assets must fall within the scope above to be included with an entry. "It might be useful for a video later" is not enough to explain its relation to the settings.

### General asset collections use indexes and external links

You can add an asset index under `memes/` and link an external storage location or a separate asset repository; there is no need to commit the whole image pack first. The index should state the collection name, covered characters or themes, its relation to the reference, the access link, source and rights status, and what range of quantity and content was actually verified. Numbers provided only by the compiler should be marked "provided by the compiler, not yet verified item by item".

An external link does not mean this repository has reviewed every image, nor does it grant usage rights. The index still needs to explain its concrete help for looking up settings or related creation, avoiding piles of unrelated links.

### How to submit images for an entry

Meme images can go under `memes/images/<character>/`, for example `memes/images/灭霸/emo_reply.jpg`; covers and wiki display images can go under `assets/images/`. Display the image in the related entry with a relative path, for example:

```markdown
![Comment screenshot of sad copy turned into a nickname](images/灭霸/emo_reply.jpg)
```

The example path does not mean the file is already included; replace it with the image actually submitted. Every included image must be locatable from an entry or list, and record the related entry or display purpose, the original link or generation note, the creator (when known), the applicable version, the actual verification scope, and the reposting permission or authorization basis. When adding an asset index, add the index to `memes/README.md`.

Under the [third-party material notice](ATTRIBUTION.md), original images within scope or images with explicit reposting permission can be submitted with a PR; for web images whose permission is unconfirmed, include the source link and text index first. Source links, third-party copyright notices and reposting permission are stated separately, and third-party assets are not automatically relicensed under this repository's CC license. Before submitting, also check images for private information.

### File formats and checks

JPG/JPEG, PNG, GIF and WebP are supported. The file extension should match the actual format; when animation or transparency is needed, check the original asset — renaming a static JPEG or converting formats will not restore animation or an alpha channel.

Pure image directories do not need a README at every level; directories containing Markdown material still need a README index. Image links are checked for file existence. The check script reads the above image formats as binary and verifies file headers; **passing the script only means technical checks pass, while inclusion purpose, source, version and rights status still need human review.**

You can run the following checks locally without installing third-party Python packages:

```bash
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
```

## What a useful contribution looks like

For example, source record [R09](sources/R09.md) preserves the comment observation "Hulk's father is called Green Bean Soup":

- Relationship: Hulk → father → Green Bean Soup.
- Type: comment co-creation; not marked as in-video dialogue.
- Location: public comments on the original video, with reply context; if there is no stable comment link, link the video page.
- Version: keep other fathers' names; do not promote one comment into the only list.

This example cites existing material and does not mean a new contributor has re-checked the original page. When submitting, state whether you saw the title, a comment, an image, a clip or the full video.

## Source types and version differences

| Label | Meaning |
| --- | --- |
| In-video canon | Explicitly expressed in dialogue or on screen; provide a timestamp when possible |
| Creator's supplement | Description, pinned comment or creator reply |
| Comment co-creation | Comment chains, danmaku, guesses, comment images |
| Editorial inference | An explanation based on the material, with evidence and uncertainty stated |
| Original expansion | A new creative version; must not be written as a fact of an existing work |
| Pending lead | No source yet or only indirect clues; can be filed as an Issue first |

Keep unclear relationships unclear; list conflicting versions side by side and name the creator, branch or episode. A name appearing does not automatically prove a father, mother or other generational role; homophones in auto-generated subtitles must keep their uncertainty. For dead sources, keep the original link and the scope checked at the time; never rewrite a conclusion without a source.

## Review and maintenance

Keep one PR focused on one character, source or topic; typos can be fixed directly. Maintainers care about source boundaries, cross-links and version differences, and will not delete a version merely because it does not match personal preference.

Regular contributors push to their own fork. Maintainers with write access may push a topic branch directly and open a PR; granting write access and protecting `main` must be configured on GitHub after the repository goes live and do not take effect automatically from local documents. We recommend merging `main` through PRs and requiring `docs-check` to pass.

## License and privacy

By submitting original organization you agree to share the part you have the rights to license under [CC BY-SA 4.0](../../LICENSE) and retain your attribution rights; no copyright transfer is required. For third-party content you do not have the rights to license, keep only necessary short excerpts, summaries and sources, and attribute them clearly. See [attribution](ATTRIBUTION.md) for details.

Do not submit private chats, real family information, account credentials, absolute local paths or unrelated personal information. Public creator credits used for provenance may be kept; do not additionally collect commenters' contact details or personal profiles. Please also respect other contributors and discuss the material itself.

## Recording different versions of same-name relatives

When the parent table conflicts, prefer adding "creator/specific work + kinship direction + original characters + location" rather than picking one name to overwrite everything. For example, when the same literal name is an older brother in one work and a grandfather in another, keep both; songs, uploader images, in-video self-statements and comment chains are also recorded by type.

When new evidence confirms a previously pending relationship, add the new source in the character file and note the confirmation in the old candidate page; keep the scope of what the old source could see at the time (title/comments only). Synchronize the character index, relationship pages and universe entries as needed, avoiding a page that is confirmed while another still says everything is unverified.

Temporary positions in a single episode, authoritative titles inside a lie, and identities based on borrowed documents cannot be directly upgraded to permanent character attributes. For cross-universe cameos, note the difference between visitors and locals; see the [cameo note](universes/跨宇宙与客串.md) for specific examples.
