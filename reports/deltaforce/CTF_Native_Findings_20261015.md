# Delta Force CN Android 1.201.37117.67 — verified ARM64 evidence

Prepared 2026-10-15. All results from read-only analysis of official cached APK, and radare2 6.2.2 / custom Python-C++ on GitHub Actions; main branch unchanged.

## Verified binary identity

- APK: 1,519,215,938 bytes; SHA256 af03179c62ac57f05e4e6d425b2471bdf651b46c2f5a636f5a9e3fa94c78337d.
- lib/arm64-v8a/libUE4.so: 566,193,496 bytes; SHA256 387cd911a67eca1069bd5e4c874bce5dfb14823ca75f55f1ae7c43a09f2f1441.
- .text: virtual address 0x0815CDB0; bytes 326,518,896; 81,629,724 instruction slots.
- .rodata: virtual address 0x01718B40; bytes 39,648,042.
- Extracted .eh_frame_hdr: 1,649,092 function entries.

## Confirmed protection

The code in the region beginning at 0x0D1FBB60, when XORed bytewise with E2, yields a sustained valid ARM64 function (stack alloc, callee-save registers, TLS and control flow). The original six words precisely match 33E0211D 1BE2D11B 4BE5BD1A 4BEAB514 4BEBAD16 4BE8991F.

The entire .rodata also uses bytewise XOR E2. Raw ASCII printable ratio 0.00691; after XOR E2 it becomes 0.70725; 10,899,389 raw E2 bytes decode to NUL bytes. Decoded .rodata SHA256 a80812b3026efb2508e5464a86352986e84077ff1f9e729ad5159a8333229240.

DO NOT XOR every ELF section: .dynstr, .data and relocation metadata differ and are not similarly encoded.

## Restored coordinate-related metadata

Decoded ASCII substring occurrences: FEncVector 4; FEncHandler 2; bEncrypted 1; RelativeLocation 75; FVector 511; GetActorLocation 3. These are literal occurrences and NOT proof of functional uses in all cases.

Confirmed precise decoded C strings:
- FEncVector 0x02509232
- FEncHandler 0x0205405B
- bEncrypted 0x02462FC4
- GetActorEncLocation 0x020DB509
- GetComponentEncLocation 0x01C2B06E
- LastFrameEncLocation and HasSameInfoWithEncLocation also exist.

ADRP + ADD reconstructed code-string XREFs, independently verified at each site:
- FEncHandler code 0x09B337C8, FDE 0x09B3374C, string 0x0205405B.
- FEncVector code 0x0C3703A0, FDE 0x0C370324, string 0x02509232.
- FEncVector code 0x0E77912C, FDE 0x0E7790B8, string 0x02509232.
- FEncVector code 0x1B065C54, FDE 0x1B065C04, string 0x02509232.
- GetActorLocation code 0x160ADD94, FDE 0x160ADB80, string 0x01A3ED44.

Nearby disassembly indicates type registration / metadata processing, not proven coordinate decrypt functions.

## Coordinate candidate tests

After XOR E2 in .text: 562 LDR S [base,#0x168], 589 at 0x16c, 609 at 0x170, 130 LDRB at 0x176. 166 same-base XYZ triples in short windows but not proven coordinate getters. Function-level same-base correlation found 97 FDE entries with all 3 float reads; 0 among those with LDRB #0x176 and 0 with both that and LDRH #0x174.

The 0x0823C6A0..0x0823C964 function containing 0x0823C800 uses FCMP/FCSEL min/max on float triples, likely bounds reduction, not decrypt. 0x093532B4..0x0935363C copies many fields; 0x0A40CE34..0x0A40CFA4 compares many fields. The 0x085232F8..0x08523488 function reads a byte at +0x176 while searching a pointer structure, not proven bEncrypted flag.

## Conclusion and remaining uncertainty

Strong proof exists for E2 code and .rodata protection, and for native use of the custom FEncVector and FEncHandler names. GetActorEncLocation / GetComponentEncLocation names exist in this exact APK. Actual FEncVector layout, runtime encrypted coordinate dataflow, key/state source, decoder logic and exact current offset are NOT yet recovered. The earlier public framework uses illustrative and author-admitted placeholder offsets; never treat them as verified. The current APK alone may not contain ACE runtime-injected code.

## Reproducible runs / scripts

- XOR instruction validation: run 38651202378, tools/deltaforce_xor_e2_verify.py
- Function contexts: run 38652331037, tools/deltaforce_xor_candidate_context.py
- Coordinate/handler correlation: run 38652899639, tools/deltaforce_xor_struct_correlation.cpp
- .rodata decoding: run 38653368918, tools/deltaforce_xor_rodata_test.py
- String XREF scan: run 38653829220, tools/deltaforce_xor_string_xrefs.cpp
- FEnc native code registration: run 38654236114, tools/deltaforce_fenc_xref_context.py

Every run restored valid cached APK parts from original run 38596903200 (artifact IDs 11912605268 / 11912625263 / 11913085103 / 11912650314) and used cached radare2 artifact 11168472545. Temporary evidence Artifacts use 1-day retention; scripts and this report stay on research branch.

Local ChatGPT container execution endpoints returned ClientError repeatedly: no claim of local ZIP environment installation is made. The static work was executed on authenticated GitHub Actions runners. This report is not a runtime decryption validation.
