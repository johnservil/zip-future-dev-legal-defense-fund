    ZIP: Unassigned
    Title: Future Dev and Legal Defense Fund Lockbox, and a ZCG Donation to the Network Sustainability Mechanism
    Owners: Sean Bowe (Tachyon Group) <ewillbefull@gmail.com>
            Zooko Wilcox (Shielded Labs) <zooko@shieldedlabs.net>
            Jason McGee (Shielded Labs) <jason@shieldedlabs.net>
    Status: Draft
    Category: Consensus / Consensus Process
    Created: 2026-10-29
    License: MIT
    Updates: 207, 209, 214, 237, 1015, 1016

# Terminology

The key words "MUST", "MUST NOT", "SHOULD", and "MAY" in this document are to
be interpreted as described in BCP 14 [^BCP14] when, and only when, they appear
in all capitals.

The terms "Mainnet", "Testnet", "block subsidy", "funding stream", "coinbase
transaction", and "chain value pool balance" have the meanings given in the Zcash
Protocol Specification. [^protocol] The character § refers to sections of that
specification.

"Zcash Community Grants" ("ZCG"), the "ZCG Committee", the "Financial
Privacy Foundation" ("FPF"), and the "Deferred Dev Fund Lockbox" have the
meanings given in ZIP 1015. [^zip-1015] "Coinholder-Controlled Fund" has the
meaning given in ZIP 1016. [^zip-1016]

"Network Sustainability Mechanism" ("NSM") refers to the mechanism specified in
ZIP 237. [^zip-0237] The "NSM fund" refers to the balance called the "NSM Value
Balance" in that ZIP. The operation of the NSM fund is specified separately from
the contributions defined here.

The "Future Dev and Legal Defense Fund Lockbox" is the chain value pool
introduced by this ZIP, with recipient identifier $\mathsf{FDLDF\_POOL}$ and no
beneficiary, custodian, or withdrawal mechanism. Its name records its intended
use, future Zcash development and legal defense, which a separate consensus
change will specify. It is distinct from the Deferred Dev Fund Lockbox
identified by $\mathsf{DEFERRED\_POOL}$ in ZIP 207. [^zip-0207] [^zip-2001]

The "designated NSM address" is, on each network, the address defined in
‘Voluntary NSM contributions’ below.

"ZCG funds" means assets held or administered by FPF for the ZCG program,
including its grant and Discretionary Budget balances, assets subsequently
received for that program, grant refunds, and proceeds attributable to those
assets. It excludes the Coinholder-Controlled Fund and assets administered by
FPF for other programs.

"Issued Supply" has the meaning given in § 4.17 ‘Chain Value Pool Balances’.
[^protocol-chainvaluepoolbalances]

All heights and indices introduced here are nonnegative integers. All subsidy
amounts, stream values, and contribution amounts are integer zatoshis in
$\{0, \ldots, \mathsf{MAX\_MONEY}\}$, where $\mathsf{MAX\_MONEY}$ is the monetary
bound defined in § 5.3 ‘Constants’. [^protocol-constants] One ZEC on Mainnet, or one
TAZ on Testnet, is 100,000,000 zatoshis.


# Abstract

This ZIP makes two changes:

1. The Zcash Community Grants funding stream ends at this ZIP's activation
   height. For the rest of its existing term, the same 8% share of the block
   subsidy accrues to a new **Future Dev and Legal Defense Fund Lockbox**,
   with no beneficiary, custodian, spending keys, or withdrawal mechanism.
   Any disposition requires a separate consensus change.

2. The ZCG Committee donates 50,000 ZEC of ZCG's existing treasury to the
   NSM fund, as soon as possible and within 30 days of this ZIP's
   acceptance. This ZIP supplies the mechanism: payments to a designated,
   verifiably unspendable address are removed from circulation and credited
   to the NSM Value Balance, including payments made before activation.

ZCG keeps its grant-making role, funded from the rest of its treasury. The 12% Coinholder-Controlled Fund stream, the Deferred Dev Fund
Lockbox, the ZEC supply cap, historical block validity, and existing
transaction formats are unchanged.


# Motivation

The rapid rise in the price of ZEC has enlarged the monetary value of ZCG's
treasury to a much greater amount than ever before. This ZIP reduces the risks
and pressure that come with large amounts of money, donates to the Network
Sustainability Mechanism (providing increased long-term issuance), and accrues
funds in a lockbox for future use by the Zcash community.

ZCG has accumulated sufficient resources to continue its grant-making role
without an automatic share of each block subsidy. This ZIP therefore ends that
funding stream, sets its remaining allocation aside in a lockbox pending a
community decision, and donates 50,000 ZEC of the existing treasury to the
network through the NSM.

## Existing resources

The public dashboard linked from ZCG's website reports 91,452.98 ZEC,
\$8,796,224 in USD, and \$2,417,165 in outstanding grant liabilities in the view
recorded for this proposal. [^zcg-dashboard] Valuing those holdings at explicit
prices gives:

