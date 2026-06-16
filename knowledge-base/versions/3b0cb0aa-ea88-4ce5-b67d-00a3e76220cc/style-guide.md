# 语言风格画像

## 总体判断

该版本整体呈现解释性、学习型翻译风格：保留巴利词形、显化定义关系、用方括号补足信息，并用换行拆分复杂解释。

## 可量化信号

| Dimension | Observation | Count |
| --- | --- | --- |
| pali_retention | 译文经常用括号保留巴利词形。 | 205 |
| translator_supplement | 译文使用方括号补出隐含或解释性内容。 | 142 |
| line_break_decomposition | 译文使用换行拆分并列解释或复杂词源分析。 | 390 |

## 风险

- 括号和方括号内容应与正文译文分层处理。
- 换行可能表示语义层级，不应在清洗时无条件删除。
- 自动抽取的中文词边界需要人工校订。

## 条目

## style-parenthetical-pali

```yaml
id: style-parenthetical-pali
version_id: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc
type: style_observation
name: pali_retention
description: 译文经常用括号保留巴利词形。
dimension: pali_retention
observation: 译文经常用括号保留巴利词形。
occurrence_count: 205
evidence:
- unit_id: 9-555-2-11
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-555-2-11
  line: 6
  source_quote: '183. Vedena paññāya īhanti etthāti vedeho. '
  target_quote: 那里他们敏而勤学吠陀，而成为勤学者(vedeha)。
- unit_id: 9-556-122-177
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-556-122-177
  line: 10
  source_quote: Kala sadde, iṅga paccayo, kaliṅgā , tesaṃ nivāso kaliṅgā, uttarāpatho[‘‘
    jagannāthā pubbabhāge kaṇhātīrantaraṃ sive kaliṅgadeso saṃvutto’’ ityuttadese(
    thomanidhi)], kaliṃ gaṇhantīti vā kaliṅgā, kvi, kalaṃ madhurasaddaṃ gāyantītivā
    kaliṅgā, assittaṃ, kena sukh…
  target_quote: 'kala意为声音，iṅga意为缘，[ 音缘国(kaliṅga)王子]他们的住所，即[kaliṅga]]，位于[ 莲雾洲 ]北部地区[的国家]；

    困苦（kali）的获取（gaha）故为 音缘国，达成；

    将甜美的声音（kala）唱（ge）出来故为 音缘国，其[额外]有[字母]“i”；

    能通过任何（ka）快乐来促成（liṅga）故为 音缘国，liṅga意为是促成，daṇḍaka为词根(dhātu2)。'
- unit_id: 9-821-125-144
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-821-125-144
  line: 16
  source_quote: 'Koseyyameva dhotaṃ paṭṭuṇṇaṃ nāma, vuttañca‘‘ paṭṭuṇṇaṃ dhotakoseyyan’’
    ti[ amara16.113]. '
  target_quote: 將茧丝(koseyya)洗淨名為paṭṭuṇṇa，或者說“paṭṭuṇṇa即洗乾淨的茧丝”。
- unit_id: 9-821-198-221
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-821-198-221
  line: 18
  source_quote: 'Saṇa sadde, kattari a, saṇo nāma thirattaco eko rukkhayoni, yassa
    tacena kevaṭṭādayo jālādīni karonti, saṇassa vikāro sāṇaṃ, vatthaṃ. '
  target_quote: saṇa這個詞【強化？】a，所謂saṇa即同源樹的韌皮部，漁夫等利用其樹皮可以製作網等，saṇa變麻(sāṇa)，[而成為]布料。
- unit_id: 14-2011-2-5
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:14-2011-2-5
  line: 23
  source_quote: 'Karaṇakārake tatiyāvibhatti hoti. '
  target_quote: 第三变格(tatiyāvibhatti)表达方式状语的用法。
- unit_id: 14-2019-2-9
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:14-2019-2-9
  line: 29
  source_quote: '289,297. Hetvatthe ca. '
  target_quote: 表达原因状语(hetvattha)。
- unit_id: 14-2023-2-6
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:14-2023-2-6
  line: 31
  source_quote: 'Sattamyatthe ca tatiyāvibhatti hoti. '
  target_quote: 第三变格表达第七格含义(sattamyattha)。
- unit_id: 14-2059-2-9
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:14-2059-2-9
  line: 32
  source_quote: '302,319. Okāse sattamī. '
  target_quote: 在表示地点状语(okāsa)时，用第七变格(sattamīvibhatti)。
evidence_ids:
- ev-001140
- ev-001141
- ev-001142
- ev-001143
- ev-001144
- ev-001145
- ev-001146
- ev-001147
- ev-001148
- ev-001149
- ev-001150
- ev-001151
- ev-001152
- ev-001153
- ev-001154
- ev-001155
- ev-001156
- ev-001157
- ev-001158
- ev-001159
- ev-001160
- ev-001161
- ev-001162
- ev-001163
- ev-001164
- ev-001165
- ev-001166
- ev-001167
- ev-001168
- ev-001169
- ev-001170
- ev-001171
- ev-001172
- ev-001173
- ev-001174
- ev-001175
- ev-001176
- ev-001177
- ev-001178
- ev-001179
- ev-001180
- ev-001181
- ev-001182
- ev-001183
- ev-001184
- ev-001185
- ev-001186
- ev-001187
- ev-001188
- ev-001189
- ev-001190
- ev-001191
- ev-001192
- ev-001193
- ev-001194
- ev-001195
- ev-001196
- ev-001197
- ev-001198
- ev-001199
- ev-001200
- ev-001201
- ev-001202
- ev-001203
- ev-001204
- ev-001205
- ev-001206
- ev-001207
- ev-001208
- ev-001209
- ev-001210
- ev-001211
- ev-001212
- ev-001213
- ev-001214
- ev-001215
- ev-001216
- ev-001217
- ev-001218
- ev-001219
- ev-001220
- ev-001221
- ev-001222
- ev-001223
- ev-001224
- ev-001225
- ev-001226
- ev-001227
- ev-001228
- ev-001229
- ev-001230
- ev-001231
- ev-001232
- ev-001233
- ev-001234
- ev-001235
- ev-001236
- ev-001237
- ev-001238
- ev-001239
- ev-001240
- ev-001241
- ev-001242
- ev-001243
- ev-001244
- ev-001245
- ev-001246
- ev-001247
- ev-001248
- ev-001249
- ev-001250
- ev-001251
- ev-001252
- ev-001253
- ev-001254
- ev-001255
- ev-001256
- ev-001257
- ev-001258
- ev-001259
- ev-001260
- ev-001261
- ev-001262
- ev-001263
- ev-001264
- ev-001265
- ev-001266
- ev-001267
- ev-001268
- ev-001269
- ev-001270
- ev-001271
- ev-001272
- ev-001273
- ev-001274
- ev-001275
- ev-001276
- ev-001277
- ev-001278
- ev-001279
- ev-001280
- ev-001281
- ev-001282
- ev-001283
- ev-001284
- ev-001285
- ev-001286
- ev-001287
- ev-001288
- ev-001289
- ev-001290
- ev-001291
- ev-001292
- ev-001293
- ev-001294
- ev-001295
- ev-001296
- ev-001297
- ev-001298
- ev-001299
- ev-001300
- ev-001301
- ev-001302
- ev-001303
- ev-001304
- ev-001305
- ev-001306
- ev-001307
- ev-001308
- ev-001309
- ev-001310
- ev-001311
- ev-001312
- ev-001313
- ev-001314
- ev-001315
- ev-001316
- ev-001317
- ev-001318
- ev-001319
- ev-001320
- ev-001321
- ev-001322
- ev-001323
- ev-001324
- ev-001325
- ev-001326
- ev-001327
- ev-001328
- ev-001329
- ev-001330
- ev-001331
- ev-001332
- ev-001333
- ev-001334
- ev-001335
- ev-001336
- ev-001337
- ev-001338
- ev-001339
- ev-001340
- ev-001341
- ev-001342
- ev-001343
- ev-001344
confidence: 0.75
review_status: machine_generated
```

