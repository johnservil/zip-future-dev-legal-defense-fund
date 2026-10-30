# Draft ZIP: Future Dev and Legal Defense Fund Lockbox

A draft Zcash Improvement Proposal, for review before submission to
[zcash/zips](https://github.com/zcash/zips):
[`zip-draft-future-dev-legal-defense-fund.md`](zip-draft-future-dev-legal-defense-fund.md).

It makes two changes, approved together as one proposal:

1. From its activation until Zcash's third halving, the 8% of the block
   subsidy that now goes to Zcash Community Grants (`FS_FPF_ZCG_H3`) goes
   instead into a new lockbox, the Future Dev and Legal Defense Fund. It
   works like the existing Deferred Dev Fund Lockbox (ZIP 2001), but it is
   a separate reserve.
2. The ZCG Committee donates 50,000 ZEC to the Network Sustainability
   Mechanism as soon as possible, by sending it to
   `t3QZUHYkaEQEuWosAc9HgMPKiQRdvuBPCQZ`, a P2SH address whose script is
   `OP_RETURN`, so no one can spend from it. A future network upgrade is
   to recycle it into the mechanism (ZIP 233).
   [`verify_nsm_donation_address.py`](verify_nsm_donation_address.py)
   checks the address.

Places marked `[TODO: Zooko]` await the owner's decision.