| Assumed ZEC price | Reported holdings less reported grant liabilities |
| --: | --: |
| \$1,300 | \$125.3 million |
| \$1,000 | \$97.8 million |
| \$500 | \$52.1 million |

The valuations exclude future funding-stream receipts. [^financial-scenarios]

For comparison, the Financial Privacy Foundation (FPF) reported \$1,530,844 in
ZCG expenses for Q1 2026 and \$3,187,515 for Q2, an annualized \$9.44 million
over the first half of the year. [^fpf-q2-2026] At an illustrative
\$10 million in annual spending, the balances above represent about 12.5 years
of spending at \$1,300 per ZEC, or 5.2 years at \$500. [^financial-scenarios]

## Continued inflows

At a block subsidy of 1.5625 ZEC and a 75-second block target spacing, the 8%
allocation is 144 ZEC per target-spaced day, or 52,560 ZEC per 365-day year.
At \$1,300 per ZEC, that is approximately \$187,200 per day or \$68.3 million
per year: more than seven times the annualized first-half expense figure.
[^stream-scenarios] NU7 deploys ZIP 218's 25-second block spacing and subsidy
rescaling, leaving this daily allocation approximately unchanged, apart from
integer rounding. [^zip-0259]

A fixed share of issuance increases in dollar value when ZEC appreciates,
regardless of the recipient's existing reserves, spending, or approved
commitments.

## The donation

Ending the stream addresses future accumulation but not the accumulation that
has already occurred. Donating 50,000 ZEC to the NSM, about 55% of the ZEC
holdings reported above, gives, at the recorded dashboard inputs:

| Assumed ZEC price | Donation | Retained holdings less reported grant liabilities |
| --: | --: | --: |
| \$1,300 | \$65.0 million | \$60.3 million |
| \$1,000 | \$50.0 million | \$47.8 million |
| \$500 | \$25.0 million | \$27.1 million |

At an illustrative \$10 million in annual spending, the retained balances
represent about 6.0 years of spending at \$1,300 per ZEC, or 2.7 years at
\$500. [^donation-scenarios]

Value contributed to the NSM is removed from circulation and reissued
algorithmically through future block subsidies under ZIP 237, benefiting the
network as a whole rather than any discretionary recipient. [^zip-0237]

## Future allocations

ZIP 1016 provides distinct community and coinholder funding channels.
[^zip-1016] This ZIP preserves ZCG's authority over its retained resources and
the Coinholder-Controlled Fund's 12% stream. The companion proposal redirects
the remaining stream to the NSM, deciding its monetary disposition at
activation. [^draft-end-zcg-stream] A lockbox instead sets the allocation aside
for future development and legal defense, and leaves how it is spent to a later
community decision.

A separate proposal would wind down ZCG entirely and contribute its residual
treasury to the NSM. [^draft-wind-down-zcg] This ZIP takes a narrower position
on the treasury — donate 50,000 ZEC, and keep the program operating with the
rest — and pairs it with the stream redirection. The three
proposals are alternatives where they overlap, and the community should adopt
at most one disposition for each of the stream and the treasury.


# Privacy Implications

The redirected amount and the lockbox balance are derived from public consensus
state and subsidy rules, and introduce no recipient addresses, notes, spending
keys, or participant identifiers.

Contributions to the designated NSM address use transparent outputs, so their
amounts and timing are public. Transparent inputs expose their source UTXOs;
shielded inputs do not reveal their source addresses. The published
transaction identifiers identify the donation from the ZCG treasury, and
establish its amount and completion without publishing grantees' private
identities, payment addresses, or privileged legal advice. The proposal leaves transparent and
shielded transaction privacy properties unchanged.


# Requirements

* End automatic block subsidy payments to ZCG at activation without changing
  the rules governing its retained assets.
* Redirect the remaining 8% allocation to a new Future Dev and Legal Defense Fund Lockbox through the
  stream's existing expiry, using the existing per-stream integer rounding rule.
* Leave the lockbox without a beneficiary, custodian, or withdrawal
  mechanism; any disposition requires a separate consensus change,
  with no preferential claim for ZCG.
* Provide a deployed consensus mechanism under which treasury contributions are
  removed from circulation and credited to the NSM fund, without introducing
  transaction fields or address formats.
* Donate 50,000 ZEC of ZCG funds to the NSM fund as soon as possible, and
  within 30 days of this ZIP's acceptance, without waiting for its activation,
  with express authorization within the ZIP framework and the applicable legal
  instruments.
* Preserve historical block validity, monetary bounds, the existing formula for
  the miner's share of each block subsidy, and the Coinholder-Controlled Fund
  stream and deferred pool arrangements.


# Specification

Stream definitions, lockbox accounting, and the designated-address rules below
are consensus requirements. The amendments to ZIPs 1015 and 1016 and the
donation obligation are consensus-process requirements.

## Activation and dependencies

Let $A$ be this ZIP's activation height and $N$ be the NU7 activation height on
the relevant network. Let $S$ and $E$ be the inclusive start and exclusive end
heights of `FS_FPF_ZCG_H3` under ZIP 214, after applying any other consensus
changes effective at $A$, but before applying this ZIP. [^zip-0214]

