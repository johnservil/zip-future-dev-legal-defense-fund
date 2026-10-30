# Draft ZIP: Future Dev and Legal Defense Fund Lockbox, and a 50,000 ZEC donation to the NSM

A draft Zcash Improvement Proposal, for review before submission to
[zcash/zips](https://github.com/zcash/zips):
[`zip-draft-future-dev-legal-defense-fund.md`](zip-draft-future-dev-legal-defense-fund.md).
Its authors are Sean Bowe (Tachyon Group), Zooko Wilcox (Shielded Labs), and
Jason McGee (Shielded Labs). It builds on Sean's
[draft](https://gist.github.com/ebfull/1610cbddaf59c0f74760fa14a25a3c41).

It makes two changes, approved together as one proposal:

1. At its activation, Zcash Community Grants' 8% funding stream ends, and
   until the third halving the same 8% accrues to a new lockbox, the Future
   Dev and Legal Defense Fund. It works like the Deferred Dev Fund Lockbox,
   but it is a separate reserve, and a later consensus change decides how it
   is spent.
2. The ZCG Committee donates 50,000 ZEC to the Network Sustainability
   Mechanism within 30 days of the ZIP's acceptance, by sending it to
   `t3QZUHYkaEQEuWosAc9HgMPKiQRdvuBPCQZ`, a P2SH address whose script is
   `OP_RETURN`, so no one can spend from it. At activation, everything sent
   there is removed from circulation and credited to the NSM.
   [`verify_nsm_donation_address.py`](verify_nsm_donation_address.py)
   checks the address, and its Testnet counterpart.
