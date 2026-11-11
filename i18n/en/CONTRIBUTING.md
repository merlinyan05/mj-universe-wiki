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

Templates: [universe](../../templates/宇宙模板.md) · [story pattern](../../templates/故事模式模板.md) · [character](../../templates/人物模板.md) · [source](../../templates/来源模板.md) · [single setting](../../templates/设定模板.md). If you are only adding one line to an existing entry, you do not need to copy a whole template.

## What a useful contribution looks like

For example, source record [R09](../../sources/R09.md) preserves the comment observation "Hulk's father is called Green Bean Soup":

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
