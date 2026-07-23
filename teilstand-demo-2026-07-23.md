# Teilstand-Linsen-Lese-Demo — Ornith-1.0-9B (2026-07-23 03:42)

Checkpoint `ornith-ckpt.pt`: 10/300 Fit-Prompts abgeschlossen (next_idx=10), 31 Quell-Layer (0..30), Ziel-Layer L31.

**Holdout-Beleg**: Prompt-Liste 1:1 identisch zu `nacht_ornith.py` reproduziert (`Salesforce/wikitext`, `wikitext-103-raw-v1`, split `train`, `streaming=True`, Filter `len(text)>400 and not text.startswith('=')`, erste 300 Treffer, `t[:1200]`). HF-Streaming ohne `.shuffle()` liefert deterministisch dieselbe Reihenfolge wie im Nachtlauf. Checkpoint-`next_idx`=10 → der Fit hat ausschließlich `prompts[0:10]` gesehen. Gewählte Holdout-Indizes: [10, 50, 150] — alle ≥ next_idx, also disjunkt vom Fit-Set.

## Holdout-Prompt 10 (5s, seq_len=128)
> The majority of material created for previous games , such as the BLiTZ system and the design of maps , was carried over . Alongside this , improvements were made to the game 's graphics and some elem...

- Position 16 (Token `' and'`):
  - L0: ['шё', 'щё', 'ёр', ' kĩ', 'ё']
  - L5: ['折不', ' kĩ', '孢', '淀', '臻']
  - L10: ['Project', ' Operations', ' Blueprint', ' Project', ' programming']
  - L15: [' Fusion', ' Project', ' Legacy', ' Tech', ' redesign']
  - L20: [' scripts', ' Cyber', ' Project', ' concepts', ' Legacy']
  - L25: [' various', ' Weapon', ' characters', ' Story', ' Blueprint']
  - L30: [' the', ' various', ' other', ' its', ' Bl']
  - L31: [' the', ' its', ' other', ' various', ' many']
- Position 64 (Token `' of'`):
  - L0: ['шё', '职业能力', ' kĩ', 'щё', 't']
  - L5: [' Japan', ' mainly', ' equipments', ' Sakura', ' parts']
  - L10: [' functionalities', ' parts', ' Parts', ' part', ' equipments']
  - L15: [' parts', ' part', ' mentioned', ' Parts', ' contribution']
  - L20: [' this', ' gameplay', 'this', ' development', ' developers']
  - L25: [' Material', ' this', ' gameplay', ' these', ' material']
  - L30: [' the', ' this', ' Bl', ' these', ' BL']
  - L31: [' the', ' this', ' these', ' each', ' what']
- Position 126 (Token `' new'`):
  - L0: ['шё', 'ёр', 'лё', 'щё', 'ём']
  - L5: ['新工艺', '新家', ' new', ' NEW', '出新']
  - L10: ['新的', ' NEW', '新', '的新', 'NEW']
  - L15: [' newcomers', ' new', 'new', ' NEW', '新的']
  - L20: [' newcomers', ' new', ' newcomer', 'new', ' NEW']
  - L25: [' audiences', ' players', ' gamers', ' audience', 'players']
  - L30: [' players', ' audiences', ' gamers', ' users', ' fans']
  - L31: [' players', ' and', ' audiences', ' gamers', ' fans']

## Holdout-Prompt 50 (2s, seq_len=107)
> Fairies became a popular theme in art and literature in the early 20th century following the releases of The Coming of the Fairies by Sir Arthur Conan Doyle , Peter Pan by J.M. Barrie , and the fairy ...

- Position 16 (Token `'th'`):
  - L0: ['шё', 'ё', 'ёр', 'щё', 't']
  - L5: [' USSR', ' Weltkrieg', '民初', 'Colour', 'colour']
  - L10: ['British', '英国', 'Modern', '德国', 'Film']
  - L15: [' feminist', 'Modern', ' century', ' feminism', ' film']
  - L20: [' century', ' Century', 'British', 'Modern', ' centuries']
  - L25: [' century', ' Century', 'Century', '世纪', ' centuries']
  - L30: [' century', ' Century', 'cent', ' centuries', 'C']
  - L31: [' century', ' Century', ' and', ' centuries', 'C']