NU7 deploys Revision 3 of ZIP 214, which preserves the start heights from
Revision 2 and moves the end heights to the third halving under ZIP 218's
25-second block spacing. [^zip-0218] If $N$ precedes the pre-NU7 third-halving
height $E_{75}$, the revised end height is $E = N + 3(E_{75} - N)$.
The pre-NU7 end heights are 4406400 on Mainnet and 4476000 on Testnet.
With the NU7 activation parameters currently specified in ZIP 259: [^zip-0259]

| Network | $N$ | $S$ | $E$ |
| :------ | --: | --: | --: |
| Mainnet | 3543405 | 3146400 | $13219200 - 2N$ |
| Testnet | 4465026 | 3536500 | 4497948 |

Revision 3 does not reactivate a stream that expired before NU7. This ZIP changes
the destination of the remaining allocation; its expiry is unchanged.

The activation parameters MUST satisfy $N \leq A$ on each network, and
$S < A < E$ on Mainnet. The NU7 changes to funding streams, fee accounting,
and the NSM Value Balance MUST be effective at $A$.

On a network where $A \geq E$, the stream changes below are vacuous: the end
height of `FS_FPF_ZCG_H3` is unchanged under the $\min(A, E)$ rule, and
`FS_FDLDF_H3` is not defined. Under ZIP 259's parameters this is the
expected case on Testnet, where the stream expires $E - N = 32922$ blocks —
about nine and a half days — after NU7 activation. The designated-address
rules apply from $A$ on each network regardless.

All consensus changes in this ZIP take effect together at $A$. Blocks before
$A$ MUST continue to be validated under their existing rules.

## Funding streams and recipients

A new revision of ZIP 214 [^zip-0214] makes the following changes at $A$ on
each network:

* The exclusive end height of `FS_FPF_ZCG_H3` becomes $\min(A, E)$; this ZIP
  never extends the stream. Its start height, fraction, and recipient at
  every height before $A$ are unchanged.
* Its recipient list becomes the prefix of the existing list, with length
  $\mathsf{fs.NumRecipients}$ recalculated for the new end height as
  specified in § 7.10 ‘Payment of Funding Streams, Deferred Lockbox, and
  Lockbox Disbursement’, using the address-period calculation from Revision 2
  of ZIP 207. [^protocol-fundingstreams] [^zip-0207] That calculation
  preserves pre-NU7 indices, triples the remaining block count in the address
  period at NU7 activation, and gives each subsequent period 105000 blocks.
  The existing Mainnet list already includes the address change made by
  ZIP 2008; apply it before truncating. [^zip-2008]
* The following funding stream is added on each network where $A < E$. On a
  network where $A \geq E$, `FS_FDLDF_H3` is not defined, and
  $\mathsf{totalFDLDFOutput}(h)$ and $F(h)$ are zero at every height.

| Stream | Numerator | Denominator | Start height | End height |
| :----- | --------: | ----------: | -----------: | ---------: |
| `FS_FDLDF_H3` | 8 | 100 | $A$ | $E$ |

A new revision of ZIP 207 [^zip-0207] extends the allowed recipient
identifiers, and the corresponding identifiers in § 7.10, with the symbolic
identifier $\mathsf{FDLDF\_POOL}$, distinct from
$\mathsf{DEFERRED\_POOL}$ and from all address encodings:

* Every entry in `FS_FDLDF_H3`'s recipient list is
  $\mathsf{FDLDF\_POOL}$; its list length and recipient-index
  calculation use the same NU7 address-period rules. The identifier has no
  payment address or spending key.
* In ZIP 207's post-NU6 coinbase-output rule and the corresponding rule in
  § 7.10, the exception for $\mathsf{DEFERRED\_POOL}$ also excludes
  $\mathsf{FDLDF\_POOL}$: crediting the lockbox is an accounting
  operation and produces no coinbase output.
* Former ZCG recipient addresses keep their ordinary address semantics, with
  no mandatory ZCG payment at or after $A$.

`FS_CCF_H3` retains its existing numerator, denominator, start height, end height,
and recipient identifiers. Keep $\mathsf{DeferredFundingStreams}$ and
$\mathsf{totalDeferredOutput}$ restricted to $\mathsf{DEFERRED\_POOL}$; the
Deferred Dev Fund Lockbox and its disbursement rules under ZIP 271 are
unchanged. [^zip-0271]

## Redirected amount

In § 7.8 ‘Calculating Block Subsidy, Funding Streams, Lockbox Disbursement, and
Founders' Reward’, [^protocol-subsidies] retain the existing definition of
$\mathsf{fs.Value}(h)$ for each funding stream, and add
$\mathsf{totalFDLDFOutput}(h)$: the sum of those values over active
streams whose recipient is $\mathsf{FDLDF\_POOL}$. This ZIP introduces
only `FS_FDLDF_H3`, so:

