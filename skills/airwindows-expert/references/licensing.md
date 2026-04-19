# Airwindows Licensing

## License: MIT

All Airwindows plugins are released under the MIT License by Chris Johnson.

```
Copyright (c) Chris Johnson / Airwindows

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## What MIT means in practice

- **Use commercially** — fine, no royalties
- **Modify** — fine, no copyleft requirement
- **Redistribute source or binary** — fine, keep the copyright notice
- **Sublicense** — fine (e.g., wrap in a proprietary product)
- **Sell products incorporating this code** — fine

## Attribution requirement

You must include the copyright notice and license text in any distribution.
In practice for a plugin product, this typically means:

1. A `LICENSES/airwindows-mit.txt` file in your repo
2. A credits section in your plugin's About screen or documentation:
   *"DSP algorithms by Chris Johnson / Airwindows (MIT License)"*

## What's NOT covered by MIT

The Steinberg VST2 SDK (required to compile WinVST/MacVST targets) has its own
license and **cannot be redistributed**. The Airwindows repo instructions note
that VST2 SDK headers must be placed locally by the developer.

**Ports to JUCE** use JUCE's own license (GPL/commercial) independently of the
MIT DSP code. The Airwindows DSP algorithms themselves (the math in `Proc.cpp`)
are what's MIT-licensed — the VST wrapper boilerplate is not what you're porting.

## GPL compatibility

MIT is GPL-compatible. Airwindows DSP can be incorporated into GPL-licensed
projects without issue.

## Source reference

`airwindows/LICENSE` — the authoritative license file in the repo.
Each plugin `.cpp` file carries the header: `Airwindows uses the MIT license`.