- Position 53 (Token `' Ida'`):
  - L0: ['щё', 'шё', 'жё', ' şi', ' neighbouring']
  - L5: ['丶', ' Ida', 'ţ', 'жё', 'avour']
  - L10: ['她', ' Ida', '女士', ' feminist', ' Irma']
  - L15: [' Ida', '她', ' feminist', ' granddaughter', '女士']
  - L20: [' Ida', ' Murdoch', '女士', ' Irma', '懿']
  - L25: [' Ida', ' Bagus', ' setId', 'IDA', ' ida']
  - L30: [' Rent', ' Tar', ' Bagus', ' Pfe', ' Pear']
  - L31: [' M', ' Darling', ' Rent', ' F', ' Pear']
- Position 105 (Token `'ies'`):
  - L0: ['шё', '帐', ' Ещё', ' honour', 'чёт']
  - L5: [' fairy', ' magic', ' Fairy', ' Magic', ' magical']
  - L10: [' fairy', ' Fairy', ' magic', ' magical', ' goddess']
  - L15: [' fairy', ' magic', ' fantasy', ' magical', ' Fairy']
  - L20: [' which', ' depicting', ' inspired', ' depicted', ' alongside']
  - L25: [' based', ' illustrating', ' inspired', ' working', ' illustrated']
  - L30: [' based', ' for', ' from', ' in', ' that']
  - L31: [' in', ' for', ' that', ' from', ' and']

## Holdout-Prompt 150 (2s, seq_len=89)
> On one day during his treatments , as his wife was wheeling him down a hospital corridor , Cullen went into cardiac arrest , requiring doctors to use a defibrillator to revive him . He underwent a bon...

- Position 16 (Token `' hospital'`):
  - L0: ['isation', 'ised', 'isations', 'шё', 'atisation']
  - L5: [' hospitals', ' hospital', ' Hospital', ' Hospitals', 'isations']
  - L10: [' hospital', ' Hospital', '医院', ' hospitals', 'Medical']
  - L15: [' hospital', ' hospitals', '医院', ' Hospital', ' doctors']
  - L20: [' hospital', ' Hospital', '医院', ' ambulance', ' hospitals']
  - L25: [' corridor', ' hallway', ' corridors', '走廊', ' aisle']
  - L30: [' corridor', ' hallway', ' aisle', ' lane', ' ward']
  - L31: [' corridor', ' hallway', ' ward', ' aisle', ' hall']
- Position 44 (Token `' that'`):
  - L0: ['шё', 'leş', '职业能力', 'ération', 'щё']
  - L5: [' canceled', 'ără', ' afterward', ' quizá', 'șa']
  - L10: ['医学', 'Medical', ' medically', '手术', '修复']
  - L15: [' hospital', ' healed', ' medical', ' afterward', ' healing']
  - L20: [' lasted', ' eventually', ' successfully', ' survived', ' later']
  - L25: [' year', ' month', '恢复了', '恢复', ' restored']
  - L30: [' year', ' restored', ' cured', ' saved', ' healed']
  - L31: [' year', ' same', ' was', ' saved', ' summer']
- Position 87 (Token `' comeback'`):
  - L0: ['铡', ' towards', ' endeavour', ' aka', ' succesfully']
  - L5: [' comeback', ' kids', ' hubby', ' newbie', ' goodies']
  - L10: [' comeback', ' rehab', '重返', '复出', ' makeover']
  - L15: [' comeback', ' movie', ' revived', ' resurgence', ' revive']
  - L20: [' comeback', '复出', '重返', ' return', 'Return']
  - L25: [' comeback', ' return', ' tour', '返回', 'Return']
  - L30: [' attempt', ' tour', ' comeback', ' fight', ' return']
  - L31: [' in', ' to', ' on', ' with', ' tour']