$$
\mathsf{totalFDLDFOutput}(h) := \begin{cases}
\left\lfloor \dfrac{8 \cdot \mathsf{BlockSubsidy}(h)}{100} \right\rfloor,
& A \leq h < E \\
0, & \text{otherwise.}
\end{cases}
$$

Here $h$ is a block height.
$\mathsf{BlockSubsidy}$ is the total block subsidy under the consensus rules in
effect at $h$, including ZIP 218's rescaling and ZIP 237's definition as
$\mathsf{ScheduledBlockSubsidy}(h) + \mathsf{AdditionalBlockSubsidy}(h)$.

The definition of $\mathsf{MinerSubsidy}$ continues to subtract the values of all
funding streams, including `FS_FDLDF_H3`. The 8% and 12% stream values
MUST be rounded down separately, as under the existing rules; their combined
value MUST NOT be calculated by rounding a single 20% allocation.

## Coinbase accounting

In § 7.1.2 ‘Transaction Consensus Rules’, [^protocol-txnconsensus] add
$\mathsf{totalFDLDFOutput}(h)$ to the definition of the coinbase
transaction's $\mathsf{totalOutputValue}$, in addition to its existing
components, including $\mathsf{totalDeferredOutput}(h)$. Retain the NU7
definition of $\mathsf{totalInputValue}$ from ZIP 235: [^zip-0235]

$$
\mathsf{BlockSubsidy}(h) + \mathsf{MinerFees}(h) + \mathsf{totalDeferredInput}(h).
$$

Here $\mathsf{MinerFees}(h)$ excludes
$\mathsf{NSMFeeContribution}(h)$, the 60% of aggregate transaction fees
removed from circulation under ZIP 235, rounded down once per block.
That fee contribution is unaffected by this ZIP.

The requirement that $\mathsf{totalOutputValue}$ equal
$\mathsf{totalInputValue}$ continues to apply. [^zip-0236] Consequently the
value claimable through coinbase outputs is reduced by exactly
$\mathsf{totalFDLDFOutput}(h)$.

These rules apply to both version 5 and version 6 coinbase transactions, the
transaction versions retained by NU7. [^zip-0259] This ZIP adds no field or
transaction encoding.

## The Future Dev and Legal Defense Fund Lockbox balance

Define the Future Dev and Legal Defense Fund Lockbox chain value pool balance for a chain through
height $h$ as:

$$
F(h) := \sum_{i=0}^{h} \mathsf{totalFDLDFOutput}(i).
$$

Here $i$ is a summation index over block heights. In § 4.17, add $F(h)$ as a
chain value pool balance, included exactly once in $\mathsf{IssuedSupply}(h)$.
The balance is zero before $A$ and remains at $F(E-1)$ for $h \geq E$. No
withdrawals are authorized. Full validators MUST track or equivalently derive
$F(h)$ for the chain being validated, including after reorganizations.

In ZIP 209's Specification, add the Future Dev and Legal Defense Fund Lockbox to the list of pools
whose balances MUST be nonnegative and whose sum MUST NOT exceed
$\mathsf{MAX\_MONEY}$; these additions apply at $A$ on each network, and
ZIP 209's original unsynchronized deployment procedure does not apply to them.
[^zip-0209] Arithmetic for the lockbox deposits MUST be evaluated exactly
without overflow, including intermediate products and sums. A block that would
produce a stream value outside its specified bounds MUST be rejected.

The lockbox is deliberately inert:

* The balance MUST NOT be treated as allocated to ZCG or any other
  beneficiary. ZCG has no entitlement, priority, or presumption of eventual
  access, and the grant and keyholder procedures in ZIPs 1015, 1016, and 271
  provide no authority over it.
* Any disposition, including withdrawal for future development or legal
  defense, MUST be specified and adopted through a separate consensus proposal. Until that
  proposal activates, the balance MUST remain locked, including after inflows
  end.
* There is no deadline requiring a disposition.

The lockbox holds issued currency. Crediting it MUST NOT decrease
$\mathsf{IssuedSupply}(h)$, increase the NSM Value Balance, or alter
$\mathsf{AdditionalBlockSubsidy}$.

## Voluntary NSM contributions

The designated NSM address is the P2SH address with script hash
`0x41c98a140039816273e50db317422c11c2bfcc88`, under the encoding in § 5.6.1.1
‘Transparent Addresses’: [^protocol-transparentaddrencoding]

* Mainnet: `t3QZUHYkaEQEuWosAc9HgMPKiQRdvuBPCQZ` (version prefix `0x1CBD`)
* Testnet: `t2CYfLDri6rrH4WSuXtHiu1WMWus6kFY2Ea` (version prefix `0x1CBA`)

The redeem script on both networks is the one-byte script `0x6a`,
`OP_RETURN`, which fails evaluation regardless of what a spender supplies.
Anyone can check this from the ZIP alone: decode the address with Base58Check,
confirm the version prefix and checksum, and compare the script hash with
HASH160 of the byte `0x6a`. Spending from the address would require a second
script with the same HASH160, contradicting second-preimage resistance.