## style-bracket-supplement

```yaml
id: style-bracket-supplement
version_id: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc
type: style_observation
name: translator_supplement
description: 译文使用方括号补出隐含或解释性内容。
dimension: translator_supplement
observation: 译文使用方括号补出隐含或解释性内容。
occurrence_count: 142
evidence:
- unit_id: 9-556-122-177
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-556-122-177
  line: 10
  source_quote: Kala sadde, iṅga paccayo, kaliṅgā , tesaṃ nivāso kaliṅgā, uttarāpatho[‘‘
    jagannāthā pubbabhāge kaṇhātīrantaraṃ sive kaliṅgadeso saṃvutto’’ ityuttadese(
    thomanidhi)], kaliṃ gaṇhantīti vā kaliṅgā, kvi, kalaṃ madhurasaddaṃ gāyantītivā
    kaliṅgā, assittaṃ, kena sukh…
  target_quote: 'kala意为声音，iṅga意为缘，[ 音缘国(kaliṅga)王子]他们的住所，即[kaliṅga]]，位于[ 莲雾洲 ]北部地区[的国家]；

    困苦（kali）的获取（gaha）故为 音缘国，达成；

    将甜美的声音（kala）唱（ge）出来故为 音缘国，其[额外]有[字母]“i”；

    能通过任何（ka）快乐来促成（liṅga）故为 音缘国，liṅga意为是促成，daṇḍaka为词根(dhātu2)。'
- unit_id: 9-821-148-153
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-821-148-153
  line: 17
  source_quote: 'Paṭṭuṇṇaraṭṭhe jātattā paṭṭuṇṇan tipi vadanti. '
  target_quote: '[很多人]也說，由於在paṭṭuṇṇaraṭṭha生產而為paṭṭuṇṇa。'
- unit_id: 9-821-198-221
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-821-198-221
  line: 18
  source_quote: 'Saṇa sadde, kattari a, saṇo nāma thirattaco eko rukkhayoni, yassa
    tacena kevaṭṭādayo jālādīni karonti, saṇassa vikāro sāṇaṃ, vatthaṃ. '
  target_quote: saṇa這個詞【強化？】a，所謂saṇa即同源樹的韌皮部，漁夫等利用其樹皮可以製作網等，saṇa變麻(sāṇa)，[而成為]布料。
- unit_id: 14-2070-2-9
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:14-2070-2-9
  line: 42
  source_quote: 'Rudato dārakassa pabbaji, rudantasmiṃ dārake pabbaji. '
  target_quote: '即使孩子在哭第六变格[他]也出家了，

    即使孩子在哭第七变格[他]也出家了。'
- unit_id: 41-730-2-13
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:41-730-2-13
  line: 93
  source_quote: 'Svākkhāto bhagavatā dhammo sandiṭṭhiko akāliko ehi passiko opaneyyiko
    paccattaṃ veditabbo viññūhi– '
  target_quote: 已被世尊说得很好的法是亲见的，是超越时间的，是公开的，是通往[涅槃]的，是可被智者本人所了知的——
- unit_id: 64-199-44-57
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:64-199-44-57
  line: 102
  source_quote: 'Yo sarīrābādhacittavikkhepakaro asappāyo utu senāsanapaṭisevanena
    vinodetabbo hoti, tassa vinodanatthaṃ ekībhāvasukhatthañcāti vuttaṃ hoti. '
  target_quote: 说的是：身体疼痛能造成心分散的身体的不合适、折磨人的季候可通过受用住所而规避，因为规避[季候]而同时获得的出离乐。
- unit_id: 65-1499-241-251
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:65-1499-241-251
  line: 214
  source_quote: 'Taṇhādiṭṭhiduccaritasaṃkilesānaṃ visayadhammatāya {saṃkilesikadhammato}ti
    evaṃ pabhedato vuttassa aniccādisammasanassa vasena sammasati. '
  target_quote: '由于渴爱成见不善行（等十种）诸烦恼的[所缘]境法——

    由于saṃkilesikadhamma'
- unit_id: 66-340-10-27
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:66-340-10-27
  line: 253
  source_quote: '{Avitakkasahagatā}ti‘‘ kathaṃ nu kho me avitakkaṃ jhānaṃ bhaveyyā’’
    ti evaṃ avitakkārammaṇā avitakkavisayā. '
  target_quote: 没有贯注伴随，“我的没有贯注的禅那会是怎样的呢？”这样的（那些）没有贯注的目标，（那些）没有贯注的[所缘]境。
evidence_ids:
- ev-001345
- ev-001346
- ev-001347
- ev-001348
- ev-001349
- ev-001350
- ev-001351
- ev-001352
- ev-001353
- ev-001354
- ev-001355
- ev-001356
- ev-001357
- ev-001358
- ev-001359
- ev-001360
- ev-001361
- ev-001362
- ev-001363
- ev-001364
- ev-001365
- ev-001366
- ev-001367
- ev-001368
- ev-001369
- ev-001370
- ev-001371
- ev-001372
- ev-001373
- ev-001374
- ev-001375
- ev-001376
- ev-001377
- ev-001378
- ev-001379
- ev-001380
- ev-001381
- ev-001382
- ev-001383
- ev-001384
- ev-001385
- ev-001386
- ev-001387
- ev-001388
- ev-001389
- ev-001390
- ev-001391
- ev-001392
- ev-001393
- ev-001394
- ev-001395
- ev-001396
- ev-001397
- ev-001398
- ev-001399
- ev-001400
- ev-001401
- ev-001402
- ev-001403
- ev-001404
- ev-001405
- ev-001406
- ev-001407
- ev-001408
- ev-001409
- ev-001410
- ev-001411
- ev-001412
- ev-001413
- ev-001414
- ev-001415
- ev-001416
- ev-001417
- ev-001418
- ev-001419
- ev-001420
- ev-001421
- ev-001422
- ev-001423
- ev-001424
- ev-001425
- ev-001426
- ev-001427
- ev-001428
- ev-001429
- ev-001430
- ev-001431
- ev-001432
- ev-001433
- ev-001434
- ev-001435
- ev-001436
- ev-001437
- ev-001438
- ev-001439
- ev-001440
- ev-001441
- ev-001442
- ev-001443
- ev-001444
- ev-001445
- ev-001446
- ev-001447
- ev-001448
- ev-001449
- ev-001450
- ev-001451
- ev-001452
- ev-001453
- ev-001454
- ev-001455
- ev-001456
- ev-001457
- ev-001458
- ev-001459
- ev-001460
- ev-001461
- ev-001462
- ev-001463
- ev-001464
- ev-001465
- ev-001466
- ev-001467
- ev-001468
- ev-001469
- ev-001470
- ev-001471
- ev-001472
- ev-001473
- ev-001474
- ev-001475
- ev-001476
- ev-001477
- ev-001478
- ev-001479
- ev-001480
- ev-001481
- ev-001482
- ev-001483
- ev-001484
- ev-001485
- ev-001486
confidence: 0.75
review_status: machine_generated
```

