    ZIP: Unassigned
    Title: Future Dev and Legal Defense Fund Lockbox, and a ZCG Donation to the Network Sustainability Mechanism
    Owners: Zooko Wilcox <zooko@shieldedlabs.net>
    Status: Draft
    Category: Consensus / Process
    Created: 2026-10-29
    License: MIT
    Pull-Request: <https://github.com/zcash/zips/pull/???>


# Terminology

The key words "MUST", "MUST NOT", "SHALL", "SHOULD", and "MAY" in this
document are to be interpreted as described in BCP 14 [^BCP14] when, and
only when, they appear in all capitals.

The character § is used when referring to sections of the Zcash Protocol
Specification. [^protocol]

The terms "Mainnet" and "Testnet" are to be interpreted as described in
§ 3.12 ‘Mainnet and Testnet’. [^protocol-networks]

The terms "Zcash Community Grants" (or "ZCG"), "ZCG Committee", "Financial
Privacy Foundation" (or "FPF"), and "Deferred Dev Fund Lockbox" are to be
interpreted as defined in ZIP 1015. [^zip-1015]

The term "Coinholder-Controlled Fund" is to be interpreted as defined in
ZIP 1016. [^zip-1016]

The terms below are to be interpreted as follows:

Future Dev and Legal Defense Fund Lockbox

: The reserve of issued ZEC defined by this ZIP, into which the funding
  stream $\mathsf{FS\_FDLDF\_H3}$ pays. It is distinct from the Deferred
  Dev Fund Lockbox defined by ZIP 2001 [^zip-2001]: its balance is tracked
  separately, and no funds move between the two.

Activation height

: The height at which the network upgrade that activates this ZIP activates
  on a given network, written $H_A$.

Network Sustainability Mechanism (or "NSM")

: The mechanism by which ZEC is removed from circulation, to be returned
  through future block subsidies, as defined in ZIP 233 [^zip-0233].


# Abstract

This ZIP makes two changes to Zcash's protocol-defined ecosystem
funding, approved together as one proposal.

1. From its activation height until Zcash's third halving, the 8% of the
   block subsidy that currently goes to Zcash Community Grants
   ($\mathsf{FS\_FPF\_ZCG\_H3}$) is instead paid into a new lockbox, the
   **Future Dev and Legal Defense Fund Lockbox**. It works like the
   existing Deferred Dev Fund Lockbox, but it is a separate reserve. Funds
   accrue in it, and no transaction can spend them until a future ZIP
   defines how they are disbursed.

2. The ZCG Committee donates 50,000 ZEC to the Network Sustainability
   Mechanism as soon as possible, by sending it to a verifiably
   unspendable address, for a future network upgrade to recycle into the
   mechanism.


# Motivation

The rapid rise in the price of ZEC has enlarged the monetary value of ZCG's treasury to a much
greater amount than ever before. This ZIP reduces the risks and pressure that come with large
amounts of money, donates to the Network Sustainability Mechanism (providing increased long-term
issuance), and accrues funds in a lockbox for future use by the Zcash community.


# Privacy Implications

This ZIP changes where a part of the block subsidy goes, and asks for one
donation, sent in the clear to a published address. It changes no
transaction format, and no wallet behavior. Lockbox balances are, like the Deferred Dev Fund
Lockbox's, a consensus-level quantity visible to every full validator.


# Requirements

* From the activation height to the third halving, the 8% of the block
  subsidy previously allocated to ZCG accrues to the Future Dev and Legal
  Defense Fund Lockbox.
* The Future Dev and Legal Defense Fund Lockbox is a separate reserve from
  the Deferred Dev Fund Lockbox: neither one's balance can be paid into or
  out of the other.
* No funds can be disbursed from the Future Dev and Legal Defense Fund
  Lockbox until a future ZIP specifies how.
* The ZCG Committee donates 50,000 ZEC to the Network Sustainability
  Mechanism as soon as possible, without waiting for ZIP 233's activation.
* The donated ZEC is verifiably unspendable by anyone from the moment it
  is sent.


# Non-requirements

* This ZIP does not specify how, when, or to whom funds in the Future Dev
  and Legal Defense Fund Lockbox are disbursed; that is for a future ZIP.
* This ZIP does not change the 12% funding stream $\mathsf{FS\_CCF\_H3}$,
  the Deferred Dev Fund Lockbox, the Coinholder-Controlled Fund, or their
  governance under ZIPs 1016 [^zip-1016] and 271 [^zip-0271].
* This ZIP does not change the composition or governance of the ZCG
  Committee, nor its obligations regarding funds it received before the
  activation height.