Define $\mathsf{totalDesignatedOutput}(h)$ as the sum of the values of all
transparent outputs in block $h$, in any transaction including the coinbase
transaction, whose script is exactly the 23-byte P2SH script
`0xa91441c98a140039816273e50db317422c11c2bfcc8887`; and the cumulative total
$\mathsf{DesignatedBefore}(h) := \sum_{i=0}^{h-1} \mathsf{totalDesignatedOutput}(i)$.

For $h \geq A$:

* A transaction that spends an output whose script is exactly that P2SH
  script is invalid, regardless of the redeem script supplied.
* In § 4.17, the transparent chain value pool balance is reduced by
  $\mathsf{totalDesignatedOutput}(h)$ in block $h$, and additionally by
  $\mathsf{DesignatedBefore}(A)$ at $h = A$. Value paid to the designated NSM
  address is thereby removed from circulation and excluded from
  $\mathsf{IssuedSupply}$.
* Extend ZIP 237's definition of $\mathsf{NSMValueRemoved}(h)$, which already
  includes ZIP 235's $\mathsf{NSMFeeContribution}(h)$, to also include
  $\mathsf{totalDesignatedOutput}(h)$, and additionally
  $\mathsf{DesignatedBefore}(A)$ at $h = A$. Each contributed zatoshi MUST be
  credited to the NSM Value Balance exactly once.

Payments made before $A$ are valid under the existing rules; the one-time
terms at $A$ credit them in
aggregate. Until then that value remains, by consensus, in the transparent
chain value pool and the Issued Supply, although it is already unspendable;
publishers of circulating-supply figures SHOULD exclude it. Because the
outputs are unspendable, the reduction at
$A$ cannot make the transparent chain value pool balance negative. Arithmetic
for these terms MUST be evaluated exactly without overflow. On a
reorganization, contributions
from disconnected blocks MUST NOT be counted toward that chain's credits.

Anyone MAY pay the designated NSM address; every such payment is a voluntary
contribution with no refund mechanism. Wallets SHOULD NOT treat the designated
NSM address as an ordinary payment destination.

## The donation

The ZCG Committee SHALL cause 50,000 ZEC of ZCG funds to be sent to the
designated NSM address on Mainnet, in one or more transactions. It SHALL do so
as soon as possible, and no later than 30 days after the date on which this ZIP
is accepted by the Zcash community. The donation does not wait for this ZIP's
activation: payments made before $A$ are credited to the NSM Value Balance at
$A$, as specified in ‘Voluntary NSM contributions’.

Since the funds ZCG administers are held by FPF, the ZCG Committee fulfills
this obligation by directing FPF to create the transactions, as it directs FPF
to make grant payments under ZIP 1015. Payments to the designated NSM address
by anyone other than FPF do not count toward the donation.

The ZCG Committee SHALL publish the transaction identifier of each such
transaction to the Zcash community promptly after it is mined.

## Legal authority

Before the donation, FPF MUST:

* obtain advice from qualified counsel in its jurisdiction of organization
  concerning its authority to execute this ZIP, including the Restricted Fund
  terms required by ZIP 1015, its constitutional documents, existing
  contracts, and any required consents or approvals;
* arrange for the commitments required by ZIPs 1015 and 1016 to be amended,
  in suitable legal language, to authorize the uses specified here;
* obtain any consent, corporate approval, or court order that an action
  requires, before taking that action; and
* publish confirmation of the authority and approvals on which it relies,
  without disclosing privileged advice or confidential information.

A ZIP MUST NOT be treated as automatically amending an agreement,
extinguishing a third party's rights, or overriding applicable law. If a
required authorization cannot be obtained for some amount, FPF MUST report the
obstacle, safeguard that amount in segregated custody solely for a future
donation to the NSM, and seek a further community decision. Such an obstacle MUST NOT
authorize an alternative recipient.

## Changes to ZIP 1015

In the Specification, under "Zcash Community Grants (ZCG)", insert a new
subsection "Donation to the NSM" immediately before "Furthering
Decentralization", with the following text: [^zip-1015-zcg]

> The permitted purposes of the ZCG Restricted Fund donation expressly include
> donating 50,000 ZEC of ZCG funds to the Network Sustainability Mechanism as
> specified by [this ZIP], and paying the reasonable documented costs of that
> donation. FPF MUST
> arrange the corresponding amendments to the restricted-fund agreements and
> obtain the legal authority required by that ZIP before executing an action
> that requires it. The NSM donation mandated by that ZIP is an authorized
> disposition of the Restricted Fund, not a grant, and compliance with that ZIP
> does not constitute a breach for the purposes of Enforcement. These purposes
> do not authorize unrelated FPF expenditure or diversion to another fund;
> retained ZCG funds remain subject to the exclusive-use restriction above.

Replace "[this ZIP]" with this ZIP's assigned identifier, and add the
corresponding reference. The existing funding-stream tables and historical
allocations in ZIP 1015 are unchanged.