## style-newline-decomposition

```yaml
id: style-newline-decomposition
version_id: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc
type: style_observation
name: line_break_decomposition
description: 译文使用换行拆分并列解释或复杂词源分析。
dimension: line_break_decomposition
observation: 译文使用换行拆分并列解释或复杂词源分析。
occurrence_count: 390
evidence:
- unit_id: 9-95-17-30
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-95-17-30
  line: 3
  source_quote: 'Mī hiṃsāyaṃ, mināti hiṃsati sabbe pabbate attano uccataraṭṭhenāti
    meru, ru paccayo. '
  target_quote: '“mī”，有伤害，丈量，压倒性，在众山中其自身更高，而成为压迫“meru”，ru

    是后缀。'
- unit_id: 9-112-49-59
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-112-49-59
  line: 5
  source_quote: 'Virūpāni akkhīni yassa virūpakkho, vividhasaṇṭhānāni akkhīni yassa
    vā virūpakkho. '
  target_quote: '他的眼睛丑陋为异眸，

    或他的眼睛形态各异为异眸。'
- unit_id: 9-556-90-101
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-556-90-101
  line: 9
  source_quote: 'Magena saddhiṃ dhāvantīti magadhā, kvi, maṃsesu gijjhantīti vā magadhā. '
  target_quote: '与鹿一起奔跑，为magadhā，

    在肉方面有渴望的，为magadhā。'
- unit_id: 9-556-122-177
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-556-122-177
  line: 10
  source_quote: Kala sadde, iṅga paccayo, kaliṅgā , tesaṃ nivāso kaliṅgā, uttarāpatho[‘‘
    jagannāthā pubbabhāge kaṇhātīrantaraṃ sive kaliṅgadeso saṃvutto’’ ityuttadese(
    thomanidhi)], kaliṃ gaṇhantīti vā kaliṅgā, kvi, kalaṃ madhurasaddaṃ gāyantītivā
    kaliṅgā, assittaṃ, kena sukh…
  target_quote: 'kala意为声音，iṅga意为缘，[ 音缘国(kaliṅga)王子]他们的住所，即[kaliṅga]]，位于[ 莲雾洲 ]北部地区[的国家]；

    困苦（kali）的获取（gaha）故为 音缘国，达成；

    将甜美的声音（kala）唱（ge）出来故为 音缘国，其[额外]有[字母]“i”；

    能通过任何（ka）快乐来促成（liṅga）故为 音缘国，liṅga意为是促成，daṇḍaka为词根(dhātu2)。'
- unit_id: 9-556-219-228
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-556-219-228
  line: 11
  source_quote: 'Gaṃ pathaviṃ dhārentīti gandhārā, kittigandhena arantīti vā gandhārā. '
  target_quote: '持有行走的大地，为gandhāra，

    或因声名流芳而到达，为gandhāra。'
- unit_id: 9-593-168-194
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-593-168-194
  line: 13
  source_quote: 'Takka ūhe, ūho ūnapūraṇaṃ, takkanaṃ takko, so sīlaṃ sabhāvo yattha
    sā takkasīlā, yo hi purisakārena ūno, so tattha gantvā tamūnaṃ pūretīti. '
  target_quote: 'takka思考的意思，思考即补充不足，

    思考补充不足的动作即takka，

    在思惯这个城市有思考的习惯，'
- unit_id: 9-594-38-54
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-594-38-54
  line: 14
  source_quote: 'Indaṃ paramissariyabhāvaṃ pāpuṇanti etthāti indapattaṃ, indo vā sakko
    devarājā, so patto etthāti indapattaṃ. '
  target_quote: '获得支配他人的权利之地，为帝·印达，

    天帝即萨卡天帝天帝到来的地方，为帝·印达。'
- unit_id: 14-1934-2-14
  unit_key: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:14-1934-2-14
  line: 19
  source_quote: 'Samaṇassa cīvaraṃ dadāti, samaṇassa rocate saccaṃ, devadattassa suvaṇṇacchattaṃ
    dhārayate yaññadatto. '
  target_quote: '把衣给到沙门；

    对沙门来说，现实是值得高兴的；

    yaññadatta为天赐撑起黄金的伞盖。'
evidence_ids:
- ev-001487
- ev-001488
- ev-001489
- ev-001490
- ev-001491
- ev-001492
- ev-001493
- ev-001494
- ev-001495
- ev-001496
- ev-001497
- ev-001498
- ev-001499
- ev-001500
- ev-001501
- ev-001502
- ev-001503
- ev-001504
- ev-001505
- ev-001506
- ev-001507
- ev-001508
- ev-001509
- ev-001510
- ev-001511
- ev-001512
- ev-001513
- ev-001514
- ev-001515
- ev-001516
- ev-001517
- ev-001518
- ev-001519
- ev-001520
- ev-001521
- ev-001522
- ev-001523
- ev-001524
- ev-001525
- ev-001526
- ev-001527
- ev-001528
- ev-001529
- ev-001530
- ev-001531
- ev-001532
- ev-001533
- ev-001534
- ev-001535
- ev-001536
- ev-001537
- ev-001538
- ev-001539
- ev-001540
- ev-001541
- ev-001542
- ev-001543
- ev-001544
- ev-001545
- ev-001546
- ev-001547
- ev-001548
- ev-001549
- ev-001550
- ev-001551
- ev-001552
- ev-001553
- ev-001554
- ev-001555
- ev-001556
- ev-001557
- ev-001558
- ev-001559
- ev-001560
- ev-001561
- ev-001562
- ev-001563
- ev-001564
- ev-001565
- ev-001566
- ev-001567
- ev-001568
- ev-001569
- ev-001570
- ev-001571
- ev-001572
- ev-001573
- ev-001574
- ev-001575
- ev-001576
- ev-001577
- ev-001578
- ev-001579
- ev-001580
- ev-001581
- ev-001582
- ev-001583
- ev-001584
- ev-001585
- ev-001586
- ev-001587
- ev-001588
- ev-001589
- ev-001590
- ev-001591
- ev-001592
- ev-001593
- ev-001594
- ev-001595
- ev-001596
- ev-001597
- ev-001598
- ev-001599
- ev-001600
- ev-001601
- ev-001602
- ev-001603
- ev-001604
- ev-001605
- ev-001606
- ev-001607
- ev-001608
- ev-001609
- ev-001610
- ev-001611
- ev-001612
- ev-001613
- ev-001614
- ev-001615
- ev-001616
- ev-001617
- ev-001618
- ev-001619
- ev-001620
- ev-001621
- ev-001622
- ev-001623
- ev-001624
- ev-001625
- ev-001626
- ev-001627
- ev-001628
- ev-001629
- ev-001630
- ev-001631
- ev-001632
- ev-001633
- ev-001634
- ev-001635
- ev-001636
- ev-001637
- ev-001638
- ev-001639
- ev-001640
- ev-001641
- ev-001642
- ev-001643
- ev-001644
- ev-001645
- ev-001646
- ev-001647
- ev-001648
- ev-001649
- ev-001650
- ev-001651
- ev-001652
- ev-001653
- ev-001654
- ev-001655
- ev-001656
- ev-001657
- ev-001658
- ev-001659
- ev-001660
- ev-001661
- ev-001662
- ev-001663
- ev-001664
- ev-001665
- ev-001666
- ev-001667
- ev-001668
- ev-001669
- ev-001670
- ev-001671
- ev-001672
- ev-001673
- ev-001674
- ev-001675
- ev-001676
- ev-001677
- ev-001678
- ev-001679
- ev-001680
- ev-001681
- ev-001682
- ev-001683
- ev-001684
- ev-001685
- ev-001686
- ev-001687
- ev-001688
- ev-001689
- ev-001690
- ev-001691
- ev-001692
- ev-001693
- ev-001694
- ev-001695
- ev-001696
- ev-001697
- ev-001698
- ev-001699
- ev-001700
- ev-001701
- ev-001702
- ev-001703
- ev-001704
- ev-001705
- ev-001706
- ev-001707
- ev-001708
- ev-001709
- ev-001710
- ev-001711
- ev-001712
- ev-001713
- ev-001714
- ev-001715
- ev-001716
- ev-001717
- ev-001718
- ev-001719
- ev-001720
- ev-001721
- ev-001722
- ev-001723
- ev-001724
- ev-001725
- ev-001726
- ev-001727
- ev-001728
- ev-001729
- ev-001730
- ev-001731
- ev-001732
- ev-001733
- ev-001734
- ev-001735
- ev-001736
- ev-001737
- ev-001738
- ev-001739
- ev-001740
- ev-001741
- ev-001742
- ev-001743
- ev-001744
- ev-001745
- ev-001746
- ev-001747
- ev-001748
- ev-001749
- ev-001750
- ev-001751
- ev-001752
- ev-001753
- ev-001754
- ev-001755
- ev-001756
- ev-001757
- ev-001758
- ev-001759
- ev-001760
- ev-001761
- ev-001762
- ev-001763
- ev-001764
- ev-001765
- ev-001766
- ev-001767
- ev-001768
- ev-001769
- ev-001770
- ev-001771
- ev-001772
- ev-001773
- ev-001774
- ev-001775
- ev-001776
- ev-001777
- ev-001778
- ev-001779
- ev-001780
- ev-001781
- ev-001782
- ev-001783
- ev-001784
- ev-001785
- ev-001786
- ev-001787
- ev-001788
- ev-001789
- ev-001790
- ev-001791
- ev-001792
- ev-001793
- ev-001794
- ev-001795
- ev-001796
- ev-001797
- ev-001798
- ev-001799
- ev-001800
- ev-001801
- ev-001802
- ev-001803
- ev-001804
- ev-001805
- ev-001806
- ev-001807
- ev-001808
- ev-001809
- ev-001810
- ev-001811
- ev-001812
- ev-001813
- ev-001814
- ev-001815
- ev-001816
- ev-001817
- ev-001818
- ev-001819
- ev-001820
- ev-001821
- ev-001822
- ev-001823
- ev-001824
- ev-001825
- ev-001826
- ev-001827
- ev-001828
- ev-001829
- ev-001830
- ev-001831
- ev-001832
- ev-001833
- ev-001834
- ev-001835
- ev-001836
- ev-001837
- ev-001838
- ev-001839
- ev-001840
- ev-001841
- ev-001842
- ev-001843
- ev-001844
- ev-001845
- ev-001846
- ev-001847
- ev-001848
- ev-001849
- ev-001850
- ev-001851
- ev-001852
- ev-001853
- ev-001854
- ev-001855
- ev-001856
- ev-001857
- ev-001858
- ev-001859
- ev-001860
- ev-001861
- ev-001862
- ev-001863
- ev-001864
- ev-001865
- ev-001866
- ev-001867
- ev-001868
- ev-001869
- ev-001870
- ev-001871
- ev-001872
- ev-001873
- ev-001874
- ev-001875
- ev-001876
confidence: 0.75
review_status: machine_generated
```