* This ZIP does not change the Network Sustainability Mechanism, nor
  specify the consensus rules by which a future upgrade recycles the
  donation into it.


# Specification

## Provision 1: The Future Dev and Legal Defense Fund Lockbox

### Funding streams

A new revision of ZIP 214 [^zip-0214] SHALL make the following changes,
taking effect at the activation height $H_A$ on each network:

* The end height of $\mathsf{FS\_FPF\_ZCG\_H3}$ becomes $H_A$. (End
  heights are exclusive, as specified in ZIP 207 [^zip-0207], so the last
  block paying it is $H_A - 1$.)

* A new funding stream $\mathsf{FS\_FDLDF\_H3}$ is defined, with
  numerator 8 and denominator 100, start height $H_A$, and end height
  equal to the end height that $\mathsf{FS\_FPF\_ZCG\_H3}$ would have
  had without this ZIP: Zcash's third halving, as specified by Revisions 2
  and 3 of ZIP 214.

* The recipient of $\mathsf{FS\_FDLDF\_H3}$ is the Future Dev and Legal
  Defense Fund Lockbox.

Every other funding stream, including $\mathsf{FS\_CCF\_H3}$, is
unchanged.

### The lockbox

ZIP 2001 [^zip-2001] defines a funding stream recipient type that deposits
a stream's value into the Deferred Dev Fund Lockbox, a chain value pool
balance of issued but unspendable ZEC. This ZIP defines a second recipient
of the same kind, for the Future Dev and Legal Defense Fund Lockbox, with
its own chain value pool balance.

Changes to the Zcash Protocol Specification:

* In § 4.17 ‘Chain Value Pool Balances’, define a new chain value pool
  balance, $\mathsf{ChainValuePoolBalance^{FDLDF}}$, the balance of the
  Future Dev and Legal Defense Fund Lockbox. At the activation height it
  is zero.

* In § 7.10 ‘Payment of Funding Streams’, specify that the value of
  $\mathsf{FS\_FDLDF\_H3}$ at each height is added to
  $\mathsf{ChainValuePoolBalance^{FDLDF}}$, as ZIP 2001 specifies for a
  deferred-pool stream and the Deferred Dev Fund Lockbox's balance. The
  stream produces no output in the coinbase transaction.

* No consensus rule defined by this ZIP permits any transaction to spend
  from $\mathsf{ChainValuePoolBalance^{FDLDF}}$. Value in it remains part
  of the issued supply, as the Deferred Dev Fund Lockbox's does.

* The Deferred Dev Fund Lockbox's balance and the Future Dev and Legal
  Defense Fund Lockbox's balance are separate quantities: no consensus
  rule moves value between them.

Disbursement from the Future Dev and Legal Defense Fund Lockbox requires a
future ZIP, as disbursement from the Deferred Dev Fund Lockbox required
ZIP 271 [^zip-0271].

### Effect on ZCG

From the activation height, the provisions of ZIP 1016 [^zip-1016] that
establish the Zcash Community Grants funding stream cease to apply. ZCG
and FPF SHALL continue to administer the funds received from
$\mathsf{FS\_FPF\_ZCG}$ and $\mathsf{FS\_FPF\_ZCG\_H3}$ before the
activation height, under the obligations and constraints that ZIPs 1015
[^zip-1015] and 1016 place on them.

## Provision 2: ZCG's donation to the Network Sustainability Mechanism

### The NSM donation address

The NSM donation address is the Mainnet P2SH address

    t3QZUHYkaEQEuWosAc9HgMPKiQRdvuBPCQZ

Its script hash is `41c98a140039816273e50db317422c11c2bfcc88`, which is
HASH160 of the one-byte script `6a`, `OP_RETURN`. Spending a P2SH output
requires the redeem script whose HASH160 is the address's script hash, and
evaluating that script; `OP_RETURN` fails evaluation at once. So no one can
spend from the NSM donation address, unless they find a second script with
the same HASH160, which would break HASH160's second-preimage resistance.

Anyone can check this: decode the address with Base58Check, confirm its
version prefix (`1cbd`, Mainnet P2SH) and checksum, and compare its 20-byte
script hash with HASH160 of the byte `0x6a`.

### The donation

The ZCG Committee SHALL cause 50,000 ZEC, from the funds it administers,
to be sent to the NSM donation address, in one or more Mainnet
transactions. It SHALL do so as soon as possible, and no later than [TODO:
Zooko, for example 30] days after the date on which this provision is
accepted by the Zcash community. The donation does not wait for the
activation of ZIP 233 [^zip-0233].