## Changes to ZIP 1016

In ZIP 1016's ‘Zcash Community Grants’ subsection, [^zip-1016] replace the
funding period with $[S, A)$, and append:

> [This ZIP] specifies a donation of 50,000 ZEC of ZCG funds to the Network
> Sustainability Mechanism, under its amendments to ZIP 1015. The remaining
> ZCG funds stay available for grants under the existing rules.

From $A$ through $E - 1$, the former ZCG allocation accrues to the Future Dev
and Legal Defense Fund Lockbox as specified above; state this in the same subsection, together with
the absence of any ZCG entitlement to the lockbox.

In the first paragraph of ZIP 1016's ‘Coinholder-Controlled Fund’ subsection,
replace the references to the duration and end height of the ZCG stream with
references to `FS_CCF_H3`'s own start and end heights under ZIP 214. Its 12%
allocation and existing duration are preserved independently of ZCG's cutoff.
In ‘Administrative obligations and constraints’, state that the donation
provisions of this ZIP apply only to ZCG funds and are not incorporated into
the requirements governing the Coinholder-Controlled Fund or its Key-Holder
Organizations.

## Boundary cases and arithmetic examples

On a network where $A < E$, the existing ZCG stream is still in effect at
$A - 1$ and the lockbox stream
has no value. At $A$, the ZCG stream has ended and the lockbox stream first
takes effect. The last height at which the lockbox stream can have a nonzero
value is $E - 1$. There is no gap or overlap between the two allocations.

The following arithmetic examples, in zatoshis, illustrate the separate
per-stream rounding for a block with no other funding streams or Founders'
Reward. The 52083333 row equals the scheduled block subsidy during $[A, E)$
under the current deployment parameters; the other rows are synthetic.
Here $B$ is the total block
subsidy, $D$ is the lockbox deposit, $C$ is the 12% CCF deposit, and $M$ is the
miner subsidy, excluding transaction fees and any deferred-pool disbursement.

| $B$ | $D = \lfloor 8B/100 \rfloor$ | $C = \lfloor 12B/100 \rfloor$ | $M = B - D - C$ |
| --: | --: | --: | --: |
| 156250000 | 12500000 | 18750000 | 125000000 |
| 52083333 | 4166666 | 6249999 | 41666668 |
| 99 | 7 | 11 | 81 |
| 1 | 0 | 0 | 1 |
| 0 | 0 | 0 | 0 |

For the designated NSM address: if blocks before $A$ contain payments to it
totalling 5,000,000,000,000 zatoshis (50,000 ZEC) and block $A$ contains a
further payment of 100,000,000 zatoshis, then at $A$ the transparent chain
value pool balance decreases by 5,000,100,000,000 zatoshis beyond its ordinary
movements, and $\mathsf{NSMValueRemoved}(A)$ includes the same amount in
addition to its ZIP 235 fee component.


# Rationale

## Ending automatic funding

The financial examples in Motivation support this ZIP's conclusion that
additional automatic allocations are no longer necessary.

Those examples use a range of prices and a spending level above the annualized
Q1 figure. The proposal leaves treasury management and grant selection with the
existing institutions.

Reducing the stream rather than ending it would continue allocating new subsidy
to a program that this ZIP concludes is already sufficiently funded. A
price-triggered cap or automatic restart would introduce a different funding
policy and additional dependencies. This ZIP instead makes a single prospective
allocation change.

## A lockbox for the stream, the NSM for the donation

The two destinations reflect the different standing of the two amounts. The
redirected stream is future issuance whose use the community has yet to
specify; holding it in a lockbox, issued but locked, sets it aside for future
development and legal defense, and leaves how, and by whom, it is spent to a
later consensus change. The donation is value already issued, from a treasury
larger than its program needs; returning it
through the NSM gives it back to the network under a protocol-defined
mechanism, rather than transferring it to another discretionary recipient or
leaving it under custody it no longer requires.

Crediting the stream to the NSM instead, as the companion proposal does, would
settle its monetary disposition at activation. [^draft-end-zcg-stream]
Combining the redirected stream with the Deferred Dev Fund Lockbox would
subject it to that pool's development-funding purpose and disbursement
machinery. A separate pool keeps the balances and their purposes distinct, and
unlike a multisig requires no custodians or spending keys.

## A fixed donation instead of a wind-down

A full wind-down, as proposed separately, [^draft-wind-down-zcg] would close
the grants program and contribute everything beyond commitments and closure
costs. This ZIP keeps the program operating, preserves grantee relationships,
and donates a fixed 50,000 ZEC. A fixed amount in ZEC can be paid at once and
checked by anyone from the chain, with no valuation, reserve formula, or
annual redetermination; ZCG keeps the rest of its treasury. Full closure
remains available as a later step; a closed program would not be as easily
restored.

## An address-based contribution mechanism

ZIP 233 proposes a transaction field for removing funds from circulation, but
NU7 deploys neither ZIP 233 nor ZIP 234. [^zip-0233] [^zip-0259] Without a
deployed mechanism, a treasury obligation would reduce to indefinite custody
pending a future upgrade. This ZIP instead recognizes payments to a single
designated unspendable address: the consensus surface is small — no new
transaction fields, address formats, or wallet changes — and the one-time
credit at $A$ lets contributions begin as soon as the community process
concludes, rather than after activation.

An address-based mechanism lacks ZIP 233's
explicit per-transaction opt-in semantics; a mistaken payment to the designated
NSM address is unrecoverable, which is why wallets should not present it as an
ordinary destination. Unspendability of a P2SH output is verifiable only from
its redeem script, which this ZIP records. Crediting third-party
payments is intentional: the mechanism is a general voluntary contribution
path, though only FPF's payments count toward the donation. The one-time
credit at $A$ also covers earlier donations to the same address under other
community initiatives, which otherwise await a future upgrade. If ZIP 233 is
later deployed, both mechanisms credit the same NSM Value Balance, and a
revision MAY retire the designated address for new contributions.

## Accounting

The reduction in claimable coinbase value and the corresponding lockbox deposit
account for the same redirected amount. The existing per-stream rounding and
miner-subsidy formula preserve the miner's share for a given total subsidy. The
proposal changes the destination of the former ZCG allocation; the fraction
deducted from that subsidy is unchanged.

Lockbox deposits remain in the Issued Supply, so they do not disturb ZIP 237's
invariant that the sum of the Issued Supply and the NSM Value Balance increases
by exactly the Scheduled Block Subsidy in each block from NU7 onward. A
designated-address contribution decreases the transparent chain value pool
balance and increases the NSM Value Balance by the same amount in the same
block — including the one-time terms at $A$ — so the invariant is preserved
there as well. Contributed value re-enters circulation only through
$\mathsf{AdditionalBlockSubsidy}$ under ZIP 237.


# Deployment

This ZIP is not included in NU7 as currently specified by ZIP 259. [^zip-0259]
It is proposed for a network upgrade that activates before the existing ZCG
stream expires and satisfies the dependencies in ‘Activation and dependencies’.
The specification builds on NU7's funding-stream rules and ZIPs 235 and 237.

Mainnet and Testnet activation heights for this ZIP are unassigned; the NU7
activation heights are separate parameters. A deployment ZIP will specify this
ZIP's activation heights and the network upgrade parameters under ZIP 200.
[^zip-0200]

Activation SHOULD allow reasonable notice to ZCG and affected grantees after
compatible software is released, taking existing commitments into account.
The contribution process MAY be rehearsed on Testnet using the Testnet
designated NSM address; Testnet activity MUST NOT be counted toward, or treated
as discharging, any Mainnet obligation.


# Reference implementation

None yet.


# Open issues

* Obtain FPF's legal review of the Restricted Fund arrangements, constitutional
  documents, and required consents.
* Reconcile this proposal with the companion stream proposal and the separate
  wind-down proposal, which amend the same ZIPs with incompatible dispositions.
  [^draft-end-zcg-stream] [^draft-wind-down-zcg]


# References