The ZCG Committee SHALL publish the transaction identifier of each such
transaction to the Zcash community promptly after it is mined.

[TODO: Zooko. What happens if the ZEC the ZCG Committee administers is less
than 50,000 ZEC at the time of the donation, for example because funds are
committed to grants or held in another form.]

Since the funds ZCG administers are held by FPF, the ZCG Committee
fulfills this provision by directing FPF to create the transactions, as it
directs FPF to make grant payments under ZIP 1015.

### Recycling into the Network Sustainability Mechanism

ZEC sent to the NSM donation address is unspendable, but it is not removed
from circulation by any consensus rule: until a network upgrade acts on it,
it remains part of the transparent chain value pool and of the issued
supply. This ZIP declares all value sent to the NSM donation address a
donation to the Network Sustainability Mechanism.

A future network upgrade SHOULD treat that value as removed from
circulation through the Network Sustainability Mechanism, as ZIP 233
specifies for $\mathsf{zip233\_amount}$: subtracted from the issued supply
and from the transparent chain value pool, to be returned to circulation
through future block subsidies. That upgrade's ZIP will specify the
consensus rules, including the height at which the value at the address is
counted.

This covers every output sent to the NSM donation address, by anyone and at
any height, the ZCG Committee's donation among them.

### Circulating supply

ZEC sent to the NSM donation address SHOULD be excluded from counts of
circulating supply, such as those that block explorers, wallets, and data
providers publish. It can never circulate again: no one can spend it, and
it is set aside for the Network Sustainability Mechanism.


# Rationale

The Future Dev and Legal Defense Fund Lockbox reuses the lockbox design of
ZIP 2001, which the network already implements and full validators already
check. A separate chain value
pool balance keeps its funds apart from the Deferred Dev Fund Lockbox, so
that each reserve's purpose and future disbursement can be decided on its
own, and so that this ZIP leaves the Coinholder-Controlled Fund exactly as
it is.

Ending $\mathsf{FS\_FPF\_ZCG\_H3}$ at the activation height and starting
$\mathsf{FS\_FDLDF\_H3}$ at the same height, with the same share and the
same end height, keeps the total block subsidy allocated to funding
streams unchanged at every height.

The donation is made by sending ZEC to an address that no one can spend
from, so that it can happen now, before ZIP 233 [^zip-0233] lets a
transaction remove funds from circulation directly. Once sent, the ZEC is
out of everyone's reach, which anyone can verify from the address alone,
and this ZIP records its purpose. A later network upgrade then has what it
needs to recycle it into the Network Sustainability Mechanism.


# Deployment

Provision 1 is a consensus change. It is proposed for activation in the
first network upgrade after its acceptance [TODO: Zooko, for example NU7
or a later network upgrade]. On Testnet, it activates at that network
upgrade's Testnet activation height.

Provision 2 is a process change. It takes effect on acceptance, with its
deadline as specified above; it needs no network upgrade. The recycling of
the donated value into the Network Sustainability Mechanism is left to a
future network upgrade and its ZIP.


# Reference implementation

TBD.


# References

[^BCP14]: [Information on BCP 14 — "RFC 2119: Key words for use in RFCs to Indicate Requirement Levels" and "RFC 8174: Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words"](https://www.rfc-editor.org/info/bcp14)

[^protocol]: [Zcash Protocol Specification, Version 2025.6.0 or later](https://zips.z.cash/protocol/protocol.pdf)

[^protocol-networks]: [Zcash Protocol Specification, Version 2025.6.0. Section 3.12: Mainnet and Testnet](https://zips.z.cash/protocol/protocol.pdf#networks)

[^zip-0207]: [ZIP 207: Funding Streams](https://zips.z.cash/zip-0207)

[^zip-0214]: [ZIP 214: Consensus rules for a Zcash Development Fund](https://zips.z.cash/zip-0214)

[^zip-0233]: [ZIP 233: Network Sustainability Mechanism: Removing Funds From Circulation](https://zips.z.cash/zip-0233)

[^zip-0271]: [ZIP 271: Dev Fund Extension and One-Time Disbursement](https://zips.z.cash/zip-0271)

[^zip-1015]: [ZIP 1015: Block Subsidy Allocation for Non-Direct Development Funding](https://zips.z.cash/zip-1015)

[^zip-1016]: [ZIP 1016: Community and Coinholder Funding Model](https://zips.z.cash/zip-1016)

[^zip-2001]: [ZIP 2001: Lockbox Funding Streams](https://zips.z.cash/zip-2001)