[^BCP14]: [Information on BCP 14 — RFC 2119 and RFC 8174](https://www.rfc-editor.org/info/bcp14)

[^protocol]: [Zcash Protocol Specification](protocol/protocol.pdf)

[^protocol-chainvaluepoolbalances]: [Zcash Protocol Specification, § 4.17: Chain Value Pool Balances](protocol/protocol.pdf#chainvaluepoolbalances)

[^protocol-constants]: [Zcash Protocol Specification, § 5.3: Constants](protocol/protocol.pdf#constants)

[^protocol-transparentaddrencoding]: [Zcash Protocol Specification, § 5.6.1.1: Transparent Addresses](protocol/protocol.pdf#transparentaddrencoding)

[^protocol-txnconsensus]: [Zcash Protocol Specification, § 7.1.2: Transaction Consensus Rules](protocol/protocol.pdf#txnconsensus)

[^protocol-subsidies]: [Zcash Protocol Specification, § 7.8: Calculating Block Subsidy, Funding Streams, Lockbox Disbursement, and Founders' Reward](protocol/protocol.pdf#subsidies)

[^protocol-fundingstreams]: [Zcash Protocol Specification, § 7.10: Payment of Funding Streams, Deferred Lockbox, and Lockbox Disbursement](protocol/protocol.pdf#fundingstreams)

[^zip-0000]: [ZIP 0: ZIP Process](zip-0000.rst)

[^zip-0200]: [ZIP 200: Network Upgrade Mechanism](zip-0200.rst)

[^zip-0207]: [ZIP 207: Funding Streams](zip-0207.rst)

[^zip-0209]: [ZIP 209: Prohibit Out-of-Range Chain Value Pool Balances](zip-0209.rst)

[^zip-0214]: [ZIP 214: Consensus rules for a Zcash Development Fund](zip-0214.rst)

[^zip-0218]: [ZIP 218: 25-second Block Target Spacing](zip-0218.md)

[^zip-0233]: [ZIP 233: Network Sustainability Mechanism: Removing Funds From Circulation](zip-0233.md)

[^zip-0235]: [ZIP 235: Remove 60% of Transaction Fees From Circulation](zip-0235.md)

[^zip-0236]: [ZIP 236: Blocks should balance exactly](zip-0236.rst)

[^zip-0237]: [ZIP 237: Network Sustainability Mechanism: Halving-Preserving Issuance](zip-0237.md)

[^zip-0259]: [ZIP 259: Deployment of the NU7 Network Upgrade](zip-0259.md)

[^zip-0271]: [ZIP 271: Dev Fund Extension and One-Time Disbursement](zip-0271.md)

[^zip-1015]: [ZIP 1015: Block Subsidy Allocation for Non-Direct Development Funding](zip-1015.rst)

[^zip-1015-zcg]: [ZIP 1015: Block Subsidy Allocation for Non-Direct Development Funding — Zcash Community Grants](zip-1015.rst#zcash-community-grants-zcg)

[^zip-1016]: [ZIP 1016: Community and Coinholder Funding Model](zip-1016.md)

[^zip-2001]: [ZIP 2001: Lockbox Funding Streams](zip-2001.rst)

[^zip-2008]: [ZIP 2008: Update to `FS_FPF_ZCG_H3` address list](zip-2008.md)

[^draft-end-zcg-stream]: [Draft: Ending the ZCG Funding Stream in Favor of the NSM (zcash/zips#1414)](https://github.com/zcash/zips/pull/1414)

[^draft-wind-down-zcg]: [Draft: Winding Down Zcash Community Grants (zcash/zips#1423)](https://github.com/zcash/zips/pull/1423)

[^fpf-q2-2026]: [Financial Privacy Foundation: Q2 2026 Report, p. 5 (ZCG statistics, with total expenses for Q1 and Q2 2026)](https://9ba4718c-5c73-47c3-a024-4fc4e5278803.usrfiles.com/ugd/9ba471_0836532577dd4f0eab3cf5080820e622.pdf). Q2's total includes \$1,216,687 of Discretionary Fund usage, versus \$54,108 in Q1, so neither quarter alone indicates recurring spending.

[^zcg-dashboard]: [Zcash Community Grants website](https://zcashcommunitygrants.org/) and its linked [Zcash Community Grants + Coinholder Grants Dashboard](https://docs.google.com/spreadsheets/d/1FQ28rDCyRW0TiNxrm3rgD8ai2KGUsXAjPieQmI1kKKg/edit?usp=sharing), accessed October 26, 2026. The recorded inputs are 91,452.98 ZEC, USD 8,796,224, and USD 2,417,165 in grant liabilities. The dashboard's block reference is 3,526,011 (October 21, 2026, 22:37:53 UTC), and the worksheet is marked “Updates required”. The figures are reported dashboard inputs and have not been independently reconciled.

[^financial-scenarios]: Calculations from the recorded dashboard inputs: at a price of P USD per ZEC, reported holdings less reported grant liabilities equal `91,452.98 * P + 8,796,224 - 2,417,165` USD. At P = 1,300, 1,000, and 500, the results are USD 125,267,933, 97,832,039, and 52,105,549, respectively. Spending comparisons divide these values by an illustrative USD 10,000,000 per year. The calculations assume realization of the stated valuations without conversion costs, constant nominal spending, no further receipts or investment returns, and no obligations beyond the dashboard's grant-liability entry.

[^stream-scenarios]: Calculations using ZIP 214's 8% allocation and the subsidy and block target spacing described in ZIP 218: `0.08 * 1.5625 * (86,400 / 75) = 144` ZEC per day; `144 * 365 = 52,560` ZEC per year. At USD 1,300 per ZEC, these are USD 187,200 and USD 68,328,000. At 25-second spacing, the per-stream integer rule gives 4,166,666 zatoshis per block, or 143.99997696 ZEC per target-spaced day. The illustrations use the scheduled subsidy before the third halving, a fixed price, and the target block rate. The first-half annualized comparison is `(1,530,844 + 3,187,515) * 2 = 9,436,718` USD, and `68,328,000 / 9,436,718` is approximately 7.24. See [ZIP 214](https://zips.z.cash/zip-0214), [ZIP 218](https://zips.z.cash/zip-0218), and the Q2 report.

[^donation-scenarios]: Calculations from the recorded dashboard inputs: after a donation of 50,000 ZEC, at a price of P USD per ZEC, retained holdings less reported grant liabilities equal `41,452.98 * P + 8,796,224 - 2,417,165` USD. At P = 1,300, 1,000, and 500, the donation is worth USD 65,000,000, 50,000,000, and 25,000,000, and the retained value USD 60,267,933, 47,832,039, and 27,105,549, respectively. Spending comparisons divide the retained values by an illustrative USD 10,000,000 per year. The calculations assume realization of the stated valuations without conversion costs, constant nominal spending, no further receipts or investment returns, and no obligations beyond the dashboard's grant-liability entry.
