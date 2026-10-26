# libGameCore.so current-version ARM64 coordinate/obfuscation functions

Sections: .text 43753884 bytes, .rodata 2481708 bytes, FDE 342568.
Capstone decoded instructions: 10938471. Matched string XREF: 484.

## Verified string references
- {"pc": "0x23fa32c", "adrp": "0x23fa328", "target": "0x11a5472", "label": "VInt3", "keywords": ["VInt3"], "fde_start": "0x23fa324", "fde_end": "0x23fa338", "kind": "add", "reg": "x0"}
- {"pc": "0x23fae1c", "adrp": "0x23fae14", "target": "0x11a5472", "label": "VInt3", "keywords": ["VInt3"], "fde_start": "0x23fae04", "fde_end": "0x23fae3c", "kind": "add", "reg": "x3"}
- {"pc": "0x24acbfc", "adrp": "0x24acbf4", "target": "0x11d8792", "label": "invisible_range", "keywords": ["invisible"], "fde_start": "0x24aca80", "fde_end": "0x24acf54", "kind": "add", "reg": "x9"}
- {"pc": "0x24acc90", "adrp": "0x24acc84", "target": "0x116570b", "label": "[Init] m_invisible_range:%d", "keywords": ["invisible"], "fde_start": "0x24aca80", "fde_end": "0x24acf54", "kind": "add", "reg": "x2"}
- {"pc": "0x24ad994", "adrp": "0x24ad988", "target": "0x117f1d6", "label": "view_manager::ViewManager::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x24ad7fc", "fde_end": "0x24ade74", "kind": "add", "reg": "x1"}
- {"pc": "0x24ad99c", "adrp": "0x24ad98c", "target": "0x114b500", "label": "hero:%d loc:(%d, %d) invisible2visible change to 55000", "keywords": ["invisible"], "fde_start": "0x24ad7fc", "fde_end": "0x24ade74", "kind": "add", "reg": "x2"}
- {"pc": "0x24ada78", "adrp": "0x24ada68", "target": "0x117f1d6", "label": "view_manager::ViewManager::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x24ad7fc", "fde_end": "0x24ade74", "kind": "add", "reg": "x1"}
- {"pc": "0x24ae028", "adrp": "0x24ae018", "target": "0x1192575", "label": "view_manager::ViewManager::ModifyEnemyInvisibleHeroPositionByTimeDynamic", "keywords": ["ModifyEnemyInvisibleHeroPositionByTimeDynamic", "ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x24ade74", "fde_end": "0x24ae674", "kind": "add", "reg": "x1"}
- {"pc": "0x24ae2f8", "adrp": "0x24ae2ec", "target": "0x1192575", "label": "view_manager::ViewManager::ModifyEnemyInvisibleHeroPositionByTimeDynamic", "keywords": ["ModifyEnemyInvisibleHeroPositionByTimeDynamic", "ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x24ade74", "fde_end": "0x24ae674", "kind": "add", "reg": "x1"}
- {"pc": "0x24ae420", "adrp": "0x24ae410", "target": "0x1192575", "label": "view_manager::ViewManager::ModifyEnemyInvisibleHeroPositionByTimeDynamic", "keywords": ["ModifyEnemyInvisibleHeroPositionByTimeDynamic", "ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x24ade74", "fde_end": "0x24ae674", "kind": "add", "reg": "x1"}
- {"pc": "0x24ae430", "adrp": "0x24ae418", "target": "0x11d87a2", "label": "frame:%d main_hero:%d hero:%d, not visible duration(sec) = %d, dist = %d, last_dist = %d, enemy true location = (%d, %d), main_hero_location = (%d, %d), invisible_range:%d", "keywords": ["invisible"], "fde_start": "0x24ade74", "fde_end": "0x24ae674", "kind": "add", "reg": "x2"}
- {"pc": "0x24ae56c", "adrp": "0x24ae55c", "target": "0x1192575", "label": "view_manager::ViewManager::ModifyEnemyInvisibleHeroPositionByTimeDynamic", "keywords": ["ModifyEnemyInvisibleHeroPositionByTimeDynamic", "ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x24ade74", "fde_end": "0x24ae674", "kind": "add", "reg": "x1"}
- {"pc": "0x24ae574", "adrp": "0x24ae560", "target": "0x1185459", "label": "frame:%d camp:%d, main_hero:%d, modify emy_hero:%d to spring, frame_diff:%d, last_visible_dist:%d, dist:%d, invisible_range:%d", "keywords": ["invisible"], "fde_start": "0x24ade74", "fde_end": "0x24ae674", "kind": "add", "reg": "x2"}
- {"pc": "0x24aea90", "adrp": "0x24aea84", "target": "0x11ac0c5", "label": "mian_hero [%d-%d-%d] tgt_hero [%d-%d-%d] cur_frame %d, last_invisible_ingrass %d --> visible_ingrass less than 6 frame", "keywords": ["invisible"], "fde_start": "0x24ae864", "fde_end": "0x24aeac0", "kind": "add", "reg": "x2"}
- {"pc": "0x24aedbc", "adrp": "0x24aedac", "target": "0x11b25de", "label": "ake use skill3, invisible, real_location = (%d,%d), modify to (%d,%d)", "keywords": ["real_location", "invisible"], "fde_start": "0x24aed38", "fde_end": "0x24aee60", "kind": "add", "reg": "x2"}
- {"pc": "0x24aef08", "adrp": "0x24aeef8", "target": "0x11925be", "label": "yindao, cid:%d, invisible, real_location = (%d,%d), modify to (%d,%d)", "keywords": ["real_location", "invisible"], "fde_start": "0x24aee60", "fde_end": "0x24aefb8", "kind": "add", "reg": "x2"}
- {"pc": "0x24af05c", "adrp": "0x24af058", "target": "0x11d1b38", "label": "view_manager::ViewManager::ModifyHeroPositionWhenNearby", "keywords": ["HeroPosition"], "fde_start": "0x24aefb8", "fde_end": "0x24af0f8", "kind": "add", "reg": "x21"}
- {"pc": "0x2555a54", "adrp": "0x2555a4c", "target": "0x11ec6c2", "label": "use_invisible_to_visible_delay_rule", "keywords": ["invisible"], "fde_start": "0x25543d0", "fde_end": "0x2556400", "kind": "add", "reg": "x10"}
- {"pc": "0x2555b64", "adrp": "0x2555b5c", "target": "0x11b8e93", "label": "invisible_to_visible_delay", "keywords": ["invisible"], "fde_start": "0x25543d0", "fde_end": "0x2556400", "kind": "add", "reg": "x9"}
- {"pc": "0x2555be0", "adrp": "0x2555bd8", "target": "0x119ed3d", "label": "invisible_to_visible_delta", "keywords": ["invisible"], "fde_start": "0x25543d0", "fde_end": "0x2556400", "kind": "add", "reg": "x8"}
- {"pc": "0x255686c", "adrp": "0x2556864", "target": "0x11f3691", "label": "m_enable_invisible_visible_rule right hand case 2", "keywords": ["invisible"], "fde_start": "0x2556400", "fde_end": "0x25572c8", "kind": "add", "reg": "x2"}
- {"pc": "0x25568ac", "adrp": "0x25568a4", "target": "0x114bcfd", "label": "invisible_visible_rule_case2", "keywords": ["invisible"], "fde_start": "0x2556400", "fde_end": "0x25572c8", "kind": "add", "reg": "x1"}
- {"pc": "0x25568f8", "adrp": "0x25568f0", "target": "0x11def93", "label": "m_enable_invisible_visible_rule right hand", "keywords": ["invisible"], "fde_start": "0x2556400", "fde_end": "0x25572c8", "kind": "add", "reg": "x2"}
- {"pc": "0x2556938", "adrp": "0x2556930", "target": "0x11d1fed", "label": "invisible_visible_rule_case1", "keywords": ["invisible"], "fde_start": "0x2556400", "fde_end": "0x25572c8", "kind": "add", "reg": "x1"}
- {"pc": "0x255b17c", "adrp": "0x255b174", "target": "0x11bef92", "label": " check visible frame_no: %d hero %d m_invisible_to_visible_frame %d m_previous_visible_num %d min_visilble_dist %d friend_num %d near_friend_num %d is_friend_front %d is_enemy_invisible_5s %d exist_filter_hero %d ", "keywords": ["invisible", "invisible"], "fde_start": "0x255a948", "fde_end": "0x255b448", "kind": "add", "reg": "x2"}
- {"pc": "0x255b220", "adrp": "0x255b218", "target": "0x11d2080", "label": " invisible_to_visible_tag sesion start frame_no: %d hero %d m_invisible_to_visible_frame %d cur_invisible_skill_delay %d diff %d", "keywords": ["invisible", "invisible", "invisible"], "fde_start": "0x255a948", "fde_end": "0x255b448", "kind": "add", "reg": "x2"}
- {"pc": "0x255b2b4", "adrp": "0x255b2ac", "target": "0x117f55c", "label": "sesion end frame_no: %d hero %d m_invisible_to_visible_frame %d cur_invisible_skill_delay %d diff %d", "keywords": ["invisible", "invisible"], "fde_start": "0x255a948", "fde_end": "0x255b448", "kind": "add", "reg": "x2"}
- {"pc": "0x255b3b4", "adrp": "0x255b3ac", "target": "0x117912c", "label": "sesion end frame_no: %d hero %d m_invisible_to_visible_frame %d cur_invisible_skill_delay %d diff %d skill_type:%d", "keywords": ["invisible", "invisible"], "fde_start": "0x255a948", "fde_end": "0x255b448", "kind": "add", "reg": "x2"}
- {"pc": "0x259bc10", "adrp": "0x259bbfc", "target": "0x11cb768", "label": "Foundation/Common/include/Type/VInt3.inl", "keywords": ["VInt3"], "fde_start": "0x259bbbc", "fde_end": "0x25a15d4", "kind": "add", "reg": "x0"}
- {"pc": "0x25a62cc", "adrp": "0x25a62c4", "target": "0x11a5472", "label": "VInt3", "keywords": ["VInt3"], "fde_start": "0x25a6288", "fde_end": "0x25a6408", "kind": "add", "reg": "x1"}
- {"pc": "0x25d2fa0", "adrp": "0x25d2f9c", "target": "0x11a5472", "label": "VInt3", "keywords": ["VInt3"], "fde_start": "0x25d2f9c", "fde_end": "0x25d2fa8", "kind": "add", "reg": "x0"}
- {"pc": "0x26719c0", "adrp": "0x26719a0", "target": "0x12070a1", "label": "frame %d, mainCid %d, mainRid %d, camp %d, valid %d, visibleEnemyCnt %d, invisibleEnemyCnt %d, useVisibleRule %d, visibleFloor %d, visibleCeil %d, useInvisibleRule %d, invisibleFloor %d, invisibleCeil %d", "keywords": ["invisible", "invisible", "invisible"], "fde_start": "0x267180c", "fde_end": "0x2671a0c", "kind": "add", "reg": "x2"}
- {"pc": "0x26934c0", "adrp": "0x26934a0", "target": "0x12070a1", "label": "frame %d, mainCid %d, mainRid %d, camp %d, valid %d, visibleEnemyCnt %d, invisibleEnemyCnt %d, useVisibleRule %d, visibleFloor %d, visibleCeil %d, useInvisibleRule %d, invisibleFloor %d, invisibleCeil %d", "keywords": ["invisible", "invisible", "invisible"], "fde_start": "0x269330c", "fde_end": "0x269350c", "kind": "add", "reg": "x2"}
- {"pc": "0x269e170", "adrp": "0x269e154", "target": "0x11dfac7", "label": "frame:%d rid=%d SKIP unit_invisible_time: friendly hero, range=[%d,%d]", "keywords": ["invisible"], "fde_start": "0x269dac8", "fde_end": "0x269ea98", "kind": "add", "reg": "x2"}
- {"pc": "0x269e8dc", "adrp": "0x269e8c8", "target": "0x11795b8", "label": "frame:%d rid=%d SKIP unit_invisible_time: not seen yet since enqueue", "keywords": ["invisible"], "fde_start": "0x269dac8", "fde_end": "0x269ea98", "kind": "add", "reg": "x2"}
- {"pc": "0x269e940", "adrp": "0x269e924", "target": "0x11dfb0e", "label": "frame:%d rid=%d SKIP unit_invisible_time: val=%d range=[%d,%d]", "keywords": ["invisible"], "fde_start": "0x269dac8", "fde_end": "0x269ea98", "kind": "add", "reg": "x2"}
- {"pc": "0x269febc", "adrp": "0x269feb4", "target": "0x11c5cda", "label": "hero_state.invisible_enemy_cnt_floor", "keywords": ["invisible"], "fde_start": "0x269efdc", "fde_end": "0x26a5db8", "kind": "add", "reg": "x1"}
- {"pc": "0x269ff70", "adrp": "0x269ff68", "target": "0x1192f25", "label": "hero_state.invisible_enemy_cnt_ceil", "keywords": ["invisible"], "fde_start": "0x269efdc", "fde_end": "0x26a5db8", "kind": "add", "reg": "x1"}
- {"pc": "0x26cdc70", "adrp": "0x26cdc68", "target": "0x11d8792", "label": "invisible_range", "keywords": ["invisible"], "fde_start": "0x26cb1a8", "fde_end": "0x26cf18c", "kind": "add", "reg": "x1"}
- {"pc": "0x26cdcac", "adrp": "0x26cdca4", "target": "0x11d8792", "label": "invisible_range", "keywords": ["invisible"], "fde_start": "0x26cb1a8", "fde_end": "0x26cf18c", "kind": "add", "reg": "x1"}
- {"pc": "0x26d55d0", "adrp": "0x26d55c0", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x1"}
- {"pc": "0x26d5ac0", "adrp": "0x26d5ab4", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x1"}
- {"pc": "0x26d5ac4", "adrp": "0x26d5ab8", "target": "0x11ac0c5", "label": "mian_hero [%d-%d-%d] tgt_hero [%d-%d-%d] cur_frame %d, last_invisible_ingrass %d --> visible_ingrass less than 6 frame", "keywords": ["invisible"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x2"}
- {"pc": "0x26d5b34", "adrp": "0x26d5b2c", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x1"}
- {"pc": "0x26d5b38", "adrp": "0x26d5b30", "target": "0x118d061", "label": "hero:%d invisible2visible", "keywords": ["invisible"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x2"}
- {"pc": "0x26d5c1c", "adrp": "0x26d5c0c", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x1"}
- {"pc": "0x26d5c24", "adrp": "0x26d5c14", "target": "0x116c7eb", "label": "lanlingwang use skill3, invisible, real_location = (%d,%d), main_hero_location = (%d, %d)", "keywords": ["real_location", "invisible"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x2"}
- {"pc": "0x26d5e04", "adrp": "0x26d5df8", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x1"}
- {"pc": "0x26d5e0c", "adrp": "0x26d5dfc", "target": "0x11b25de", "label": "ake use skill3, invisible, real_location = (%d,%d), modify to (%d,%d)", "keywords": ["real_location", "invisible"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x2"}
- {"pc": "0x26d5e60", "adrp": "0x26d5e58", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x1"}
- {"pc": "0x26d5e80", "adrp": "0x26d5e7c", "target": "0x11dfda4", "label": "lanlingwang use skill3, invisible and far to main hero, real location = (%d, %d), modified location = (50000, 50000), main_hero_location = (%d, %d)", "keywords": ["invisible"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x2"}
- {"pc": "0x26d5f20", "adrp": "0x26d5f18", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x23"}
- {"pc": "0x26d5f38", "adrp": "0x26d5f24", "target": "0x119f627", "label": "ake use skill3, invisible and dist to main hero < 100, real location = (%d, %d), main_hero_location = (%d, %d)", "keywords": ["invisible"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x2"}
- {"pc": "0x26d5f94", "adrp": "0x26d5f80", "target": "0x119f696", "label": "ake use skill3, invisible and dist to main hero < 100, modified_location = (%d, %d), main_hero_location = (%d, %d)", "keywords": ["invisible"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x2"}
- {"pc": "0x26d6014", "adrp": "0x26d6004", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x1"}
- {"pc": "0x26d601c", "adrp": "0x26d6008", "target": "0x119901c", "label": "lanlingwang use skill3, invisible, modified location = (%d,%d), main_hero_location = (%d, %d)", "keywords": ["invisible"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x2"}
- {"pc": "0x26d6030", "adrp": "0x26d602c", "target": "0x11b33ca", "label": "lanlingwang use skill3, invisible and far to main hero, real location = (%d, %d), modified location = (-50000, -50000), main_hero_location = (%d, %d)", "keywords": ["invisible"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x2"}
- {"pc": "0x26d6054", "adrp": "0x26d604c", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x1"}
- {"pc": "0x26d6074", "adrp": "0x26d6070", "target": "0x118d07b", "label": "ake use skill3, invisible and dist to main hero > 100, real location = (%d, %d), modified_location = (50000,0,50000), main_hero_location = (%d, %d)", "keywords": ["invisible"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x2"}
- {"pc": "0x26d6098", "adrp": "0x26d6094", "target": "0x11d2925", "label": "ake use skill3, invisible and dist to main hero > 100, real location = (%d, %d), modified_location = (-50000,0,-50000), main_hero_location = (%d, %d)", "keywords": ["invisible"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x2"}
- {"pc": "0x26d6148", "adrp": "0x26d613c", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x1"}
- {"pc": "0x26d6150", "adrp": "0x26d6140", "target": "0x114c547", "label": "hero:%d loc:(%d, %d) invisible2visible delay:%d change to 50000", "keywords": ["invisible"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x2"}
- {"pc": "0x26d61c8", "adrp": "0x26d61c0", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x1"}
- {"pc": "0x26d62a4", "adrp": "0x26d62a0", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x22"}
- {"pc": "0x26d6348", "adrp": "0x26d633c", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x1"}
- {"pc": "0x26d65a4", "adrp": "0x26d6594", "target": "0x11c5f0b", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPositionByTimeDynamic", "keywords": ["ModifyEnemyInvisibleHeroPositionByTimeDynamic", "ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d63cc", "fde_end": "0x26d6b48", "kind": "add", "reg": "x1"}
- {"pc": "0x26d6a00", "adrp": "0x26d69f0", "target": "0x11c5f0b", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPositionByTimeDynamic", "keywords": ["ModifyEnemyInvisibleHeroPositionByTimeDynamic", "ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d63cc", "fde_end": "0x26d6b48", "kind": "add", "reg": "x1"}
- {"pc": "0x26d6a08", "adrp": "0x26d69f8", "target": "0x11d87a2", "label": "frame:%d main_hero:%d hero:%d, not visible duration(sec) = %d, dist = %d, last_dist = %d, enemy true location = (%d, %d), main_hero_location = (%d, %d), invisible_range:%d", "keywords": ["invisible"], "fde_start": "0x26d63cc", "fde_end": "0x26d6b48", "kind": "add", "reg": "x2"}
- {"pc": "0x26d6ab0", "adrp": "0x26d6aa0", "target": "0x11c5f0b", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPositionByTimeDynamic", "keywords": ["ModifyEnemyInvisibleHeroPositionByTimeDynamic", "ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d63cc", "fde_end": "0x26d6b48", "kind": "add", "reg": "x1"}
- {"pc": "0x26d6ab8", "adrp": "0x26d6aa4", "target": "0x1185459", "label": "frame:%d camp:%d, main_hero:%d, modify emy_hero:%d to spring, frame_diff:%d, last_visible_dist:%d, dist:%d, invisible_range:%d", "keywords": ["invisible"], "fde_start": "0x26d63cc", "fde_end": "0x26d6b48", "kind": "add", "reg": "x2"}
- {"pc": "0x26d6b14", "adrp": "0x26d6b08", "target": "0x11c5f0b", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPositionByTimeDynamic", "keywords": ["ModifyEnemyInvisibleHeroPositionByTimeDynamic", "ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d63cc", "fde_end": "0x26d6b48", "kind": "add", "reg": "x1"}
- {"pc": "0x2770044", "adrp": "0x277003c", "target": "0x1145b4b", "label": "_invisible_visible_rule_case1", "keywords": ["invisible"], "fde_start": "0x276df9c", "fde_end": "0x27702e0", "kind": "add", "reg": "x1"}
- {"pc": "0x277010c", "adrp": "0x2770104", "target": "0x1152f26", "label": "_invisible_visible_rule_case2", "keywords": ["invisible"], "fde_start": "0x276df9c", "fde_end": "0x27702e0", "kind": "add", "reg": "x1"}
- {"pc": "0x27a98d0", "adrp": "0x27a98c0", "target": "0x11a6f31", "label": "last_enemy_visible_frame %d last_enemy_invisible_frame %d", "keywords": ["invisible"], "fde_start": "0x27a9820", "fde_end": "0x27a9d7c", "kind": "add", "reg": "x2"}
- {"pc": "0x27c31dc", "adrp": "0x27c31d4", "target": "0x11d1fed", "label": "invisible_visible_rule_case1", "keywords": ["invisible"], "fde_start": "0x27c003c", "fde_end": "0x27cee04", "kind": "add", "reg": "x8"}
- {"pc": "0x27c501c", "adrp": "0x27c5014", "target": "0x1173977", "label": "kUseMoveDirRandom", "keywords": ["MoveDir"], "fde_start": "0x27c003c", "fde_end": "0x27cee04", "kind": "add", "reg": "x9"}
- {"pc": "0x27e5a48", "adrp": "0x27e5a40", "target": "0x1207f17", "label": "target_monster_hp_rate is less than STAY_WITH_MONSTER_HP threshold. Change MoveDir to NormAtk", "keywords": ["MoveDir"], "fde_start": "0x27e5438", "fde_end": "0x27e5ed8", "kind": "add", "reg": "x2"}
- {"pc": "0x27e5bf0", "adrp": "0x27e5be8", "target": "0x11fb2c5", "label": "more restrict Laye rule for bailixuance. Change MoveDir to MovePos", "keywords": ["MoveDir"], "fde_start": "0x27e5438", "fde_end": "0x27e5ed8", "kind": "add", "reg": "x2"}
- {"pc": "0x27fb474", "adrp": "0x27fb46c", "target": "0x11537ac", "label": "mask skill3 -> kMoveDir, hp_rate:%.2f", "keywords": ["MoveDir"], "fde_start": "0x27fac24", "fde_end": "0x27fbde0", "kind": "add", "reg": "x2"}
- {"pc": "0x2812d14", "adrp": "0x2812d0c", "target": "0x11c046c", "label": "CurFrame[%d] Enter Alert Because In HeroAlert, EnemyPos[%d;%d:%d:%d] MainHeroPos[%d;%d:%d:%d] MovePos[%d:%d:%d]\n", "keywords": ["EnemyPos", "MainHeroPos"], "fde_start": "0x2812960", "fde_end": "0x2812d6c", "kind": "add", "reg": "x2"}
- {"pc": "0x281315c", "adrp": "0x2813154", "target": "0x114d690", "label": "CurFrame[%d] Enter Danger Because In HeroDanger, EnemyPos[%d;%d:%d:%d] MainHeroPos[%d;%d:%d:%d] MovePos[%d:%d:%d]\n", "keywords": ["EnemyPos", "MainHeroPos"], "fde_start": "0x2812d6c", "fde_end": "0x28131b4", "kind": "add", "reg": "x2"}
- {"pc": "0x2827c74", "adrp": "0x2827c68", "target": "0x11872a5", "label": "Ignore, yAction:%d not kMoveDir", "keywords": ["MoveDir"], "fde_start": "0x2827bec", "fde_end": "0x2827d70", "kind": "add", "reg": "x2"}
- {"pc": "0x282cf8c", "adrp": "0x282cf84", "target": "0x12084ba", "label": "OptimizeMoveDir", "keywords": ["MoveDir"], "fde_start": "0x282cf0c", "fde_end": "0x282d018", "kind": "add", "reg": "x2"}
- {"pc": "0x282d1c0", "adrp": "0x282d1b8", "target": "0x114672f", "label": "GuanyuActionOpt::OptimizeMoveDir", "keywords": ["MoveDir"], "fde_start": "0x282d06c", "fde_end": "0x282d360", "kind": "add", "reg": "x1"}
- {"pc": "0x282d27c", "adrp": "0x282d274", "target": "0x114672f", "label": "GuanyuActionOpt::OptimizeMoveDir", "keywords": ["MoveDir"], "fde_start": "0x282d06c", "fde_end": "0x282d360", "kind": "add", "reg": "x1"}
- {"pc": "0x282d2dc", "adrp": "0x282d2d4", "target": "0x114672f", "label": "GuanyuActionOpt::OptimizeMoveDir", "keywords": ["MoveDir"], "fde_start": "0x282d06c", "fde_end": "0x282d360", "kind": "add", "reg": "x1"}
- {"pc": "0x282d304", "adrp": "0x282d2fc", "target": "0x114672f", "label": "GuanyuActionOpt::OptimizeMoveDir", "keywords": ["MoveDir"], "fde_start": "0x282d06c", "fde_end": "0x282d360", "kind": "add", "reg": "x1"}
- {"pc": "0x2832c34", "adrp": "0x2832c2c", "target": "0x117417f", "label": "no_shoot_invisible_frame_gap", "keywords": ["invisible"], "fde_start": "0x2832508", "fde_end": "0x2832f68", "kind": "add", "reg": "x1"}
- {"pc": "0x2835d38", "adrp": "0x2835d2c", "target": "0x114d8b7", "label": "frame=%d,monster_rid=%d,invisible,move_to_it", "keywords": ["invisible"], "fde_start": "0x2835a7c", "fde_end": "0x2835e20", "kind": "add", "reg": "x2"}
- {"pc": "0x28374f4", "adrp": "0x28374f0", "target": "0x114d91d", "label": "frame=%d,emy_hero=%d,cid=%d,hp=%d,dis_from_main=%d,invisible", "keywords": ["invisible"], "fde_start": "0x2837144", "fde_end": "0x2837710", "kind": "add", "reg": "x23"}
- {"pc": "0x285ea70", "adrp": "0x285ea68", "target": "0x11d8792", "label": "invisible_range", "keywords": ["invisible"], "fde_start": "0x285ac94", "fde_end": "0x2860024", "kind": "add", "reg": "x1"}
- {"pc": "0x285eaa8", "adrp": "0x285eaa0", "target": "0x11d8792", "label": "invisible_range", "keywords": ["invisible"], "fde_start": "0x285ac94", "fde_end": "0x2860024", "kind": "add", "reg": "x1"}
- {"pc": "0x28c9ba0", "adrp": "0x28c9b98", "target": "0x11e76f3", "label": "CreateMoveDirectionState", "keywords": ["MoveDir"], "fde_start": "0x28c9b6c", "fde_end": "0x28c9c08", "kind": "add", "reg": "x1"}
- {"pc": "0x28d1634", "adrp": "0x28d162c", "target": "0x114079c", "label": "SyncPositionMoveCmd", "keywords": ["SyncPosition"], "fde_start": "0x28d1600", "fde_end": "0x28d1690", "kind": "add", "reg": "x1"}
- {"pc": "0x29276c0", "adrp": "0x29276b8", "target": "0x1208aa0", "label": "MoveDirectionCmd", "keywords": ["MoveDir"], "fde_start": "0x292768c", "fde_end": "0x2927728", "kind": "add", "reg": "x1"}
- {"pc": "0x2932698", "adrp": "0x2932690", "target": "0x11f554b", "label": "Physics::MoveDirectionState", "keywords": ["MoveDir"], "fde_start": "0x2932664", "fde_end": "0x2932700", "kind": "add", "reg": "x1"}
- {"pc": "0x29e9e2c", "adrp": "0x29e9e28", "target": "0x1154147", "label": "AGE::SimpleMoveDirType", "keywords": ["MoveDir"], "fde_start": "0x29e9e0c", "fde_end": "0x29e9ef0", "kind": "add", "reg": "x1"}
- {"pc": "0x2a0e360", "adrp": "0x2a0e35c", "target": "0x119a5c3", "label": "CheckActorPositionCrossWall", "keywords": ["ActorPos"], "fde_start": "0x2a0df48", "fde_end": "0x2a0e478", "kind": "add", "reg": "x1"}
- {"pc": "0x2a2cb78", "adrp": "0x2a2cb70", "target": "0x11c0f57", "label": "invisible_range: ", "keywords": ["invisible"], "fde_start": "0x2a2c668", "fde_end": "0x2a2cbe8", "kind": "add", "reg": "x1"}
- {"pc": "0x2c46fc0", "adrp": "0x2c46fb8", "target": "0x11dadbe", "label": "USGActorRoot", "keywords": ["ActorRoot"], "fde_start": "0x2c46f8c", "fde_end": "0x2c47028", "kind": "add", "reg": "x1"}
- {"pc": "0x2cf5100", "adrp": "0x2cf50fc", "target": "0x11a11c8", "label": "TraverseVInt3Array", "keywords": ["VInt3"], "fde_start": "0x2cf4f00", "fde_end": "0x2cf5e10", "kind": "add", "reg": "x1"}
- {"pc": "0x2cf5550", "adrp": "0x2cf5548", "target": "0x11a5472", "label": "VInt3", "keywords": ["VInt3"], "fde_start": "0x2cf4f00", "fde_end": "0x2cf5e10", "kind": "add", "reg": "x1"}
- {"pc": "0x2cf55b4", "adrp": "0x2cf55ac", "target": "0x1187de3", "label": "VInt3Array", "keywords": ["VInt3"], "fde_start": "0x2cf4f00", "fde_end": "0x2cf5e10", "kind": "add", "reg": "x1"}
- {"pc": "0x2e71c50", "adrp": "0x2e71c48", "target": "0x11ae660", "label": "ActorPositionChangeEventNodeRuntime", "keywords": ["ActorPos"], "fde_start": "0x2e71c1c", "fde_end": "0x2e71cb8", "kind": "add", "reg": "x1"}
- {"pc": "0x2e83ba0", "adrp": "0x2e83b98", "target": "0x119a990", "label": "ActorPositionChangeListenerNodeRuntime", "keywords": ["ActorPos"], "fde_start": "0x2e83b6c", "fde_end": "0x2e83c08", "kind": "add", "reg": "x1"}
- {"pc": "0x2f39c48", "adrp": "0x2f39c40", "target": "0x11d4497", "label": "GlobalVariableActorRootNodeRuntime", "keywords": ["ActorRoot"], "fde_start": "0x2f39c14", "fde_end": "0x2f39cb0", "kind": "add", "reg": "x1"}
- {"pc": "0x2f3a984", "adrp": "0x2f3a97c", "target": "0x12028c3", "label": "VInt3ConstantMapNodeRuntime", "keywords": ["VInt3"], "fde_start": "0x2f3a950", "fde_end": "0x2f3a9ec", "kind": "add", "reg": "x1"}
- {"pc": "0x2f3adcc", "adrp": "0x2f3adc4", "target": "0x1161a0e", "label": "VInt3MapForeachLoopNodeRuntime", "keywords": ["VInt3"], "fde_start": "0x2f3ad98", "fde_end": "0x2f3ae34", "kind": "add", "reg": "x1"}
- {"pc": "0x2f3b03c", "adrp": "0x2f3b034", "target": "0x11815db", "label": "GlobalVariableVInt3MapNodeRuntime", "keywords": ["VInt3"], "fde_start": "0x2f3b008", "fde_end": "0x2f3b0a4", "kind": "add", "reg": "x1"}
- {"pc": "0x2f3b5a8", "adrp": "0x2f3b5a0", "target": "0x11ae791", "label": "VInt3MapNodeRuntime", "keywords": ["VInt3"], "fde_start": "0x2f3b574", "fde_end": "0x2f3b610", "kind": "add", "reg": "x1"}
- {"pc": "0x2f3c984", "adrp": "0x2f3c97c", "target": "0x11c74f3", "label": "ActorRootConstantMapNodeRuntime", "keywords": ["ActorRoot"], "fde_start": "0x2f3c950", "fde_end": "0x2f3c9ec", "kind": "add", "reg": "x1"}
- {"pc": "0x2f3cd0c", "adrp": "0x2f3cd04", "target": "0x11c7513", "label": "ActorRootMapForeachLoopNodeRuntime", "keywords": ["ActorRoot"], "fde_start": "0x2f3ccd8", "fde_end": "0x2f3cd74", "kind": "add", "reg": "x1"}
- {"pc": "0x2f3cf7c", "adrp": "0x2f3cf74", "target": "0x11fc1b3", "label": "GlobalVariableActorRootMapNodeRuntime", "keywords": ["ActorRoot"], "fde_start": "0x2f3cf48", "fde_end": "0x2f3cfe4", "kind": "add", "reg": "x1"}
- {"pc": "0x2f3d4e8", "adrp": "0x2f3d4e0", "target": "0x1187fca", "label": "ActorRootMapNodeRuntime", "keywords": ["ActorRoot"], "fde_start": "0x2f3d4b4", "fde_end": "0x2f3d550", "kind": "add", "reg": "x1"}
- {"pc": "0x2f3d8a8", "adrp": "0x2f3d8a0", "target": "0x1140f41", "label": "ConstantVInt3NodeRuntime", "keywords": ["VInt3"], "fde_start": "0x2f3d874", "fde_end": "0x2f3d910", "kind": "add", "reg": "x1"}
- {"pc": "0x2f3dba8", "adrp": "0x2f3dba0", "target": "0x12028df", "label": "GlobalVariableVInt3NodeRuntime", "keywords": ["VInt3"], "fde_start": "0x2f3db74", "fde_end": "0x2f3dc10", "kind": "add", "reg": "x1"}
- {"pc": "0x2f3e108", "adrp": "0x2f3e100", "target": "0x116e1ab", "label": "VariableVInt3NodeRuntime", "keywords": ["VInt3"], "fde_start": "0x2f3e0d4", "fde_end": "0x2f3e170", "kind": "add", "reg": "x1"}
- {"pc": "0x2f41588", "adrp": "0x2f41580", "target": "0x12028fe", "label": "VInt3ArrayForeachLoopNodeRuntime", "keywords": ["VInt3"], "fde_start": "0x2f41554", "fde_end": "0x2f415f0", "kind": "add", "reg": "x1"}
- {"pc": "0x2f417f8", "adrp": "0x2f417f0", "target": "0x11e181d", "label": "GlobalVariableVInt3ArrayNodeRuntime", "keywords": ["VInt3"], "fde_start": "0x2f417c4", "fde_end": "0x2f41860", "kind": "add", "reg": "x1"}
- {"pc": "0x2f4553c", "adrp": "0x2f45534", "target": "0x1194dc5", "label": "ActorRootArrayForeachLoopNodeRuntime", "keywords": ["ActorRoot"], "fde_start": "0x2f45508", "fde_end": "0x2f455a4", "kind": "add", "reg": "x1"}
- {"pc": "0x2f457ac", "adrp": "0x2f457a4", "target": "0x11ef056", "label": "GlobalVariableActorRootArrayNodeRuntime", "keywords": ["ActorRoot"], "fde_start": "0x2f45778", "fde_end": "0x2f45814", "kind": "add", "reg": "x1"}
- {"pc": "0x2fce680", "adrp": "0x2fce67c", "target": "0x118179f", "label": "AGETemplate::ForbidMoveDirectionCmdDuration", "keywords": ["MoveDir"], "fde_start": "0x2fce670", "fde_end": "0x2fce6fc", "kind": "add", "reg": "x1"}
- {"pc": "0x2fd1c7c", "adrp": "0x2fd1c78", "target": "0x1194e93", "label": "AGETemplate::ActorPositionChangeEventListenerDuration", "keywords": ["ActorPos"], "fde_start": "0x2fd1c6c", "fde_end": "0x2fd1cf8", "kind": "add", "reg": "x1"}
- {"pc": "0x2fd81c4", "adrp": "0x2fd81c0", "target": "0x120912f", "label": "AGETemplate::MoveDirectionalLeapDuration", "keywords": ["MoveDir"], "fde_start": "0x2fd81b4", "fde_end": "0x2fd8240", "kind": "add", "reg": "x1"}
- {"pc": "0x2feec74", "adrp": "0x2feec70", "target": "0x11f5b78", "label": "AGETemplate::NewActorRootListAdd", "keywords": ["ActorRoot"], "fde_start": "0x2feec64", "fde_end": "0x2feecf0", "kind": "add", "reg": "x1"}
- {"pc": "0x2feefe8", "adrp": "0x2feefe4", "target": "0x11a16ca", "label": "AGETemplate::NewActorRootList", "keywords": ["ActorRoot"], "fde_start": "0x2feefd8", "fde_end": "0x2fef064", "kind": "add", "reg": "x1"}
- {"pc": "0x2ff1c64", "adrp": "0x2ff1c60", "target": "0x11e8310", "label": "AGETemplate::NewGetActorRootDuration", "keywords": ["ActorRoot"], "fde_start": "0x2ff1c54", "fde_end": "0x2ff1ce0", "kind": "add", "reg": "x1"}
- {"pc": "0x3023f28", "adrp": "0x3023f24", "target": "0x118ef13", "label": "AGETemplate::ValidateActorPositionTick", "keywords": ["ActorPos"], "fde_start": "0x3023f18", "fde_end": "0x3023fa4", "kind": "add", "reg": "x1"}
- {"pc": "0x30316f0", "adrp": "0x30316ec", "target": "0x1194f2e", "label": "AGETemplate::NewVariableVInt3CalTick", "keywords": ["VInt3"], "fde_start": "0x30316e0", "fde_end": "0x303176c", "kind": "add", "reg": "x1"}
- {"pc": "0x3038f04", "adrp": "0x3038f00", "target": "0x1194f75", "label": "AGETemplate::FilterTargetCacheMoveDirectionTick", "keywords": ["MoveDir"], "fde_start": "0x3038ef4", "fde_end": "0x3038f80", "kind": "add", "reg": "x1"}
- {"pc": "0x3042404", "adrp": "0x3042400", "target": "0x119adbb", "label": "AGETemplate::RecordActorPositionTick", "keywords": ["ActorPos"], "fde_start": "0x30423f4", "fde_end": "0x3042480", "kind": "add", "reg": "x1"}
- {"pc": "0x30488b0", "adrp": "0x30488ac", "target": "0x11c78ea", "label": "AGETemplate::GetDataFromActorRootList", "keywords": ["ActorRoot"], "fde_start": "0x30488a0", "fde_end": "0x304892c", "kind": "add", "reg": "x1"}
- {"pc": "0x3048f7c", "adrp": "0x3048f78", "target": "0x11a1921", "label": "AGETemplate::NewActorRootListCount", "keywords": ["ActorRoot"], "fde_start": "0x3048f6c", "fde_end": "0x3048ff8", "kind": "add", "reg": "x1"}
- {"pc": "0x3049654", "adrp": "0x3049650", "target": "0x11fc47e", "label": "AGETemplate::NewActorRootListRmv", "keywords": ["ActorRoot"], "fde_start": "0x3049644", "fde_end": "0x30496d0", "kind": "add", "reg": "x1"}
- {"pc": "0x30499bc", "adrp": "0x30499b8", "target": "0x11b5279", "label": "AGETemplate::NewActorRootListAddTick", "keywords": ["ActorRoot"], "fde_start": "0x30499ac", "fde_end": "0x3049a38", "kind": "add", "reg": "x1"}
- {"pc": "0x304cf78", "adrp": "0x304cf74", "target": "0x11680ef", "label": "AGETemplate::NewGetActorRootTick", "keywords": ["ActorRoot"], "fde_start": "0x304cf68", "fde_end": "0x304cff4", "kind": "add", "reg": "x1"}
- {"pc": "0x304d2d8", "adrp": "0x304d2d4", "target": "0x11a8ace", "label": "AGETemplate::NewRmvActorRootTick", "keywords": ["ActorRoot"], "fde_start": "0x304d2c8", "fde_end": "0x304d354", "kind": "add", "reg": "x1"}
- {"pc": "0x304d630", "adrp": "0x304d62c", "target": "0x11fc4db", "label": "AGETemplate::NewSaveActorRootTick", "keywords": ["ActorRoot"], "fde_start": "0x304d620", "fde_end": "0x304d6ac", "kind": "add", "reg": "x1"}
- {"pc": "0x31c90e8", "adrp": "0x31c90e0", "target": "0x11c79e4", "label": "AGE::RecordActorPositionTick", "keywords": ["ActorPos"], "fde_start": "0x31c90b4", "fde_end": "0x31c9150", "kind": "add", "reg": "x1"}
- {"pc": "0x31ca764", "adrp": "0x31ca75c", "target": "0x1188738", "label": "AGE::NewActorRootListCount", "keywords": ["ActorRoot"], "fde_start": "0x31ca730", "fde_end": "0x31ca7cc", "kind": "add", "reg": "x1"}
- {"pc": "0x31f3078", "adrp": "0x31f3070", "target": "0x11e1f76", "label": "AGE::NewVariableVInt3CalTick", "keywords": ["VInt3"], "fde_start": "0x31f3044", "fde_end": "0x31f30e0", "kind": "add", "reg": "x1"}
- {"pc": "0x3201b5c", "adrp": "0x3201b54", "target": "0x120962f", "label": "AGE::NewRmvActorRootTick", "keywords": ["ActorRoot"], "fde_start": "0x3201b28", "fde_end": "0x3201bc4", "kind": "add", "reg": "x1"}
- {"pc": "0x320202c", "adrp": "0x3202024", "target": "0x1202e52", "label": "AGE::NewSaveActorRootTick", "keywords": ["ActorRoot"], "fde_start": "0x3201ff8", "fde_end": "0x3202094", "kind": "add", "reg": "x1"}
- {"pc": "0x3212b58", "adrp": "0x3212b50", "target": "0x118f1f1", "label": "AGE::ValidateActorPositionTick", "keywords": ["ActorPos"], "fde_start": "0x3212b24", "fde_end": "0x3212bc0", "kind": "add", "reg": "x1"}
- {"pc": "0x3237150", "adrp": "0x3237148", "target": "0x11f602f", "label": "AGE::FilterTargetCacheMoveDirectionTick", "keywords": ["MoveDir"], "fde_start": "0x323711c", "fde_end": "0x32371b8", "kind": "add", "reg": "x1"}
- {"pc": "0x3242d08", "adrp": "0x3242d00", "target": "0x1202f6a", "label": "AGE::NewGetActorRootTick", "keywords": ["ActorRoot"], "fde_start": "0x3242cd4", "fde_end": "0x3242d70", "kind": "add", "reg": "x1"}
- {"pc": "0x3243664", "adrp": "0x324365c", "target": "0x11a8da1", "label": "AGE::NewActorRootListRmv", "keywords": ["ActorRoot"], "fde_start": "0x3243630", "fde_end": "0x32436cc", "kind": "add", "reg": "x1"}
- {"pc": "0x3243d64", "adrp": "0x3243d5c", "target": "0x11888c6", "label": "AGE::NewActorRootListAddTick", "keywords": ["ActorRoot"], "fde_start": "0x3243d30", "fde_end": "0x3243dcc", "kind": "add", "reg": "x1"}
- {"pc": "0x3244288", "adrp": "0x3244280", "target": "0x11db7b6", "label": "AGE::GetDataFromActorRootList", "keywords": ["ActorRoot"], "fde_start": "0x3244254", "fde_end": "0x32442f0", "kind": "add", "reg": "x1"}
- {"pc": "0x3268d90", "adrp": "0x3268d88", "target": "0x1141629", "label": "AGE::NewActorRootListAdd", "keywords": ["ActorRoot"], "fde_start": "0x3268d5c", "fde_end": "0x3268df8", "kind": "add", "reg": "x1"}
- {"pc": "0x32698c8", "adrp": "0x32698c0", "target": "0x11bb63b", "label": "AGE::NewActorRootList", "keywords": ["ActorRoot"], "fde_start": "0x3269894", "fde_end": "0x3269930", "kind": "add", "reg": "x1"}
- {"pc": "0x3285810", "adrp": "0x3285808", "target": "0x11952d9", "label": "AGE::NewGetActorRootDuration", "keywords": ["ActorRoot"], "fde_start": "0x32857dc", "fde_end": "0x3285878", "kind": "add", "reg": "x1"}
- {"pc": "0x33bb3e0", "adrp": "0x33bb3d8", "target": "0x119541b", "label": "ActorRootBinderNodeRuntime", "keywords": ["ActorRoot"], "fde_start": "0x33bb3ac", "fde_end": "0x33bb448", "kind": "add", "reg": "x1"}
- {"pc": "0x33bc220", "adrp": "0x33bc218", "target": "0x12030f4", "label": "ActorRootConstantArrayNodeRuntime", "keywords": ["ActorRoot"], "fde_start": "0x33bc1ec", "fde_end": "0x33bc288", "kind": "add", "reg": "x1"}
- {"pc": "0x33bc568", "adrp": "0x33bc560", "target": "0x11fc9d8", "label": "ActorRootArrayNodeRuntime", "keywords": ["ActorRoot"], "fde_start": "0x33bc534", "fde_end": "0x33bc5d0", "kind": "add", "reg": "x1"}
- {"pc": "0x3466a9c", "adrp": "0x3466a94", "target": "0x11c7eed", "label": "USGMobaActorRoot", "keywords": ["ActorRoot"], "fde_start": "0x3466a60", "fde_end": "0x3466c6c", "kind": "add", "reg": "x1"}
- {"pc": "0x34670fc", "adrp": "0x34670ec", "target": "0x116eb7b", "label": "Mods/USG/GameModes/Moba55/src/GamePlay/GameMode/Adapter/USGMobaActorRoot.cpp", "keywords": ["ActorRoot"], "fde_start": "0x34670c0", "fde_end": "0x3467138", "kind": "add", "reg": "x0"}
- {"pc": "0x34c06c4", "adrp": "0x34c06bc", "target": "0x1188b92", "label": "ConstantActorRootNodeRuntime", "keywords": ["ActorRoot"], "fde_start": "0x34c0690", "fde_end": "0x34c072c", "kind": "add", "reg": "x1"}
- {"pc": "0x34c0c58", "adrp": "0x34c0c50", "target": "0x114edaa", "label": "VariableActorRootNodeRuntime", "keywords": ["ActorRoot"], "fde_start": "0x34c0c24", "fde_end": "0x34c0cc0", "kind": "add", "reg": "x1"}
- {"pc": "0x353639c", "adrp": "0x3536394", "target": "0x11af290", "label": "AGE::MoveDirectionalLeapDuration", "keywords": ["MoveDir"], "fde_start": "0x3536364", "fde_end": "0x3536510", "kind": "add", "reg": "x1"}
- {"pc": "0x3556948", "adrp": "0x3556940", "target": "0x11fcc04", "label": "AGE::ForbidMoveDirectionCmdDuration", "keywords": ["MoveDir"], "fde_start": "0x3556914", "fde_end": "0x35569b0", "kind": "add", "reg": "x1"}
- {"pc": "0x358c164", "adrp": "0x358c15c", "target": "0x11624e1", "label": "AGE::CheckActorPositionDuration", "keywords": ["ActorPos"], "fde_start": "0x358c130", "fde_end": "0x358c1cc", "kind": "add", "reg": "x1"}
- {"pc": "0x35b4a00", "adrp": "0x35b49f8", "target": "0x11d50f7", "label": "AGE::ActorPositionChangeEventListenerDuration", "keywords": ["ActorPos"], "fde_start": "0x35b49cc", "fde_end": "0x35b4a68", "kind": "add", "reg": "x1"}
- {"pc": "0x3770308", "adrp": "0x3770300", "target": "0x116278a", "label": "Project8GetRandomEnemyPositionNode", "keywords": ["EnemyPos"], "fde_start": "0x37702cc", "fde_end": "0x3770364", "kind": "add", "reg": "x1"}
- {"pc": "0x3775ed0", "adrp": "0x3775ec8", "target": "0x11e258a", "label": "Project8GetMaxtrixCrowdedEnemyPositionNode", "keywords": ["EnemyPos"], "fde_start": "0x3775e94", "fde_end": "0x3775f2c", "kind": "add", "reg": "x1"}
- {"pc": "0x379ada0", "adrp": "0x379ad98", "target": "0x1168a3d", "label": "Project8GetHighestDamageActorPositionNode", "keywords": ["ActorPos"], "fde_start": "0x379ad64", "fde_end": "0x379adfc", "kind": "add", "reg": "x1"}
- {"pc": "0x379de68", "adrp": "0x379de60", "target": "0x11cea40", "label": "Project8GetCrossEnemyPositionNode", "keywords": ["EnemyPos"], "fde_start": "0x379de2c", "fde_end": "0x379dec4", "kind": "add", "reg": "x1"}
- {"pc": "0x37f5b88", "adrp": "0x37f5b80", "target": "0x11e90db", "label": "VInt3LengthNode", "keywords": ["VInt3"], "fde_start": "0x37f5b4c", "fde_end": "0x37f5be4", "kind": "add", "reg": "x1"}
- {"pc": "0x3866490", "adrp": "0x3866488", "target": "0x11a95f4", "label": "GetPositionInUnityObjectPairSetNode", "keywords": ["GetPositionInUnity"], "fde_start": "0x3866454", "fde_end": "0x38664ec", "kind": "add", "reg": "x1"}
- {"pc": "0x3872d0c", "adrp": "0x3872d04", "target": "0x11f6ae6", "label": "RecordActorPositionNode", "keywords": ["ActorPos"], "fde_start": "0x3872cd0", "fde_end": "0x3872d68", "kind": "add", "reg": "x1"}
- {"pc": "0x388fa30", "adrp": "0x388fa28", "target": "0x114838b", "label": "NewGetVInt3Variable", "keywords": ["VInt3"], "fde_start": "0x388f9f4", "fde_end": "0x388fa8c", "kind": "add", "reg": "x1"}
- {"pc": "0x388fe7c", "adrp": "0x388fe74", "target": "0x11c85da", "label": "NewSaveVInt3Variable", "keywords": ["VInt3"], "fde_start": "0x388fe40", "fde_end": "0x388fed8", "kind": "add", "reg": "x1"}
- {"pc": "0x38a2fd0", "adrp": "0x38a2fc8", "target": "0x11fd1eb", "label": "NewSaveActorRoot", "keywords": ["ActorRoot"], "fde_start": "0x38a2f94", "fde_end": "0x38a302c", "kind": "add", "reg": "x1"}
- {"pc": "0x38a34f4", "adrp": "0x38a34ec", "target": "0x114f545", "label": "NewGetActorRoot", "keywords": ["ActorRoot"], "fde_start": "0x38a34b8", "fde_end": "0x38a3550", "kind": "add", "reg": "x1"}
- {"pc": "0x38becc8", "adrp": "0x38becc0", "target": "0x1155a85", "label": "SetActorParamConfigActorRootNode", "keywords": ["ActorRoot"], "fde_start": "0x38bec8c", "fde_end": "0x38bed24", "kind": "add", "reg": "x1"}
- {"pc": "0x38bf238", "adrp": "0x38bf230", "target": "0x11d5801", "label": "GetActorParamConfigActorRootNode", "keywords": ["ActorRoot"], "fde_start": "0x38bf1fc", "fde_end": "0x38bf294", "kind": "add", "reg": "x1"}
- {"pc": "0x38c03c8", "adrp": "0x38c03c0", "target": "0x118278f", "label": "SetActorParamConfigVInt3Node", "keywords": ["VInt3"], "fde_start": "0x38c038c", "fde_end": "0x38c0424", "kind": "add", "reg": "x1"}
- {"pc": "0x38c09b8", "adrp": "0x38c09b0", "target": "0x1195bcd", "label": "GetActorParamConfigVInt3", "keywords": ["VInt3"], "fde_start": "0x38c097c", "fde_end": "0x38c0a14", "kind": "add", "reg": "x1"}
- {"pc": "0x38d4910", "adrp": "0x38d4908", "target": "0x115c402", "label": "IsWorldVInt3ValidNode", "keywords": ["VInt3"], "fde_start": "0x38d48d4", "fde_end": "0x38d496c", "kind": "add", "reg": "x1"}
- {"pc": "0x38dfb20", "adrp": "0x38dfb18", "target": "0x12039f1", "label": "GetVInt3YValueNode", "keywords": ["VInt3"], "fde_start": "0x38dfae4", "fde_end": "0x38dfb7c", "kind": "add", "reg": "x1"}

## Candidate functions and disassembly

### Function start 0x23fa324
Hits: [{"pc": "0x23fa32c", "adrp": "0x23fa328", "target": "0x11a5472", "label": "VInt3", "keywords": ["VInt3"], "fde_start": "0x23fa324", "fde_end": "0x23fa338", "kind": "add", "reg": "x0"}]
~~~asm
0x023FA324: adrp     x8, #0x522a000
0x023FA328: adrp     x0, #0x11a5000
0x023FA32C: add      x0, x0, #0x472
0x023FA330: ldr      x1, [x8, #0x2a8]
0x023FA334: br       x1
~~~

### Function start 0x23fae04
Hits: [{"pc": "0x23fae1c", "adrp": "0x23fae14", "target": "0x11a5472", "label": "VInt3", "keywords": ["VInt3"], "fde_start": "0x23fae04", "fde_end": "0x23fae3c", "kind": "add", "reg": "x3"}]
~~~asm
0x023FAE04: stp      x30, x19, [sp, #-0x10]!
0x023FAE08: adrp     x19, #0x5407000
0x023FAE0C: adrp     x2, #0x115e000
0x023FAE10: add      x19, x19, #0x360
0x023FAE14: adrp     x3, #0x11a5000
0x023FAE18: add      x2, x2, #0xe9b
0x023FAE1C: add      x3, x3, #0x472
0x023FAE20: mov      x0, x19
0x023FAE24: mov      w1, #0x100
0x023FAE28: bl       #0x4b40240
0x023FAE2C: mov      x0, x19
0x023FAE30: strb     wzr, [x19, #0xff]
0x023FAE34: ldp      x30, x19, [sp], #0x10
0x023FAE38: ret      
~~~

### Function start 0x24aca80
Hits: [{"pc": "0x24acbfc", "adrp": "0x24acbf4", "target": "0x11d8792", "label": "invisible_range", "keywords": ["invisible"], "fde_start": "0x24aca80", "fde_end": "0x24acf54", "kind": "add", "reg": "x9"}, {"pc": "0x24acc90", "adrp": "0x24acc84", "target": "0x116570b", "label": "[Init] m_invisible_range:%d", "keywords": ["invisible"], "fde_start": "0x24aca80", "fde_end": "0x24acf54", "kind": "add", "reg": "x2"}]
~~~asm
0x024ACA80: sub      sp, sp, #0x90
0x024ACA84: stp      x30, x25, [sp, #0x50]
0x024ACA88: stp      x24, x23, [sp, #0x60]
0x024ACA8C: stp      x22, x21, [sp, #0x70]
0x024ACA90: stp      x20, x19, [sp, #0x80]
0x024ACA94: adrp     x9, #0x11ac000
0x024ACA98: mov      w8, #0xe10
0x024ACA9C: add      x9, x9, #0x56
0x024ACAA0: mov      x19, x1
0x024ACAA4: mov      x20, x0
0x024ACAA8: mov      w21, #0x2c
0x024ACAAC: str      w8, [x0, #0x20]
0x024ACAB0: add      x1, sp, #0x30
0x024ACAB4: ldr      q0, [x9]
0x024ACAB8: mov      x0, x19
0x024ACABC: ldur     x22, [x9, #0xe]
0x024ACAC0: strb     w21, [sp, #0x30]
0x024ACAC4: strb     wzr, [sp, #0x47]
0x024ACAC8: str      q0, [sp, #0x20]
0x024ACACC: stur     q0, [sp, #0x31]
0x024ACAD0: stur     x22, [sp, #0x3f]
0x024ACAD4: bl       #0x227e1dc
0x024ACAD8: add      x24, x19, #8
0x024ACADC: cmp      x24, x0
0x024ACAE0: b.eq     #0x24acb2c
0x024ACAE4: ldr      q0, [sp, #0x20]
0x024ACAE8: add      x1, sp, #0x48
0x024ACAEC: add      x2, sp, #0x30
0x024ACAF0: mov      x0, x19
0x024ACAF4: strb     w21, [sp, #0x30]
0x024ACAF8: stur     q0, [sp, #0x31]
0x024ACAFC: stur     x22, [sp, #0x3f]
0x024ACB00: strb     wzr, [sp, #0x47]
0x024ACB04: bl       #0x227e070
0x024ACB08: ldr      x8, [x0]
0x024ACB0C: cbz      x8, #0x24acf28
0x024ACB10: ldrb     w9, [x8, #0x38]
0x024ACB14: ldr      x10, [x8, #0x48]
0x024ACB18: add      x8, x8, #0x39
0x024ACB1C: tst      w9, #1
0x024ACB20: csel     x0, x8, x10, eq
0x024ACB24: bl       #0x4b400f0
0x024ACB28: str      w0, [x20, #0x20]
0x024ACB2C: adrp     x23, #0x509c000
0x024ACB30: ldr      x8, [x23, #0x70]
0x024ACB34: blr      x8
0x024ACB38: adrp     x1, #0x11ec000
0x024ACB3C: adrp     x2, #0x11c5000
0x024ACB40: ldr      w3, [x20, #0x20]
0x024ACB44: add      x1, x1, #0x1da
0x024ACB48: add      x2, x2, #0x19b
0x024ACB4C: bl       #0x2185854
0x024ACB50: adrp     x9, #0x11f3000
0x024ACB54: mov      w8, #1
0x024ACB58: add      x9, x9, #0x2d3
0x024ACB5C: mov      w21, #0x1e
0x024ACB60: add      x1, sp, #0x30
0x024ACB64: mov      x0, x19
0x024ACB68: str      w8, [x20, #0x1c]
0x024ACB6C: ldr      x22, [x9]
0x024ACB70: strb     w21, [sp, #0x30]
0x024ACB74: ldur     x25, [x9, #7]
0x024ACB78: strb     wzr, [sp, #0x40]
0x024ACB7C: stur     x22, [sp, #0x31]
0x024ACB80: str      x25, [sp, #0x38]
0x024ACB84: bl       #0x227e1dc
0x024ACB88: cmp      x24, x0
0x024ACB8C: b.eq     #0x24acbd4
0x024ACB90: add      x1, sp, #0x48
0x024ACB94: add      x2, sp, #0x30
0x024ACB98: mov      x0, x19
0x024ACB9C: strb     w21, [sp, #0x30]
0x024ACBA0: stur     x22, [sp, #0x31]
0x024ACBA4: str      x25, [sp, #0x38]
0x024ACBA8: strb     wzr, [sp, #0x40]
0x024ACBAC: bl       #0x227e070
0x024ACBB0: ldr      x8, [x0]
0x024ACBB4: cbz      x8, #0x24acf28
0x024ACBB8: ldrb     w9, [x8, #0x38]
0x024ACBBC: ldr      x10, [x8, #0x48]
0x024ACBC0: add      x8, x8, #0x39
0x024ACBC4: tst      w9, #1
0x024ACBC8: csel     x0, x8, x10, eq
0x024ACBCC: bl       #0x4b400f0
0x024ACBD0: str      w0, [x20, #0x1c]
0x024ACBD4: ldr      x8, [x23, #0x70]
0x024ACBD8: blr      x8
0x024ACBDC: adrp     x1, #0x11ec000
0x024ACBE0: adrp     x2, #0x11ec000
0x024ACBE4: ldr      w3, [x20, #0x1c]
0x024ACBE8: add      x1, x1, #0x1da
0x024ACBEC: add      x2, x2, #0x1fa
0x024ACBF0: bl       #0x2185854
0x024ACBF4: adrp     x9, #0x11d8000
0x024ACBF8: mov      w8, #0x96
0x024ACBFC: add      x9, x9, #0x792
0x024ACC00: strb     w21, [sp, #0x30]
0x024ACC04: add      x1, sp, #0x30
0x024ACC08: mov      x0, x19
0x024ACC0C: str      w8, [x20, #0x24]
0x024ACC10: ldr      x22, [x9]
0x024ACC14: strb     wzr, [sp, #0x40]
0x024ACC18: ldur     x21, [x9, #7]
0x024ACC1C: stur     x22, [sp, #0x31]
0x024ACC20: str      x21, [sp, #0x38]
0x024ACC24: bl       #0x227e1dc
0x024ACC28: cmp      x24, x0
0x024ACC2C: b.eq     #0x24acc78
0x024ACC30: mov      w8, #0x1e
0x024ACC34: add      x1, sp, #0x48
0x024ACC38: add      x2, sp, #0x30
0x024ACC3C: mov      x0, x19
0x024ACC40: stur     x22, [sp, #0x31]
0x024ACC44: str      x21, [sp, #0x38]
0x024ACC48: strb     w8, [sp, #0x30]
0x024ACC4C: strb     wzr, [sp, #0x40]
0x024ACC50: bl       #0x227e070
0x024ACC54: ldr      x8, [x0]
0x024ACC58: cbz      x8, #0x24acf28
0x024ACC5C: ldrb     w9, [x8, #0x38]
0x024ACC60: ldr      x10, [x8, #0x48]
0x024ACC64: add      x8, x8, #0x39
0x024ACC68: tst      w9, #1
0x024ACC6C: csel     x0, x8, x10, eq
0x024ACC70: bl       #0x4b400f0
0x024ACC74: str      w0, [x20, #0x24]
0x024ACC78: ldr      x8, [x23, #0x70]
0x024ACC7C: blr      x8
0x024ACC80: adrp     x1, #0x11ec000
0x024ACC84: adrp     x2, #0x1165000
0x024ACC88: ldr      w3, [x20, #0x24]
0x024ACC8C: add      x1, x1, #0x1da
0x024ACC90: add      x2, x2, #0x70b
0x024ACC94: bl       #0x2185854
0x024ACC98: adrp     x9, #0x1165000
0x024ACC9C: mov      w8, #1
0x024ACCA0: add      x9, x9, #0x727
0x024ACCA4: mov      w21, #0x1c
0x024ACCA8: add      x1, sp, #0x30
0x024ACCAC: mov      x0, x19
0x024ACCB0: str      w8, [x20, #0x28]
0x024ACCB4: ldr      x22, [x9]
0x024ACCB8: strb     w21, [sp, #0x30]
0x024ACCBC: ldur     x25, [x9, #6]
0x024ACCC0: strb     wzr, [sp, #0x3f]
0x024ACCC4: stur     x22, [sp, #0x31]
0x024ACCC8: stur     x25, [sp, #0x37]
0x024ACCCC: bl       #0x227e1dc
0x024ACCD0: cmp      x24, x0
0x024ACCD4: b.eq     #0x24acd1c
0x024ACCD8: add      x1, sp, #0x48
0x024ACCDC: add      x2, sp, #0x30
0x024ACCE0: mov      x0, x19
0x024ACCE4: strb     w21, [sp, #0x30]
0x024ACCE8: stur     x22, [sp, #0x31]
0x024ACCEC: stur     x25, [sp, #0x37]
0x024ACCF0: strb     wzr, [sp, #0x3f]
0x024ACCF4: bl       #0x227e070
0x024ACCF8: ldr      x8, [x0]
0x024ACCFC: cbz      x8, #0x24acf28
0x024ACD00: ldrb     w9, [x8, #0x38]
0x024ACD04: ldr      x10, [x8, #0x48]
0x024ACD08: add      x8, x8, #0x39
0x024ACD0C: tst      w9, #1
0x024ACD10: csel     x0, x8, x10, eq
0x024ACD14: bl       #0x4b400f0
0x024ACD18: str      w0, [x20, #0x28]
0x024ACD1C: ldr      x8, [x23, #0x70]
0x024ACD20: blr      x8
0x024ACD24: adrp     x1, #0x11ec000
0x024ACD28: adrp     x2, #0x1158000
0x024ACD2C: ldr      w3, [x20, #0x28]
0x024ACD30: add      x1, x1, #0x1da
0x024ACD34: add      x2, x2, #0x9ef
0x024ACD38: bl       #0x2185854
0x024ACD3C: adrp     x8, #0x1192000
0x024ACD40: mov      w21, #0x190
0x024ACD44: add      x8, x8, #0x55f
0x024ACD48: mov      w22, #0x2a
0x024ACD4C: add      x1, sp, #0x30
0x024ACD50: mov      x0, x19
0x024ACD54: str      w21, [x20, #0x2c]
0x024ACD58: ldr      q0, [x8]
0x024ACD5C: strb     w22, [sp, #0x30]
0x024ACD60: ldur     x25, [x8, #0xd]
0x024ACD64: strb     wzr, [sp, #0x46]
0x024ACD68: str      q0, [sp, #0x20]
0x024ACD6C: stur     q0, [sp, #0x31]
0x024ACD70: stur     x25, [sp, #0x3e]
0x024ACD74: bl       #0x227e1dc
0x024ACD78: cmp      x24, x0
0x024ACD7C: b.eq     #0x24acdc8
0x024ACD80: ldr      q0, [sp, #0x20]
0x024ACD84: add      x1, sp, #0x48
0x024ACD88: add      x2, sp, #0x30
0x024ACD8C: mov      x0, x19
0x024ACD90: strb     w22, [sp, #0x30]
0x024ACD94: stur     q0, [sp, #0x31]
0x024ACD98: stur     x25, [sp, #0x3e]
0x024ACD9C: strb     wzr, [sp, #0x46]
0x024ACDA0: bl       #0x227e070
0x024ACDA4: ldr      x8, [x0]
0x024ACDA8: cbz      x8, #0x24acf28
0x024ACDAC: ldrb     w9, [x8, #0x38]
0x024ACDB0: ldr      x10, [x8, #0x48]
0x024ACDB4: add      x8, x8, #0x39
0x024ACDB8: tst      w9, #1
0x024ACDBC: csel     x0, x8, x10, eq
0x024ACDC0: bl       #0x4b400f0
0x024ACDC4: str      w0, [x20, #0x2c]
0x024ACDC8: ldr      x8, [x23, #0x70]
0x024ACDCC: blr      x8
0x024ACDD0: adrp     x1, #0x11ec000
0x024ACDD4: adrp     x2, #0x11b2000
0x024ACDD8: ldr      w3, [x20, #0x2c]
0x024ACDDC: add      x1, x1, #0x1da
0x024ACDE0: add      x2, x2, #0x5bc
0x024ACDE4: bl       #0x2185854
0x024ACDE8: mov      w0, #0x20
0x024ACDEC: str      w21, [x20, #0x30]
0x024ACDF0: bl       #0x4b40050
0x024ACDF4: adrp     x9, #0x117f000
0x024ACDF8: adrp     x8, #0x113d000
0x024ACDFC: add      x9, x9, #0x1bb
0x024ACE00: mov      x21, x0
0x024ACE04: str      x0, [sp, #0x40]
0x024ACE08: add      x1, sp, #0x30
0x024ACE0C: ldr      q2, [x8, #0xa0]
0x024ACE10: strb     wzr, [x0, #0x1a]
0x024ACE14: ldr      q0, [x9]
0x024ACE18: ldur     q1, [x9, #0xa]
0x024ACE1C: str      q2, [sp]
0x024ACE20: str      q0, [x0]
0x024ACE24: stur     q1, [x0, #0xa]
0x024ACE28: mov      x0, x19
0x024ACE2C: stp      q1, q0, [sp, #0x10]
0x024ACE30: str      q2, [sp, #0x30]
0x024ACE34: bl       #0x227e1dc
0x024ACE38: mov      x22, x0
0x024ACE3C: mov      x0, x21
~~~

### Function start 0x24ad7fc
Hits: [{"pc": "0x24ad994", "adrp": "0x24ad988", "target": "0x117f1d6", "label": "view_manager::ViewManager::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x24ad7fc", "fde_end": "0x24ade74", "kind": "add", "reg": "x1"}, {"pc": "0x24ad99c", "adrp": "0x24ad98c", "target": "0x114b500", "label": "hero:%d loc:(%d, %d) invisible2visible change to 55000", "keywords": ["invisible"], "fde_start": "0x24ad7fc", "fde_end": "0x24ade74", "kind": "add", "reg": "x2"}, {"pc": "0x24ada78", "adrp": "0x24ada68", "target": "0x117f1d6", "label": "view_manager::ViewManager::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x24ad7fc", "fde_end": "0x24ade74", "kind": "add", "reg": "x1"}]
~~~asm
0x024AD7FC: sub      sp, sp, #0x80
0x024AD800: stp      x29, x30, [sp, #0x20]
0x024AD804: stp      x28, x27, [sp, #0x30]
0x024AD808: stp      x26, x25, [sp, #0x40]
0x024AD80C: stp      x24, x23, [sp, #0x50]
0x024AD810: stp      x22, x21, [sp, #0x60]
0x024AD814: stp      x20, x19, [sp, #0x70]
0x024AD818: ldp      x21, x8, [x1, #0x68]
0x024AD81C: cmp      x21, x8
0x024AD820: b.eq     #0x24ade50
0x024AD824: mov      x19, x2
0x024AD828: mov      x20, x1
0x024AD82C: mov      x22, x0
0x024AD830: add      x8, x2, #0xae0
0x024AD834: adrp     x23, #0x508a000
0x024AD838: adrp     x25, #0x508a000
0x024AD83C: str      x8, [sp, #0x18]
0x024AD840: b        #0x24ad874
0x024AD844: adrp     x8, #0x508a000
0x024AD848: ldr      x8, [x8, #0xcf0]
0x024AD84C: mov      x0, x22
0x024AD850: mov      x1, x20
0x024AD854: mov      x2, x19
0x024AD858: mov      x3, x21
0x024AD85C: mov      w4, w27
0x024AD860: blr      x8
0x024AD864: ldr      x8, [x20, #0x70]
0x024AD868: add      x21, x21, #0x3f0
0x024AD86C: cmp      x21, x8
0x024AD870: b.eq     #0x24ade50
0x024AD874: ldr      w8, [x21, #0x18]
0x024AD878: ldr      w9, [x22, #0x18]
0x024AD87C: cmp      w8, w9
0x024AD880: b.eq     #0x24ad864
0x024AD884: ldr      x8, [x23, #0xc70]
0x024AD888: mov      x0, x22
0x024AD88C: mov      x1, x21
0x024AD890: blr      x8
0x024AD894: tbz      w0, #0, #0x24ad864
0x024AD898: adrp     x8, #0x508a000
0x024AD89C: mov      x0, x22
0x024AD8A0: mov      x1, x21
0x024AD8A4: ldr      x8, [x8, #0xc80]
0x024AD8A8: blr      x8
0x024AD8AC: adrp     x8, #0x508a000
0x024AD8B0: mov      w27, w0
0x024AD8B4: mov      x0, x22
0x024AD8B8: mov      x1, x20
0x024AD8BC: mov      x2, x21
0x024AD8C0: mov      x3, x19
0x024AD8C4: ldr      x8, [x8, #0xca0]
0x024AD8C8: blr      x8
0x024AD8CC: mov      w29, w0
0x024AD8D0: ldr      x8, [x25, #0xcc0]
0x024AD8D4: mov      x0, x22
0x024AD8D8: mov      x1, x20
0x024AD8DC: mov      x2, x21
0x024AD8E0: mov      x3, x19
0x024AD8E4: blr      x8
0x024AD8E8: and      w8, w27, w29
0x024AD8EC: tbnz     w0, #0, #0x24ad8f4
0x024AD8F0: tbnz     w8, #0, #0x24ad864
0x024AD8F4: mov      x26, x21
0x024AD8F8: ldr      w9, [x26, #4]!
0x024AD8FC: cmp      w9, #0x74
0x024AD900: b.eq     #0x24ad90c
0x024AD904: cmp      w9, #0x99
0x024AD908: b.ne     #0x24ad974
0x024AD90C: ldr      x8, [x22, #0x10]
0x024AD910: add      x28, x21, #0x20
0x024AD914: mov      x0, x22
0x024AD918: mov      x1, x28
0x024AD91C: mov      w3, #1
0x024AD920: add      x2, x8, #0x20
0x024AD924: adrp     x8, #0x517f000
0x024AD928: ldr      x8, [x8, #0x388]
0x024AD92C: blr      x8
0x024AD930: ldr      w8, [x21, #4]
0x024AD934: mov      w27, w0
0x024AD938: cmp      w8, #0x74
0x024AD93C: b.eq     #0x24ad9c0
0x024AD940: adrp     x24, #0x5180000
0x024AD944: cmp      w8, #0x99
0x024AD948: b.ne     #0x24ad9cc
0x024AD94C: ldrb     w8, [x21, #0x358]
0x024AD950: cbnz     w8, #0x24ad9cc
0x024AD954: adrp     x8, #0x508a000
0x024AD958: mov      x0, x22
0x024AD95C: mov      x1, x20
0x024AD960: mov      x2, x21
0x024AD964: mov      w3, w27
0x024AD968: ldr      x8, [x8, #0xcd0]
0x024AD96C: blr      x8
0x024AD970: b        #0x24ad864
0x024AD974: and      w9, w27, w0
0x024AD978: tbz      w9, #0, #0x24ada1c
0x024AD97C: adrp     x8, #0x509c000
0x024AD980: ldr      x8, [x8, #0x70]
0x024AD984: blr      x8
0x024AD988: adrp     x1, #0x117f000
0x024AD98C: adrp     x2, #0x114b000
0x024AD990: ldr      w3, [x21, #4]
0x024AD994: add      x1, x1, #0x1d6
0x024AD998: ldr      w4, [x21, #0x20]
0x024AD99C: add      x2, x2, #0x500
0x024AD9A0: ldr      w5, [x21, #0x28]
0x024AD9A4: bl       #0x2185854
0x024AD9A8: adrp     x8, #0x508a000
0x024AD9AC: mov      x0, x22
0x024AD9B0: mov      x1, x21
0x024AD9B4: ldr      x8, [x8, #0xcb0]
0x024AD9B8: blr      x8
0x024AD9BC: b        #0x24ad864
0x024AD9C0: ldrb     w8, [x21, #0x358]
0x024AD9C4: adrp     x24, #0x5180000
0x024AD9C8: cbz      w8, #0x24adba8
0x024AD9CC: mov      w3, #0xe8fa
0x024AD9D0: ldr      x8, [x24, #0x68]
0x024AD9D4: mov      x0, x22
0x024AD9D8: mov      x1, x20
0x024AD9DC: mov      x2, x21
0x024AD9E0: movk     w3, #0xd, lsl #16
0x024AD9E4: blr      x8
0x024AD9E8: tbnz     w0, #0, #0x24ada10
0x024AD9EC: mov      w9, #0xe8fa
0x024AD9F0: ldr      x8, [x24, #0x68]
0x024AD9F4: movk     w9, #0xd, lsl #16
0x024AD9F8: mov      x0, x22
0x024AD9FC: add      w3, w9, #1
0x024ADA00: mov      x1, x20
0x024ADA04: mov      x2, x21
0x024ADA08: blr      x8
0x024ADA0C: tbz      w0, #0, #0x24ada24
0x024ADA10: ldrb     w8, [x21, #0x358]
0x024ADA14: cbnz     w8, #0x24ada38
0x024ADA18: b        #0x24ad844
0x024ADA1C: tbnz     w8, #0, #0x24ad864
0x024ADA20: b        #0x24ad90c
0x024ADA24: ldrb     w8, [x21, #0x358]
0x024ADA28: cmp      w8, #0
0x024ADA2C: cset     w8, eq
0x024ADA30: and      w8, w29, w8
0x024ADA34: tbnz     w8, #0, #0x24ad864
0x024ADA38: ldr      w8, [x21, #4]
0x024ADA3C: cmp      w8, #0xc4
0x024ADA40: b.ne     #0x24ada94
0x024ADA44: cmp      w27, #0x1d
0x024ADA48: b.gt     #0x24ada94
0x024ADA4C: ldr      x9, [x22, #0x10]
0x024ADA50: ldrb     w9, [x9, #0x358]
0x024ADA54: cbz      w9, #0x24ada94
0x024ADA58: adrp     x8, #0x509c000
0x024ADA5C: ldr      x8, [x8, #0x70]
0x024ADA60: blr      x8
0x024ADA64: ldr      x8, [x22, #0x10]
0x024ADA68: adrp     x1, #0x117f000
0x024ADA6C: adrp     x2, #0x11ac000
0x024ADA70: ldr      w3, [x21, #4]
0x024ADA74: ldrb     w4, [x21, #0x358]
0x024ADA78: add      x1, x1, #0x1d6
0x024ADA7C: ldr      w5, [x8, #4]
0x024ADA80: add      x2, x2, #0x6d
0x024ADA84: ldrb     w6, [x8, #0x358]
0x024ADA88: mov      w7, w27
0x024ADA8C: bl       #0x2185854
0x024ADA90: b        #0x24ad864
0x024ADA94: ldr      x9, [sp, #0x18]
0x024ADA98: ldr      x9, [x9]
0x024ADA9C: cbz      x9, #0x24ad864
0x024ADAA0: ldr      x24, [sp, #0x18]
0x024ADAA4: ldr      w10, [x9, #0x1c]
0x024ADAA8: cmp      w10, w8
0x024ADAAC: cset     w10, lt
0x024ADAB0: csel     x24, x24, x9, lt
0x024ADAB4: ldr      x9, [x9, w10, uxtw #3]
0x024ADAB8: cbnz     x9, #0x24adaa4
0x024ADABC: ldr      x9, [sp, #0x18]
0x024ADAC0: cmp      x24, x9
0x024ADAC4: b.eq     #0x24ad864
0x024ADAC8: ldr      w9, [x24, #0x1c]
0x024ADACC: cmp      w8, w9
0x024ADAD0: b.lt     #0x24ad864
0x024ADAD4: adrp     x8, #0x5089000
0x024ADAD8: ldr      x0, [x19, #0xad0]
0x024ADADC: mov      x1, x26
0x024ADAE0: ldr      x8, [x8, #0x210]
0x024ADAE4: blr      x8
0x024ADAE8: ldr      x8, [x19, #0xad0]
0x024ADAEC: add      x8, x8, #8
0x024ADAF0: cmp      x8, x0
0x024ADAF4: b.eq     #0x24ad864
0x024ADAF8: ldr      w8, [x26]
0x024ADAFC: cmp      w8, #0x1f8
0x024ADB00: b.ne     #0x24adbb4
0x024ADB04: ldp      x29, x8, [x20, #0xc8]
0x024ADB08: mov      w9, #0x9680
0x024ADB0C: movk     w9, #0x98, lsl #16
0x024ADB10: cmp      x29, x8
0x024ADB14: str      w9, [sp, #0x14]
0x024ADB18: b.eq     #0x24adc04
0x024ADB1C: str      wzr, [sp, #0x10]
0x024ADB20: b        #0x24adb34
0x024ADB24: ldr      x8, [x20, #0xd0]
0x024ADB28: add      x29, x29, #0xb8
0x024ADB2C: cmp      x29, x8
0x024ADB30: b.eq     #0x24adc08
0x024ADB34: adrp     x8, #0x517f000
0x024ADB38: ldr      w1, [x29]
0x024ADB3C: mov      x0, x22
0x024ADB40: ldr      x8, [x8, #0xb78]
0x024ADB44: blr      x8
0x024ADB48: tbz      w0, #0, #0x24adb24
0x024ADB4C: ldr      w8, [x29, #0x2c]
0x024ADB50: cmp      w8, #1
0x024ADB54: b.lt     #0x24adb24
0x024ADB58: adrp     x8, #0x508a000
0x024ADB5C: mov      x0, x22
0x024ADB60: mov      x1, x29
0x024ADB64: ldr      x8, [x8, #0xc90]
0x024ADB68: blr      x8
0x024ADB6C: tbz      w0, #0, #0x24adb24
0x024ADB70: adrp     x8, #0x517f000
0x024ADB74: add      x2, x29, #0x14
0x024ADB78: mov      x0, x22
0x024ADB7C: mov      x1, x28
0x024ADB80: mov      w3, #1
0x024ADB84: mov      w9, #1
0x024ADB88: ldr      x8, [x8, #0x388]
0x024ADB8C: str      w9, [sp, #0x10]
0x024ADB90: blr      x8
0x024ADB94: ldr      w8, [sp, #0x14]
0x024ADB98: cmp      w0, w8
0x024ADB9C: csel     w8, w0, w8, lt
0x024ADBA0: str      w8, [sp, #0x14]
0x024ADBA4: b        #0x24adb24
0x024ADBA8: adrp     x8, #0x508a000
0x024ADBAC: ldr      x8, [x8, #0xce0]
0x024ADBB0: b        #0x24ad84c
0x024ADBB4: ldr      x28, [x19, #0xaf0]
0x024ADBB8: mov      x29, x28
~~~

### Function start 0x24ade74
Hits: [{"pc": "0x24ae028", "adrp": "0x24ae018", "target": "0x1192575", "label": "view_manager::ViewManager::ModifyEnemyInvisibleHeroPositionByTimeDynamic", "keywords": ["ModifyEnemyInvisibleHeroPositionByTimeDynamic", "ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x24ade74", "fde_end": "0x24ae674", "kind": "add", "reg": "x1"}, {"pc": "0x24ae2f8", "adrp": "0x24ae2ec", "target": "0x1192575", "label": "view_manager::ViewManager::ModifyEnemyInvisibleHeroPositionByTimeDynamic", "keywords": ["ModifyEnemyInvisibleHeroPositionByTimeDynamic", "ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x24ade74", "fde_end": "0x24ae674", "kind": "add", "reg": "x1"}, {"pc": "0x24ae420", "adrp": "0x24ae410", "target": "0x1192575", "label": "view_manager::ViewManager::ModifyEnemyInvisibleHeroPositionByTimeDynamic", "keywords": ["ModifyEnemyInvisibleHeroPositionByTimeDynamic", "ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x24ade74", "fde_end": "0x24ae674", "kind": "add", "reg": "x1"}, {"pc": "0x24ae430", "adrp": "0x24ae418", "target": "0x11d87a2", "label": "frame:%d main_hero:%d hero:%d, not visible duration(sec) = %d, dist = %d, last_dist = %d, enemy true location = (%d, %d), main_hero_location = (%d, %d), invisible_range:%d", "keywords": ["invisible"], "fde_start": "0x24ade74", "fde_end": "0x24ae674", "kind": "add", "reg": "x2"}, {"pc": "0x24ae56c", "adrp": "0x24ae55c", "target": "0x1192575", "label": "view_manager::ViewManager::ModifyEnemyInvisibleHeroPositionByTimeDynamic", "keywords": ["ModifyEnemyInvisibleHeroPositionByTimeDynamic", "ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x24ade74", "fde_end": "0x24ae674", "kind": "add", "reg": "x1"}, {"pc": "0x24ae574", "adrp": "0x24ae560", "target": "0x1185459", "label": "frame:%d camp:%d, main_hero:%d, modify emy_hero:%d to spring, frame_diff:%d, last_visible_dist:%d, dist:%d, invisible_range:%d", "keywords": ["invisible"], "fde_start": "0x24ade74", "fde_end": "0x24ae674", "kind": "add", "reg": "x2"}]
~~~asm
0x024ADE74: sub      sp, sp, #0xb0
0x024ADE78: stp      x29, x30, [sp, #0x50]
0x024ADE7C: stp      x28, x27, [sp, #0x60]
0x024ADE80: stp      x26, x25, [sp, #0x70]
0x024ADE84: stp      x24, x23, [sp, #0x80]
0x024ADE88: stp      x22, x21, [sp, #0x90]
0x024ADE8C: stp      x20, x19, [sp, #0xa0]
0x024ADE90: adrp     x8, #0x508a000
0x024ADE94: str      w4, [sp, #0x48]
0x024ADE98: mov      w23, w3
0x024ADE9C: mov      x20, x2
0x024ADEA0: mov      x21, x1
0x024ADEA4: mov      x22, x0
0x024ADEA8: ldr      x8, [x8, #0xd10]
0x024ADEAC: blr      x8
0x024ADEB0: ldr      w8, [x21]
0x024ADEB4: cmp      w8, #0x96
0x024ADEB8: mov      w8, #0xf
0x024ADEBC: csel     w8, w8, w23, lt
0x024ADEC0: cmp      w8, #0xe0f
0x024ADEC4: str      w8, [sp, #0x4c]
0x024ADEC8: b.gt     #0x24ae650
0x024ADECC: ldp      x23, x8, [x21, #0x68]
0x024ADED0: cmp      x23, x8
0x024ADED4: b.eq     #0x24ae650
0x024ADED8: add      x24, x22, #0x58
0x024ADEDC: add      x8, x20, #0xae0
0x024ADEE0: adrp     x26, #0x508a000
0x024ADEE4: adrp     x28, #0x508a000
0x024ADEE8: str      x8, [sp, #0x40]
0x024ADEEC: b        #0x24adf18
0x024ADEF0: adrp     x8, #0x508a000
0x024ADEF4: mov      x0, x22
0x024ADEF8: mov      x1, x23
0x024ADEFC: ldr      x8, [x8, #0xcb0]
0x024ADF00: blr      x8
0x024ADF04: adrp     x28, #0x508a000
0x024ADF08: ldr      x8, [x21, #0x70]
0x024ADF0C: add      x23, x23, #0x3f0
0x024ADF10: cmp      x23, x8
0x024ADF14: b.eq     #0x24ae650
0x024ADF18: ldr      w8, [x23, #0x18]
0x024ADF1C: ldr      w9, [x22, #0x18]
0x024ADF20: cmp      w8, w9
0x024ADF24: b.eq     #0x24adf08
0x024ADF28: ldr      x8, [x26, #0xc80]
0x024ADF2C: mov      x0, x22
0x024ADF30: mov      x1, x23
0x024ADF34: blr      x8
0x024ADF38: tbnz     w0, #0, #0x24adf08
0x024ADF3C: ldr      w8, [x23, #4]
0x024ADF40: cmp      w8, #0x74
0x024ADF44: b.eq     #0x24adf9c
0x024ADF48: cmp      w8, #0x99
0x024ADF4C: b.eq     #0x24adf9c
0x024ADF50: adrp     x8, #0x5180000
0x024ADF54: mov      w3, #0xe8fa
0x024ADF58: mov      x0, x22
0x024ADF5C: mov      x1, x21
0x024ADF60: mov      x2, x23
0x024ADF64: movk     w3, #0xd, lsl #16
0x024ADF68: ldr      x8, [x8, #0x68]
0x024ADF6C: blr      x8
0x024ADF70: tbnz     w0, #0, #0x24adf9c
0x024ADF74: adrp     x8, #0x5180000
0x024ADF78: mov      w9, #0xe8fa
0x024ADF7C: movk     w9, #0xd, lsl #16
0x024ADF80: mov      x0, x22
0x024ADF84: add      w3, w9, #1
0x024ADF88: mov      x1, x21
0x024ADF8C: ldr      x8, [x8, #0x68]
0x024ADF90: mov      x2, x23
0x024ADF94: blr      x8
0x024ADF98: tbz      w0, #0, #0x24adfb8
0x024ADF9C: ldr      x8, [x28, #0xc70]
0x024ADFA0: mov      x0, x22
0x024ADFA4: mov      x1, x23
0x024ADFA8: blr      x8
0x024ADFAC: tbz      w0, #0, #0x24adfb8
0x024ADFB0: ldrb     w8, [x23, #0x358]
0x024ADFB4: cbz      w8, #0x24adf08
0x024ADFB8: ldr      x8, [x22, #0x10]
0x024ADFBC: add      x29, x23, #0x20
0x024ADFC0: mov      x0, x22
0x024ADFC4: mov      x1, x29
0x024ADFC8: mov      w3, #1
0x024ADFCC: add      x2, x8, #0x20
0x024ADFD0: adrp     x8, #0x517f000
0x024ADFD4: ldr      x8, [x8, #0x388]
0x024ADFD8: blr      x8
0x024ADFDC: ldr      w8, [x23, #4]
0x024ADFE0: cmp      w8, #0xc4
0x024ADFE4: b.ne     #0x24ae044
0x024ADFE8: ldrb     w8, [x23, #0x358]
0x024ADFEC: cbz      w8, #0x24ae044
0x024ADFF0: mov      w25, w0
0x024ADFF4: cmp      w0, #0x1d
0x024ADFF8: b.gt     #0x24ae044
0x024ADFFC: ldr      x8, [x22, #0x10]
0x024AE000: ldrb     w8, [x8, #0x358]
0x024AE004: cbz      w8, #0x24ae044
0x024AE008: adrp     x8, #0x509c000
0x024AE00C: ldr      x8, [x8, #0x70]
0x024AE010: blr      x8
0x024AE014: ldr      x8, [x22, #0x10]
0x024AE018: adrp     x1, #0x1192000
0x024AE01C: adrp     x2, #0x11a5000
0x024AE020: ldr      w3, [x23, #4]
0x024AE024: ldrb     w4, [x23, #0x358]
0x024AE028: add      x1, x1, #0x575
0x024AE02C: ldr      w5, [x8, #4]
0x024AE030: add      x2, x2, #0x888
0x024AE034: ldrb     w6, [x8, #0x358]
0x024AE038: mov      w7, w25
0x024AE03C: bl       #0x2185854
0x024AE040: b        #0x24adf08
0x024AE044: ldr      x19, [x24]
0x024AE048: cbz      x19, #0x24ae214
0x024AE04C: ldr      w8, [x23, #8]
0x024AE050: mov      x9, x24
0x024AE054: mov      x10, x19
0x024AE058: ldr      w11, [x10, #0x1c]
0x024AE05C: cmp      w11, w8
0x024AE060: cset     w11, lt
0x024AE064: csel     x9, x9, x10, lt
0x024AE068: ldr      x10, [x10, w11, uxtw #3]
0x024AE06C: cbnz     x10, #0x24ae058
0x024AE070: cmp      x9, x24
0x024AE074: b.eq     #0x24ae214
0x024AE078: ldr      w9, [x9, #0x1c]
0x024AE07C: cmp      w8, w9
0x024AE080: b.lt     #0x24ae214
0x024AE084: mov      x27, x24
0x024AE088: b        #0x24ae09c
0x024AE08C: ldr      x9, [x19]
0x024AE090: mov      x27, x19
0x024AE094: cbz      x9, #0x24ae0bc
0x024AE098: mov      x19, x9
0x024AE09C: ldr      w9, [x19, #0x1c]
0x024AE0A0: cmp      w8, w9
0x024AE0A4: b.lt     #0x24ae08c
0x024AE0A8: cmp      w9, w8
0x024AE0AC: b.ge     #0x24ae0bc
0x024AE0B0: mov      x27, x19
0x024AE0B4: ldr      x9, [x27, #8]!
0x024AE0B8: cbnz     x9, #0x24ae098
0x024AE0BC: ldr      x25, [x27]
0x024AE0C0: cbnz     x25, #0x24ae114
0x024AE0C4: mov      w0, #0x28
0x024AE0C8: bl       #0x4b40050
0x024AE0CC: ldr      w8, [x23, #8]
0x024AE0D0: stp      xzr, xzr, [x0]
0x024AE0D4: str      x19, [x0, #0x10]
0x024AE0D8: mov      x25, x0
0x024AE0DC: stp      w8, wzr, [x0, #0x1c]
0x024AE0E0: str      x0, [x27]
0x024AE0E4: ldr      x8, [x22, #0x50]
0x024AE0E8: ldr      x8, [x8]
0x024AE0EC: cbz      x8, #0x24ae0fc
0x024AE0F0: str      x8, [x22, #0x50]
0x024AE0F4: ldr      x1, [x27]
0x024AE0F8: b        #0x24ae100
0x024AE0FC: mov      x1, x25
0x024AE100: ldr      x0, [x22, #0x58]
0x024AE104: bl       #0x2260c4c
0x024AE108: ldr      x8, [x22, #0x60]
0x024AE10C: add      x8, x8, #1
0x024AE110: str      x8, [x22, #0x60]
0x024AE114: ldr      w8, [x25, #0x20]
0x024AE118: cmp      w8, #1
0x024AE11C: b.lt     #0x24ae214
0x024AE120: ldr      x19, [x24]
0x024AE124: cbz      x19, #0x24ae16c
0x024AE128: ldr      w8, [x23, #8]
0x024AE12C: mov      x27, x24
0x024AE130: ldr      w9, [x19, #0x1c]
0x024AE134: cmp      w8, w9
0x024AE138: b.ge     #0x24ae150
0x024AE13C: ldr      x9, [x19]
0x024AE140: cbz      x9, #0x24ae1b4
0x024AE144: mov      x27, x19
0x024AE148: mov      x19, x9
0x024AE14C: b        #0x24ae130
0x024AE150: cmp      w9, w8
0x024AE154: b.ge     #0x24ae174
0x024AE158: mov      x27, x19
0x024AE15C: ldr      x9, [x27, #8]!
0x024AE160: cbz      x9, #0x24ae174
0x024AE164: mov      x19, x9
0x024AE168: b        #0x24ae130
0x024AE16C: mov      x19, x24
0x024AE170: mov      x27, x24
0x024AE174: ldr      x25, [x27]
0x024AE178: cbnz     x25, #0x24ae1dc
0x024AE17C: mov      w0, #0x28
0x024AE180: bl       #0x4b40050
0x024AE184: ldr      w8, [x23, #8]
0x024AE188: stp      xzr, xzr, [x0]
0x024AE18C: str      x19, [x0, #0x10]
0x024AE190: mov      x25, x0
0x024AE194: stp      w8, wzr, [x0, #0x1c]
0x024AE198: str      x0, [x27]
0x024AE19C: ldr      x8, [x22, #0x50]
0x024AE1A0: ldr      x8, [x8]
0x024AE1A4: cbz      x8, #0x24ae1c4
0x024AE1A8: str      x8, [x22, #0x50]
0x024AE1AC: ldr      x1, [x27]
0x024AE1B0: b        #0x24ae1c8
0x024AE1B4: mov      x27, x19
0x024AE1B8: ldr      x25, [x27]
0x024AE1BC: cbnz     x25, #0x24ae1dc
0x024AE1C0: b        #0x24ae17c
0x024AE1C4: mov      x1, x25
0x024AE1C8: ldr      x0, [x22, #0x58]
0x024AE1CC: bl       #0x2260c4c
0x024AE1D0: ldr      x8, [x22, #0x60]
0x024AE1D4: add      x8, x8, #1
0x024AE1D8: str      x8, [x22, #0x60]
0x024AE1DC: ldr      w8, [x25, #0x20]
0x024AE1E0: ldr      w9, [x22, #0x30]
0x024AE1E4: cmp      w8, w9
0x024AE1E8: b.ge     #0x24ae214
0x024AE1EC: adrp     x8, #0x508a000
0x024AE1F0: mov      x0, x22
0x024AE1F4: mov      x1, x21
0x024AE1F8: mov      x2, x23
0x024AE1FC: mov      w3, #0xc8
0x024AE200: mov      w4, #0x64
0x024AE204: ldr      x8, [x8, #0xd20]
0x024AE208: mov      w5, #0x5dc
0x024AE20C: blr      x8
0x024AE210: b        #0x24adf08
0x024AE214: ldr      x27, [x20, #0xaf0]
0x024AE218: cbz      x27, #0x24ae2e0
0x024AE21C: mov      x9, x27
0x024AE220: ldr      x28, [x9, #8]!
0x024AE224: cbz      x28, #0x24adf04
0x024AE228: ldr      w8, [x23, #4]
0x024AE22C: mov      x10, x9
0x024AE230: mov      x11, x28
~~~

### Function start 0x24ae864
Hits: [{"pc": "0x24aea90", "adrp": "0x24aea84", "target": "0x11ac0c5", "label": "mian_hero [%d-%d-%d] tgt_hero [%d-%d-%d] cur_frame %d, last_invisible_ingrass %d --> visible_ingrass less than 6 frame", "keywords": ["invisible"], "fde_start": "0x24ae864", "fde_end": "0x24aeac0", "kind": "add", "reg": "x2"}]
~~~asm
0x024AE864: sub      sp, sp, #0x80
0x024AE868: stp      x29, x30, [sp, #0x20]
0x024AE86C: stp      x28, x27, [sp, #0x30]
0x024AE870: stp      x26, x25, [sp, #0x40]
0x024AE874: stp      x24, x23, [sp, #0x50]
0x024AE878: stp      x22, x21, [sp, #0x60]
0x024AE87C: stp      x20, x19, [sp, #0x70]
0x024AE880: ldr      x24, [x3, #0xb38]
0x024AE884: cbz      x24, #0x24ae97c
0x024AE888: mov      x8, x24
0x024AE88C: ldr      x25, [x8, #8]!
0x024AE890: cbz      x25, #0x24ae97c
0x024AE894: mov      x21, x3
0x024AE898: mov      x20, x2
0x024AE89C: mov      x19, x1
0x024AE8A0: mov      x22, x0
0x024AE8A4: ldr      w26, [x2, #4]
0x024AE8A8: mov      x9, x8
0x024AE8AC: mov      x10, x25
0x024AE8B0: ldr      w11, [x10, #0x1c]
0x024AE8B4: cmp      w11, w26
0x024AE8B8: cset     w11, lt
0x024AE8BC: csel     x9, x9, x10, lt
0x024AE8C0: ldr      x10, [x10, w11, uxtw #3]
0x024AE8C4: cbnz     x10, #0x24ae8b0
0x024AE8C8: cmp      x9, x8
0x024AE8CC: b.eq     #0x24ae97c
0x024AE8D0: ldr      w8, [x9, #0x1c]
0x024AE8D4: cmp      w26, w8
0x024AE8D8: b.lt     #0x24ae97c
0x024AE8DC: add      x27, x24, #8
0x024AE8E0: b        #0x24ae8f4
0x024AE8E4: ldr      x8, [x25]
0x024AE8E8: mov      x27, x25
0x024AE8EC: cbz      x8, #0x24ae914
0x024AE8F0: mov      x25, x8
0x024AE8F4: ldr      w8, [x25, #0x1c]
0x024AE8F8: cmp      w26, w8
0x024AE8FC: b.lt     #0x24ae8e4
0x024AE900: cmp      w8, w26
0x024AE904: b.ge     #0x24ae914
0x024AE908: mov      x27, x25
0x024AE90C: ldr      x8, [x27, #8]!
0x024AE910: cbnz     x8, #0x24ae8f0
0x024AE914: ldr      x23, [x27]
0x024AE918: cbnz     x23, #0x24ae968
0x024AE91C: mov      w0, #0x28
0x024AE920: bl       #0x4b40050
0x024AE924: stp      w26, wzr, [x0, #0x1c]
0x024AE928: mov      x23, x0
0x024AE92C: stp      xzr, xzr, [x0]
0x024AE930: str      x25, [x0, #0x10]
0x024AE934: str      x0, [x27]
0x024AE938: ldr      x8, [x24]
0x024AE93C: ldr      x8, [x8]
0x024AE940: cbz      x8, #0x24ae950
0x024AE944: str      x8, [x24]
0x024AE948: ldr      x1, [x27]
0x024AE94C: b        #0x24ae954
0x024AE950: mov      x1, x23
0x024AE954: ldr      x0, [x24, #8]
0x024AE958: bl       #0x2260c4c
0x024AE95C: ldr      x8, [x24, #0x10]
0x024AE960: add      x8, x8, #1
0x024AE964: str      x8, [x24, #0x10]
0x024AE968: ldr      w8, [x23, #0x20]
0x024AE96C: ldr      w9, [x19]
0x024AE970: add      w8, w8, #6
0x024AE974: cmp      w8, w9
0x024AE978: b.ge     #0x24ae9a0
0x024AE97C: mov      w0, #1
0x024AE980: ldp      x20, x19, [sp, #0x70]
0x024AE984: ldp      x22, x21, [sp, #0x60]
0x024AE988: ldp      x24, x23, [sp, #0x50]
0x024AE98C: ldp      x26, x25, [sp, #0x40]
0x024AE990: ldp      x28, x27, [sp, #0x30]
0x024AE994: ldp      x29, x30, [sp, #0x20]
0x024AE998: add      sp, sp, #0x80
0x024AE99C: ret      
0x024AE9A0: adrp     x8, #0x509c000
0x024AE9A4: ldr      x8, [x8, #0x70]
0x024AE9A8: blr      x8
0x024AE9AC: ldr      x27, [x21, #0xb38]
0x024AE9B0: ldr      x8, [x22, #0x10]
0x024AE9B4: ldr      w25, [x22, #0x18]
0x024AE9B8: mov      x28, x27
0x024AE9BC: ldr      w21, [x20, #0x18]
0x024AE9C0: ldp      w26, w24, [x8, #4]
0x024AE9C4: ldr      w22, [x20, #4]
0x024AE9C8: ldr      x29, [x28, #8]!
0x024AE9CC: cbz      x29, #0x24aea10
0x024AE9D0: add      x28, x27, #8
0x024AE9D4: ldr      w8, [x29, #0x1c]
0x024AE9D8: cmp      w22, w8
0x024AE9DC: b.ge     #0x24ae9f4
0x024AE9E0: ldr      x8, [x29]
0x024AE9E4: cbz      x8, #0x24aea18
0x024AE9E8: mov      x28, x29
0x024AE9EC: mov      x29, x8
0x024AE9F0: b        #0x24ae9d4
0x024AE9F4: cmp      w8, w22
0x024AE9F8: b.ge     #0x24aea1c
0x024AE9FC: mov      x28, x29
0x024AEA00: ldr      x8, [x28, #8]!
0x024AEA04: cbz      x8, #0x24aea1c
0x024AEA08: mov      x29, x8
0x024AEA0C: b        #0x24ae9d4
0x024AEA10: mov      x29, x28
0x024AEA14: b        #0x24aea1c
0x024AEA18: mov      x28, x29
0x024AEA1C: ldr      w23, [x20, #8]
0x024AEA20: ldr      x20, [x28]
0x024AEA24: ldr      w19, [x19]
0x024AEA28: cbnz     x20, #0x24aea80
0x024AEA2C: str      x0, [sp, #0x18]
0x024AEA30: mov      w0, #0x28
0x024AEA34: bl       #0x4b40050
0x024AEA38: stp      w22, wzr, [x0, #0x1c]
0x024AEA3C: mov      x20, x0
0x024AEA40: stp      xzr, xzr, [x0]
0x024AEA44: str      x29, [x0, #0x10]
0x024AEA48: str      x0, [x28]
0x024AEA4C: ldr      x8, [x27]
0x024AEA50: ldr      x8, [x8]
0x024AEA54: cbz      x8, #0x24aea64
0x024AEA58: str      x8, [x27]
0x024AEA5C: ldr      x1, [x28]
0x024AEA60: b        #0x24aea68
0x024AEA64: mov      x1, x20
0x024AEA68: ldr      x0, [x27, #8]
0x024AEA6C: bl       #0x2260c4c
0x024AEA70: ldr      x8, [x27, #0x10]
0x024AEA74: ldr      x0, [sp, #0x18]
0x024AEA78: add      x8, x8, #1
0x024AEA7C: str      x8, [x27, #0x10]
0x024AEA80: adrp     x1, #0x11cb000
0x024AEA84: adrp     x2, #0x11ac000
0x024AEA88: ldr      w8, [x20, #0x20]
0x024AEA8C: add      x1, x1, #0x16f
0x024AEA90: add      x2, x2, #0xc5
0x024AEA94: mov      w3, w25
0x024AEA98: mov      w4, w26
0x024AEA9C: mov      w5, w24
0x024AEAA0: mov      w6, w21
0x024AEAA4: mov      w7, w22
0x024AEAA8: str      w8, [sp, #0x10]
0x024AEAAC: str      w19, [sp, #8]
0x024AEAB0: str      w23, [sp]
0x024AEAB4: bl       #0x2185854
0x024AEAB8: mov      w0, wzr
0x024AEABC: b        #0x24ae980
~~~

### Function start 0x24aed38
Hits: [{"pc": "0x24aedbc", "adrp": "0x24aedac", "target": "0x11b25de", "label": "ake use skill3, invisible, real_location = (%d,%d), modify to (%d,%d)", "keywords": ["real_location", "invisible"], "fde_start": "0x24aed38", "fde_end": "0x24aee60", "kind": "add", "reg": "x2"}]
~~~asm
0x024AED38: str      x30, [sp, #-0x40]!
0x024AED3C: stp      x24, x23, [sp, #0x10]
0x024AED40: stp      x22, x21, [sp, #0x20]
0x024AED44: stp      x20, x19, [sp, #0x30]
0x024AED48: mov      x20, x1
0x024AED4C: ldr      x8, [x2, #0xaf8]
0x024AED50: cbz      x8, #0x24aede0
0x024AED54: ldr      w9, [x20]
0x024AED58: adrp     x11, #0x5089000
0x024AED5C: ldr      w10, [x2, #0xefc]
0x024AED60: mov      x21, x0
0x024AED64: add      x1, sp, #0xc
0x024AED68: mov      x0, x8
0x024AED6C: mov      w23, w4
0x024AED70: mov      x19, x3
0x024AED74: sub      w9, w9, w10
0x024AED78: ldr      x10, [x11, #0x210]
0x024AED7C: mov      x24, x2
0x024AED80: str      w9, [sp, #0xc]
0x024AED84: blr      x10
0x024AED88: ldr      x8, [x24, #0xaf8]
0x024AED8C: add      x8, x8, #8
0x024AED90: cmp      x8, x0
0x024AED94: b.eq     #0x24aee14
0x024AED98: adrp     x8, #0x509c000
0x024AED9C: mov      x22, x0
0x024AEDA0: ldr      x8, [x8, #0x70]
0x024AEDA4: blr      x8
0x024AEDA8: adrp     x1, #0x11f9000
0x024AEDAC: adrp     x2, #0x11b2000
0x024AEDB0: ldr      w3, [x19, #0x20]
0x024AEDB4: add      x1, x1, #0xac0
0x024AEDB8: ldr      w4, [x19, #0x28]
0x024AEDBC: add      x2, x2, #0x5de
0x024AEDC0: ldr      w5, [x22, #0x20]
0x024AEDC4: ldr      w6, [x22, #0x28]
0x024AEDC8: bl       #0x2185854
0x024AEDCC: ldr      w8, [x22, #0x28]
0x024AEDD0: ldr      x9, [x22, #0x20]
0x024AEDD4: str      w8, [x19, #0x28]
0x024AEDD8: str      x9, [x19, #0x20]
0x024AEDDC: b        #0x24aee4c
0x024AEDE0: adrp     x8, #0x509c000
0x024AEDE4: ldr      x8, [x8, #0x70]
0x024AEDE8: blr      x8
0x024AEDEC: ldr      w3, [x20]
0x024AEDF0: adrp     x1, #0x11f9000
0x024AEDF4: ldp      x20, x19, [sp, #0x30]
0x024AEDF8: adrp     x2, #0x11be000
0x024AEDFC: add      x1, x1, #0xac0
0x024AEE00: ldp      x22, x21, [sp, #0x20]
0x024AEE04: add      x2, x2, #0xac3
0x024AEE08: ldp      x24, x23, [sp, #0x10]
0x024AEE0C: ldr      x30, [sp], #0x40
0x024AEE10: b        #0x2185854
0x024AEE14: cmp      w23, #0x63
0x024AEE18: b.gt     #0x24aee38
0x024AEE1C: adrp     x8, #0x508a000
0x024AEE20: mov      x0, x21
0x024AEE24: mov      x1, x20
0x024AEE28: mov      x2, x19
0x024AEE2C: ldr      x8, [x8, #0xd00]
0x024AEE30: blr      x8
0x024AEE34: b        #0x24aee4c
0x024AEE38: adrp     x8, #0x508a000
0x024AEE3C: mov      x0, x21
0x024AEE40: mov      x1, x19
0x024AEE44: ldr      x8, [x8, #0xcb0]
0x024AEE48: blr      x8
0x024AEE4C: ldp      x20, x19, [sp, #0x30]
0x024AEE50: ldp      x22, x21, [sp, #0x20]
0x024AEE54: ldp      x24, x23, [sp, #0x10]
0x024AEE58: ldr      x30, [sp], #0x40
0x024AEE5C: ret      
~~~

### Function start 0x24aee60
Hits: [{"pc": "0x24aef08", "adrp": "0x24aeef8", "target": "0x11925be", "label": "yindao, cid:%d, invisible, real_location = (%d,%d), modify to (%d,%d)", "keywords": ["real_location", "invisible"], "fde_start": "0x24aee60", "fde_end": "0x24aefb8", "kind": "add", "reg": "x2"}]
~~~asm
0x024AEE60: sub      sp, sp, #0x50
0x024AEE64: stp      x30, x25, [sp, #0x10]
0x024AEE68: stp      x24, x23, [sp, #0x20]
0x024AEE6C: stp      x22, x21, [sp, #0x30]
0x024AEE70: stp      x20, x19, [sp, #0x40]
0x024AEE74: mov      x20, x1
0x024AEE78: ldr      x25, [x2, #0xb00]
0x024AEE7C: cbz      x25, #0x24aef30
0x024AEE80: adrp     x8, #0x5088000
0x024AEE84: mov      x21, x0
0x024AEE88: add      x1, x3, #8
0x024AEE8C: mov      x0, x25
0x024AEE90: mov      w22, w4
0x024AEE94: mov      x19, x3
0x024AEE98: ldr      x8, [x8, #0xf18]
0x024AEE9C: mov      x23, x2
0x024AEEA0: blr      x8
0x024AEEA4: add      x8, x25, #8
0x024AEEA8: cmp      x8, x0
0x024AEEAC: b.eq     #0x24aef68
0x024AEEB0: ldr      w8, [x20]
0x024AEEB4: adrp     x10, #0x5089000
0x024AEEB8: ldr      w9, [x23, #0xefc]
0x024AEEBC: mov      x24, x0
0x024AEEC0: add      x0, x0, #0x28
0x024AEEC4: add      x1, sp, #0xc
0x024AEEC8: sub      w8, w8, w9
0x024AEECC: ldr      x9, [x10, #0x210]
0x024AEED0: str      w8, [sp, #0xc]
0x024AEED4: blr      x9
0x024AEED8: add      x8, x24, #0x30
0x024AEEDC: cmp      x8, x0
0x024AEEE0: b.eq     #0x24aef68
0x024AEEE4: adrp     x8, #0x509c000
0x024AEEE8: mov      x23, x0
0x024AEEEC: ldr      x8, [x8, #0x70]
0x024AEEF0: blr      x8
0x024AEEF4: adrp     x1, #0x11cb000
0x024AEEF8: adrp     x2, #0x1192000
0x024AEEFC: ldr      w3, [x19, #4]
0x024AEF00: add      x1, x1, #0x1a3
0x024AEF04: ldr      w4, [x19, #0x20]
0x024AEF08: add      x2, x2, #0x5be
0x024AEF0C: ldr      w5, [x19, #0x28]
0x024AEF10: ldr      w6, [x23, #0x20]
0x024AEF14: ldr      w7, [x23, #0x28]
0x024AEF18: bl       #0x2185854
0x024AEF1C: ldr      w8, [x23, #0x28]
0x024AEF20: ldr      x9, [x23, #0x20]
0x024AEF24: str      w8, [x19, #0x28]
0x024AEF28: str      x9, [x19, #0x20]
0x024AEF2C: b        #0x24aefa0
0x024AEF30: adrp     x8, #0x509c000
0x024AEF34: ldr      x8, [x8, #0x70]
0x024AEF38: blr      x8
0x024AEF3C: ldr      w3, [x20]
0x024AEF40: adrp     x1, #0x11cb000
0x024AEF44: ldp      x20, x19, [sp, #0x40]
0x024AEF48: adrp     x2, #0x1185000
0x024AEF4C: add      x1, x1, #0x1a3
0x024AEF50: ldp      x22, x21, [sp, #0x30]
0x024AEF54: add      x2, x2, #0x4d8
0x024AEF58: ldp      x24, x23, [sp, #0x20]
0x024AEF5C: ldp      x30, x25, [sp, #0x10]
0x024AEF60: add      sp, sp, #0x50
0x024AEF64: b        #0x2185854
0x024AEF68: cmp      w22, #0x63
0x024AEF6C: b.gt     #0x24aef8c
0x024AEF70: adrp     x8, #0x508a000
0x024AEF74: mov      x0, x21
0x024AEF78: mov      x1, x20
0x024AEF7C: mov      x2, x19
0x024AEF80: ldr      x8, [x8, #0xd00]
0x024AEF84: blr      x8
0x024AEF88: b        #0x24aefa0
0x024AEF8C: adrp     x8, #0x508a000
0x024AEF90: mov      x0, x21
0x024AEF94: mov      x1, x19
0x024AEF98: ldr      x8, [x8, #0xcb0]
0x024AEF9C: blr      x8
0x024AEFA0: ldp      x20, x19, [sp, #0x40]
0x024AEFA4: ldp      x22, x21, [sp, #0x30]
0x024AEFA8: ldp      x24, x23, [sp, #0x20]
0x024AEFAC: ldp      x30, x25, [sp, #0x10]
0x024AEFB0: add      sp, sp, #0x50
0x024AEFB4: ret      
~~~

### Function start 0x24aefb8
Hits: [{"pc": "0x24af05c", "adrp": "0x24af058", "target": "0x11d1b38", "label": "view_manager::ViewManager::ModifyHeroPositionWhenNearby", "keywords": ["HeroPosition"], "fde_start": "0x24aefb8", "fde_end": "0x24af0f8", "kind": "add", "reg": "x21"}]
~~~asm
0x024AEFB8: stp      d9, d8, [sp, #-0x40]!
0x024AEFBC: str      x30, [sp, #0x10]
0x024AEFC0: stp      x22, x21, [sp, #0x20]
0x024AEFC4: stp      x20, x19, [sp, #0x30]
0x024AEFC8: mov      x20, x0
0x024AEFCC: mov      x0, xzr
0x024AEFD0: mov      x19, x2
0x024AEFD4: bl       #0x4b40500
0x024AEFD8: bl       #0x4b40380
0x024AEFDC: bl       #0x4b40370
0x024AEFE0: mov      w21, #0x851f
0x024AEFE4: mov      w22, #0x32
0x024AEFE8: movk     w21, #0x51eb, lsl #16
0x024AEFEC: smull    x8, w0, w21
0x024AEFF0: lsr      x9, x8, #0x20
0x024AEFF4: lsr      x8, x8, #0x3f
0x024AEFF8: add      w8, w8, w9, asr #4
0x024AEFFC: mov      w9, #0x42c80000
0x024AF000: msub     w8, w8, w22, w0
0x024AF004: mov      x0, xzr
0x024AF008: fmov     s8, w9
0x024AF00C: sub      w8, w8, #0x19
0x024AF010: scvtf    s0, w8
0x024AF014: fdiv     s9, s0, s8
0x024AF018: bl       #0x4b40500
0x024AF01C: add      w0, w0, #1
0x024AF020: bl       #0x4b40380
0x024AF024: bl       #0x4b40370
0x024AF028: smull    x8, w0, w21
0x024AF02C: lsr      x9, x8, #0x20
0x024AF030: lsr      x8, x8, #0x3f
0x024AF034: add      w8, w8, w9, asr #4
0x024AF038: msub     w8, w8, w22, w0
0x024AF03C: adrp     x22, #0x509c000
0x024AF040: sub      w8, w8, #0x19
0x024AF044: scvtf    s0, w8
0x024AF048: ldr      x8, [x22, #0x70]
0x024AF04C: fdiv     s8, s0, s8
0x024AF050: blr      x8
0x024AF054: ldr      x8, [x20, #0x10]
0x024AF058: adrp     x21, #0x11d1000
0x024AF05C: add      x21, x21, #0xb38
0x024AF060: adrp     x2, #0x1198000
0x024AF064: ldr      w3, [x19, #4]
0x024AF068: add      x2, x2, #0x41c
0x024AF06C: ldr      w4, [x19, #0x20]
0x024AF070: mov      x1, x21
0x024AF074: ldr      w5, [x19, #0x28]
0x024AF078: ldr      w6, [x8, #0x20]
0x024AF07C: ldr      w7, [x8, #0x28]
0x024AF080: bl       #0x2185854
0x024AF084: ldr      s0, [x19, #0x20]
0x024AF088: mov      w8, #0xe000
0x024AF08C: ldr      s1, [x19, #0x28]
0x024AF090: movk     w8, #0x460a, lsl #16
0x024AF094: ldr      x10, [x22, #0x70]
0x024AF098: scvtf    s0, s0
0x024AF09C: scvtf    s1, s1
0x024AF0A0: fmov     s2, w8
0x024AF0A4: fmadd    s0, s9, s2, s0
0x024AF0A8: fmadd    s1, s8, s2, s1
0x024AF0AC: fcvtzs   w8, s0
0x024AF0B0: fcvtzs   w9, s1
0x024AF0B4: str      w8, [x19, #0x20]
0x024AF0B8: str      w9, [x19, #0x28]
0x024AF0BC: blr      x10
0x024AF0C0: ldr      x8, [x20, #0x10]
0x024AF0C4: mov      x1, x21
0x024AF0C8: ldr      w3, [x19, #4]
0x024AF0CC: adrp     x2, #0x11c5000
0x024AF0D0: ldr      w4, [x19, #0x20]
0x024AF0D4: add      x2, x2, #0x1be
0x024AF0D8: ldr      w5, [x19, #0x28]
0x024AF0DC: ldp      x20, x19, [sp, #0x30]
0x024AF0E0: ldp      x22, x21, [sp, #0x20]
0x024AF0E4: ldr      w6, [x8, #0x20]
0x024AF0E8: ldr      w7, [x8, #0x28]
0x024AF0EC: ldr      x30, [sp, #0x10]
0x024AF0F0: ldp      d9, d8, [sp], #0x40
0x024AF0F4: b        #0x2185854
~~~

### Function start 0x25543d0
Hits: [{"pc": "0x2555a54", "adrp": "0x2555a4c", "target": "0x11ec6c2", "label": "use_invisible_to_visible_delay_rule", "keywords": ["invisible"], "fde_start": "0x25543d0", "fde_end": "0x2556400", "kind": "add", "reg": "x10"}, {"pc": "0x2555b64", "adrp": "0x2555b5c", "target": "0x11b8e93", "label": "invisible_to_visible_delay", "keywords": ["invisible"], "fde_start": "0x25543d0", "fde_end": "0x2556400", "kind": "add", "reg": "x9"}, {"pc": "0x2555be0", "adrp": "0x2555bd8", "target": "0x119ed3d", "label": "invisible_to_visible_delta", "keywords": ["invisible"], "fde_start": "0x25543d0", "fde_end": "0x2556400", "kind": "add", "reg": "x8"}]
~~~asm
0x025543D0: sub      sp, sp, #0x170
0x025543D4: stp      x29, x30, [sp, #0x110]
0x025543D8: stp      x28, x27, [sp, #0x120]
0x025543DC: stp      x26, x25, [sp, #0x130]
0x025543E0: stp      x24, x23, [sp, #0x140]
0x025543E4: stp      x22, x21, [sp, #0x150]
0x025543E8: stp      x20, x19, [sp, #0x160]
0x025543EC: mov      x19, x0
0x025543F0: mov      x22, x1
0x025543F4: add      x0, x0, #0x170
0x025543F8: add      x20, x19, #0x178
0x025543FC: ldr      x1, [x19, #0x178]
0x02554400: bl       #0x223f158
0x02554404: adrp     x8, #0x4ff3000
0x02554408: str      xzr, [x19, #0x180]
0x0255440C: ldr      x8, [x8, #0x1b8]
0x02554410: stp      x20, xzr, [x19, #0x170]
0x02554414: ldrb     w9, [x22]
0x02554418: ldr      x10, [x22, #8]
0x0255441C: ldr      x24, [x8]
0x02554420: lsr      x8, x9, #1
0x02554424: tst      w9, #1
0x02554428: csel     x8, x8, x10, eq
0x0255442C: cbz      x24, #0x25561b4
0x02554430: cmp      x8, x24
0x02554434: csel     x8, x8, x24, lo
0x02554438: cbz      x8, #0x25544e4
0x0255443C: adrp     x8, #0x5179000
0x02554440: mov      w9, #0x3d02
0x02554444: add      x25, x19, #0x20
0x02554448: add      x0, x19, #0x18
0x0255444C: strb     wzr, [sp, #0xe2]
0x02554450: ldr      x8, [x8, #0xb20]
0x02554454: strh     w9, [sp, #0xe0]
0x02554458: add      x2, sp, #0xe0
0x0255445C: mov      x1, x22
0x02554460: mov      x3, x25
0x02554464: str      x0, [sp, #0x70]
0x02554468: blr      x8
0x0255446C: mov      w20, w0
0x02554470: ldrb     w8, [sp, #0xe0]
0x02554474: tbz      w8, #0, #0x2554480
0x02554478: ldr      x0, [sp, #0xf0]
0x0255447C: bl       #0x4b3fb60
0x02554480: tbz      w20, #0, #0x2554524
0x02554484: adrp     x10, #0x1158000
0x02554488: mov      w9, #0x696c
0x0255448C: add      x10, x10, #0xd51
0x02554490: mov      w8, #0x18
0x02554494: movk     w9, #0x7473, lsl #16
0x02554498: add      x1, sp, #0xe0
0x0255449C: mov      x0, x25
0x025544A0: strb     wzr, [sp, #0xed]
0x025544A4: ldr      x10, [x10]
0x025544A8: strb     w8, [sp, #0xe0]
0x025544AC: stur     w9, [sp, #0xe9]
0x025544B0: stur     x10, [sp, #0xe1]
0x025544B4: bl       #0x227e510
0x025544B8: add      x26, x19, #0x28
0x025544BC: cmp      x26, x0
0x025544C0: b.eq     #0x2554504
0x025544C4: mov      x8, x0
0x025544C8: ldrb     w9, [x8, #0x38]!
0x025544CC: tbnz     w9, #0, #0x255454c
0x025544D0: ldr      q0, [x8]
0x025544D4: ldr      x8, [x8, #0x10]
0x025544D8: str      q0, [sp, #0xc0]
0x025544DC: str      x8, [sp, #0xd0]
0x025544E0: b        #0x255459c
0x025544E4: adrp     x8, #0x509c000
0x025544E8: ldr      x8, [x8, #0x70]
0x025544EC: blr      x8
0x025544F0: adrp     x1, #0x11d8000
0x025544F4: adrp     x2, #0x114b000
0x025544F8: add      x1, x1, #0xbce
0x025544FC: add      x2, x2, #0xcad
0x02554500: b        #0x2554520
0x02554504: adrp     x8, #0x509c000
0x02554508: ldr      x8, [x8, #0x70]
0x0255450C: blr      x8
0x02554510: adrp     x1, #0x11d8000
0x02554514: adrp     x2, #0x1158000
0x02554518: add      x1, x1, #0xbce
0x0255451C: add      x2, x2, #0xd51
0x02554520: bl       #0x2185854
0x02554524: mov      w20, wzr
0x02554528: mov      w0, w20
0x0255452C: ldp      x20, x19, [sp, #0x160]
0x02554530: ldp      x22, x21, [sp, #0x150]
0x02554534: ldp      x24, x23, [sp, #0x140]
0x02554538: ldp      x26, x25, [sp, #0x130]
0x0255453C: ldp      x28, x27, [sp, #0x120]
0x02554540: ldp      x29, x30, [sp, #0x110]
0x02554544: add      sp, sp, #0x170
0x02554548: ret      
0x0255454C: ldp      x23, x20, [x0, #0x40]
0x02554550: cmp      x23, #0x16
0x02554554: b.hi     #0x255456c
0x02554558: lsl      w9, w23, #1
0x0255455C: add      x8, sp, #0xc0
0x02554560: orr      x0, x8, #1
0x02554564: strb     w9, [sp, #0xc0]
0x02554568: b        #0x2554590
0x0255456C: cmn      x23, #0x10
0x02554570: b.hs     #0x25561e0
0x02554574: add      x8, x23, #0x10
0x02554578: and      x21, x8, #0xfffffffffffffff0
0x0255457C: mov      x0, x21
0x02554580: bl       #0x4b40050
0x02554584: orr      x8, x21, #1
0x02554588: stp      x23, x0, [sp, #0xc8]
0x0255458C: str      x8, [sp, #0xc0]
0x02554590: add      x2, x23, #1
0x02554594: mov      x1, x20
0x02554598: bl       #0x4b405c0
0x0255459C: adrp     x9, #0x5179000
0x025545A0: mov      w8, #0x3b02
0x025545A4: stp      xzr, xzr, [sp, #0xa8]
0x025545A8: str      xzr, [sp, #0xb8]
0x025545AC: ldr      x9, [x9, #0xb40]
0x025545B0: strh     w8, [sp, #0xe0]
0x025545B4: strb     wzr, [sp, #0xe2]
0x025545B8: add      x1, sp, #0xc0
0x025545BC: add      x2, sp, #0xa8
0x025545C0: add      x3, sp, #0xe0
0x025545C4: ldr      x0, [sp, #0x70]
0x025545C8: blr      x9
0x025545CC: ldrb     w8, [sp, #0xe0]
0x025545D0: str      x25, [sp, #0x10]
0x025545D4: tbz      w8, #0, #0x25545e0
0x025545D8: ldr      x0, [sp, #0xf0]
0x025545DC: bl       #0x4b3fb60
0x025545E0: ldp      x23, x8, [sp, #0xa8]
0x025545E4: str      x26, [sp, #0x18]
0x025545E8: cmp      x23, x8
0x025545EC: b.eq     #0x2554d54
0x025545F0: add      x9, x19, #0xd8
0x025545F4: add      x8, x19, #0xf0
0x025545F8: mov      w28, #1
0x025545FC: stp      x9, x8, [sp, #0x58]
0x02554600: add      x8, sp, #0x90
0x02554604: orr      x29, x8, #1
0x02554608: b        #0x2554634
0x0255460C: ldr      x9, [sp, #0xf0]
0x02554610: add      x10, x8, #0x18
0x02554614: ldr      q0, [sp, #0xe0]
0x02554618: str      x9, [x8, #0x10]
0x0255461C: str      q0, [x8]
0x02554620: str      x10, [x19, #0xf8]
0x02554624: ldr      x8, [sp, #0xb0]
0x02554628: add      x23, x23, #0x18
0x0255462C: cmp      x23, x8
0x02554630: b.eq     #0x2554d54
0x02554634: ldp      x26, x20, [x23, #8]
0x02554638: ldrb     w21, [x23]
0x0255463C: tst      w21, #1
0x02554640: lsr      x8, x21, #1
0x02554644: csinc    x27, x20, x23, ne
0x02554648: csel     x2, x8, x26, eq
0x0255464C: add      x25, x27, x2
0x02554650: cmp      x2, #1
0x02554654: b.lt     #0x2554684
0x02554658: mov      x0, x27
0x0255465C: mov      w1, #0x3a
0x02554660: bl       #0x4b400e0
0x02554664: cbz      x0, #0x2554684
0x02554668: ldrb     w8, [x0]
0x0255466C: cmp      w8, #0x3a
0x02554670: b.eq     #0x2554688
0x02554674: add      x0, x0, #1
0x02554678: sub      x2, x25, x0
0x0255467C: cmp      x2, #0
0x02554680: b.gt     #0x255465c
0x02554684: mov      x0, x25
0x02554688: sub      x8, x0, x27
0x0255468C: cmp      x0, x25
0x02554690: csinv    x8, x8, xzr, ne
0x02554694: cmp      x8, x24
0x02554698: b.ne     #0x25546c0
0x0255469C: ldp      x27, x8, [x19, #0xe0]
0x025546A0: cmp      x27, x8
0x025546A4: b.eq     #0x2554744
0x025546A8: tbnz     w21, #0, #0x2554754
0x025546AC: ldr      x8, [x23, #0x10]
0x025546B0: ldr      q0, [x23]
0x025546B4: str      x8, [x27, #0x10]
0x025546B8: str      q0, [x27]
0x025546BC: b        #0x25548ec
0x025546C0: adrp     x8, #0x5179000
0x025546C4: mov      w9, #0x3a02
0x025546C8: stp      xzr, xzr, [sp, #0xe0]
0x025546CC: str      xzr, [sp, #0xf0]
0x025546D0: ldr      x8, [x8, #0xb40]
0x025546D4: strh     w9, [sp, #0x90]
0x025546D8: strb     wzr, [sp, #0x92]
0x025546DC: add      x2, sp, #0xe0
0x025546E0: add      x3, sp, #0x90
0x025546E4: ldr      x0, [sp, #0x70]
0x025546E8: mov      x1, x23
0x025546EC: blr      x8
0x025546F0: ldrb     w8, [sp, #0x90]
0x025546F4: tbz      w8, #0, #0x2554700
0x025546F8: ldr      x0, [sp, #0xa0]
0x025546FC: bl       #0x4b3fb60
0x02554700: ldr      x20, [sp, #0xe0]
0x02554704: ldrb     w8, [x20]
0x02554708: tbnz     w8, #0, #0x2554724
0x0255470C: ldr      q0, [x20]
0x02554710: ldr      x8, [x20, #0x10]
0x02554714: str      q0, [sp, #0x90]
0x02554718: ldrb     w26, [sp, #0x90]
0x0255471C: str      x8, [sp, #0xa0]
0x02554720: b        #0x25547a0
0x02554724: ldp      x25, x21, [x20, #8]
0x02554728: cmp      x25, #0x16
0x0255472C: b.hi     #0x255476c
0x02554730: and      w8, w25, #0xff
0x02554734: mov      x0, x29
0x02554738: lsl      w26, w8, #1
0x0255473C: strb     w26, [sp, #0x90]
0x02554740: b        #0x2554794
0x02554744: ldr      x0, [sp, #0x58]
0x02554748: mov      x1, x23
0x0255474C: bl       #0x25c84b4
0x02554750: b        #0x25548f4
0x02554754: cmp      x26, #0x16
0x02554758: b.hi     #0x25548bc
0x0255475C: lsl      w8, w26, #1
0x02554760: mov      x0, x27
0x02554764: strb     w8, [x0], #1
0x02554768: b        #0x25548e0
0x0255476C: cmn      x25, #0x10
0x02554770: b.hs     #0x25561b8
0x02554774: add      x8, x25, #0x10
0x02554778: and      x26, x8, #0xfffffffffffffff0
0x0255477C: mov      x0, x26
0x02554780: bl       #0x4b40050
0x02554784: orr      x8, x26, #1
0x02554788: stp      x25, x0, [sp, #0x98]
0x0255478C: and      w26, w8, #0xff
~~~

### Function start 0x2556400
Hits: [{"pc": "0x255686c", "adrp": "0x2556864", "target": "0x11f3691", "label": "m_enable_invisible_visible_rule right hand case 2", "keywords": ["invisible"], "fde_start": "0x2556400", "fde_end": "0x25572c8", "kind": "add", "reg": "x2"}, {"pc": "0x25568ac", "adrp": "0x25568a4", "target": "0x114bcfd", "label": "invisible_visible_rule_case2", "keywords": ["invisible"], "fde_start": "0x2556400", "fde_end": "0x25572c8", "kind": "add", "reg": "x1"}, {"pc": "0x25568f8", "adrp": "0x25568f0", "target": "0x11def93", "label": "m_enable_invisible_visible_rule right hand", "keywords": ["invisible"], "fde_start": "0x2556400", "fde_end": "0x25572c8", "kind": "add", "reg": "x2"}, {"pc": "0x2556938", "adrp": "0x2556930", "target": "0x11d1fed", "label": "invisible_visible_rule_case1", "keywords": ["invisible"], "fde_start": "0x2556400", "fde_end": "0x25572c8", "kind": "add", "reg": "x1"}]
~~~asm
0x02556400: sub      sp, sp, #0x100
0x02556404: stp      x29, x30, [sp, #0xa0]
0x02556408: stp      x28, x27, [sp, #0xb0]
0x0255640C: stp      x26, x25, [sp, #0xc0]
0x02556410: stp      x24, x23, [sp, #0xd0]
0x02556414: stp      x22, x21, [sp, #0xe0]
0x02556418: stp      x20, x19, [sp, #0xf0]
0x0255641C: ldp      x9, x8, [x0]
0x02556420: cmp      x8, x9
0x02556424: b.eq     #0x2556e30
0x02556428: adrp     x8, #0x517f000
0x0255642C: mov      x21, x0
0x02556430: add      x0, x0, #0xcc
0x02556434: mov      x19, x2
0x02556438: mov      x20, x1
0x0255643C: strb     wzr, [x2, #0xa37]
0x02556440: ldr      x8, [x8, #0x748]
0x02556444: blr      x8
0x02556448: adrp     x8, #0x508c000
0x0255644C: mov      w24, w0
0x02556450: mov      x0, x21
0x02556454: mov      x1, x20
0x02556458: ldr      x26, [x20, #0x68]
0x0255645C: ldr      x8, [x8, #0x550]
0x02556460: blr      x8
0x02556464: adrp     x8, #0x508c000
0x02556468: mov      x0, x21
0x0255646C: mov      x1, x20
0x02556470: mov      x2, x19
0x02556474: ldr      x8, [x8, #0x5b0]
0x02556478: blr      x8
0x0255647C: ldrb     w8, [x19, #0xa36]
0x02556480: adrp     x28, #0x509c000
0x02556484: cbz      w8, #0x2556d58
0x02556488: mov      w8, #1
0x0255648C: strb     w8, [x19, #0x690]
0x02556490: ldrsw    x22, [x19, #0xb8]
0x02556494: ldr      x8, [x21]
0x02556498: ldr      x0, [x8, x22, lsl #3]
0x0255649C: ldr      x8, [x0]
0x025564A0: ldr      x8, [x8, #0x20]
0x025564A4: blr      x8
0x025564A8: ldr      x8, [x28, #0x70]
0x025564AC: blr      x8
0x025564B0: adrp     x1, #0x1185000
0x025564B4: adrp     x2, #0x11b2000
0x025564B8: add      x1, x1, #0x91f
0x025564BC: add      x2, x2, #0xc87
0x025564C0: mov      w3, w22
0x025564C4: bl       #0x2185854
0x025564C8: ldrb     w8, [x19, #0x690]
0x025564CC: cbz      w8, #0x2556e1c
0x025564D0: adrp     x8, #0x508c000
0x025564D4: mov      w9, #1
0x025564D8: ldr      w1, [x19, #0x18]
0x025564DC: mov      x0, x21
0x025564E0: ldr      x8, [x8, #0x540]
0x025564E4: strh     w9, [x19, #0xa34]
0x025564E8: blr      x8
0x025564EC: tbz      w0, #0, #0x2556e38
0x025564F0: ldr      w8, [x21, #0xb0]
0x025564F4: cbz      w8, #0x2557058
0x025564F8: ldp      x8, x9, [x19, #0x50]
0x025564FC: mov      w10, #-2
0x02556500: str      w10, [x19, #0x694]
0x02556504: cmp      x9, x8
0x02556508: b.eq     #0x2556e30
0x0255650C: ldr      w9, [x21, #0xb0]
0x02556510: mov      w23, #1
0x02556514: tbnz     w9, #0x1f, #0x25570f4
0x02556518: sxtw     x9, w24
0x0255651C: mov      w10, #0x3f0
0x02556520: mov      w22, wzr
0x02556524: mov      x25, xzr
0x02556528: madd     x9, x9, x10, x26
0x0255652C: add      x29, x19, #0xa48
0x02556530: adrp     x24, #0x526e000
0x02556534: add      x11, x9, #8
0x02556538: add      x10, x9, #4
0x0255653C: stp      x10, x11, [sp, #0x68]
0x02556540: add      x11, x9, #0x1d8
0x02556544: add      x10, x9, #0x1e0
0x02556548: stp      x10, x11, [sp, #0x58]
0x0255654C: add      x10, x9, #0x1e4
0x02556550: str      x10, [sp, #0x78]
0x02556554: add      x10, x9, #0x1e8
0x02556558: add      x9, x9, #0x358
0x0255655C: stp      x9, x10, [sp, #0x48]
0x02556560: mov      w9, #0x15f8
0x02556564: add      x10, sp, #0x80
0x02556568: add      x9, x19, x9
0x0255656C: orr      x26, x10, #1
0x02556570: stp      x26, x9, [sp, #0x30]
0x02556574: ldr      w27, [x8, x25, lsl #2]
0x02556578: ldr      w8, [x21, #0x108]
0x0255657C: cbz      w8, #0x255658c
0x02556580: ldr      w8, [x19, #0x18]
0x02556584: str      w27, [x19, #0x1c]
0x02556588: mov      w27, w8
0x0255658C: ldr      x8, [x28, #0x70]
0x02556590: blr      x8
0x02556594: ldp      x9, x8, [x21]
0x02556598: adrp     x1, #0x1185000
0x0255659C: adrp     x2, #0x1172000
0x025565A0: ldr      w6, [x19, #0x1c]
0x025565A4: add      x1, x1, #0x91f
0x025565A8: ldrb     w7, [x19, #0x692]
0x025565AC: add      x2, x2, #0x4ca
0x025565B0: mov      w4, w27
0x025565B4: mov      x5, x25
0x025565B8: sub      x8, x8, x9
0x025565BC: asr      x3, x8, #3
0x025565C0: ldr      w8, [x21, #0x10c]
0x025565C4: str      w8, [sp]
0x025565C8: bl       #0x2185854
0x025565CC: ldp      x8, x9, [x21]
0x025565D0: mov      w10, w27
0x025565D4: sub      x9, x9, x8
0x025565D8: cmp      x10, x9, asr #3
0x025565DC: b.hs     #0x25570d4
0x025565E0: ldr      x0, [x8, w27, sxtw #3]
0x025565E4: mov      x1, x20
0x025565E8: mov      x2, x19
0x025565EC: ldr      x8, [x0]
0x025565F0: ldr      x8, [x8, #0x18]
0x025565F4: blr      x8
0x025565F8: tbz      w0, #0, #0x25570b8
0x025565FC: ldrb     w8, [x21, #0x1f0]
0x02556600: cbz      w8, #0x2556944
0x02556604: adrp     x8, #0x508c000
0x02556608: mov      x0, x21
0x0255660C: mov      x1, x20
0x02556610: mov      x2, x19
0x02556614: ldr      x8, [x8, #0x5d0]
0x02556618: blr      x8
0x0255661C: ldr      w8, [x21, #0x190]
0x02556620: cmp      w8, #1
0x02556624: b.lt     #0x2556944
0x02556628: ldr      w9, [x21, #0x194]
0x0255662C: cmn      w9, #1
0x02556630: b.ne     #0x255681c
0x02556634: ldr      w10, [x19, #0x150]
0x02556638: cmp      w10, #0x19
0x0255663C: b.hi     #0x255681c
0x02556640: mov      w11, #0x10e2
0x02556644: lsl      w10, w23, w10
0x02556648: movk     w11, #0x220, lsl #16
0x0255664C: tst      w10, w11
0x02556650: b.eq     #0x255681c
0x02556654: ldr      x8, [x24, #0x8f8]
0x02556658: str      w22, [sp, #0x44]
0x0255665C: ldr      x26, [sp, #0x38]
0x02556660: mov      x22, x29
0x02556664: ldr      x24, [sp, #0x70]
0x02556668: mov      x0, x26
0x0255666C: mov      x1, x24
0x02556670: blr      x8
0x02556674: adrp     x8, #0x116b000
0x02556678: ldr      x29, [sp, #0x30]
0x0255667C: add      x8, x8, #0xe8c
0x02556680: add      x0, x0, #0x10
0x02556684: add      x1, sp, #0x80
0x02556688: strb     wzr, [sp, #0x92]
0x0255668C: ldr      q0, [x8]
0x02556690: mov      w8, #0x22
0x02556694: strb     w8, [sp, #0x80]
0x02556698: mov      w8, #0x65
0x0255669C: str      q0, [sp, #0x20]
0x025566A0: str      q0, [x29]
0x025566A4: strb     w8, [x29, #0x10]
0x025566A8: bl       #0x227e6cc
0x025566AC: cbz      x0, #0x2556754
0x025566B0: adrp     x8, #0x526e000
0x025566B4: mov      x0, x26
0x025566B8: mov      x1, x24
0x025566BC: str      x22, [sp, #0x18]
0x025566C0: ldr      x8, [x8, #0x8f8]
0x025566C4: blr      x8
0x025566C8: mov      w8, #0x22
0x025566CC: add      x26, x0, #0x10
0x025566D0: mov      x24, x0
0x025566D4: ldr      q0, [sp, #0x20]
0x025566D8: add      x1, sp, #0x98
0x025566DC: add      x2, sp, #0x80
0x025566E0: strb     w8, [sp, #0x80]
0x025566E4: mov      w8, #0x65
0x025566E8: mov      x0, x26
0x025566EC: str      q0, [x29]
0x025566F0: strb     wzr, [sp, #0x92]
0x025566F4: strb     w8, [x29, #0x10]
0x025566F8: bl       #0x227e070
0x025566FC: ldr      x29, [x0]
0x02556700: ldr      w22, [sp, #0x44]
0x02556704: cbnz     x29, #0x2556778
0x02556708: mov      x28, x0
0x0255670C: mov      w0, #0x50
0x02556710: bl       #0x4b40050
0x02556714: ldr      x8, [sp, #0x90]
0x02556718: stp      xzr, xzr, [x0, #0x40]
0x0255671C: ldr      q0, [sp, #0x80]
0x02556720: stp      xzr, xzr, [x0]
0x02556724: mov      x29, x0
0x02556728: stp      x8, xzr, [x0, #0x30]
0x0255672C: ldr      x8, [sp, #0x98]
0x02556730: str      q0, [x0, #0x20]
0x02556734: str      x8, [x0, #0x10]
0x02556738: str      x0, [x28]
0x0255673C: ldr      x8, [x26]
0x02556740: ldr      x8, [x8]
0x02556744: cbz      x8, #0x2556760
0x02556748: str      x8, [x26]
0x0255674C: ldr      x1, [x28]
0x02556750: b        #0x2556764
0x02556754: mov      x29, x22
0x02556758: ldr      w22, [sp, #0x44]
0x0255675C: b        #0x2556798
0x02556760: mov      x1, x29
0x02556764: ldr      x0, [x24, #0x18]
0x02556768: bl       #0x2260c4c
0x0255676C: ldr      x8, [x24, #0x20]
0x02556770: add      x8, x8, #1
0x02556774: str      x8, [x24, #0x20]
0x02556778: ldrb     w8, [x29, #0x38]
0x0255677C: add      x10, x29, #0x39
0x02556780: ldr      x9, [x29, #0x48]
0x02556784: tst      w8, #1
0x02556788: csel     x0, x10, x9, eq
0x0255678C: bl       #0x4b400f0
0x02556790: adrp     x28, #0x509c000
0x02556794: ldr      x29, [sp, #0x18]
0x02556798: ldp      x9, x10, [x21, #0x1b8]
0x0255679C: ldr      x8, [x21, #0x1a0]
0x025567A0: ldr      w24, [x8]
0x025567A4: subs     x10, x10, x9
0x025567A8: b.eq     #0x25567dc
0x025567AC: asr      x10, x10, #2
0x025567B0: cmp      x10, #1
0x025567B4: csinc    x10, x10, xzr, hi
0x025567B8: ldr      w11, [x9]
0x025567BC: cmp      w0, w11
~~~

### Function start 0x255a948
Hits: [{"pc": "0x255b17c", "adrp": "0x255b174", "target": "0x11bef92", "label": " check visible frame_no: %d hero %d m_invisible_to_visible_frame %d m_previous_visible_num %d min_visilble_dist %d friend_num %d near_friend_num %d is_friend_front %d is_enemy_invisible_5s %d exist_filter_hero %d ", "keywords": ["invisible", "invisible"], "fde_start": "0x255a948", "fde_end": "0x255b448", "kind": "add", "reg": "x2"}, {"pc": "0x255b220", "adrp": "0x255b218", "target": "0x11d2080", "label": " invisible_to_visible_tag sesion start frame_no: %d hero %d m_invisible_to_visible_frame %d cur_invisible_skill_delay %d diff %d", "keywords": ["invisible", "invisible", "invisible"], "fde_start": "0x255a948", "fde_end": "0x255b448", "kind": "add", "reg": "x2"}, {"pc": "0x255b2b4", "adrp": "0x255b2ac", "target": "0x117f55c", "label": "sesion end frame_no: %d hero %d m_invisible_to_visible_frame %d cur_invisible_skill_delay %d diff %d", "keywords": ["invisible", "invisible"], "fde_start": "0x255a948", "fde_end": "0x255b448", "kind": "add", "reg": "x2"}, {"pc": "0x255b3b4", "adrp": "0x255b3ac", "target": "0x117912c", "label": "sesion end frame_no: %d hero %d m_invisible_to_visible_frame %d cur_invisible_skill_delay %d diff %d skill_type:%d", "keywords": ["invisible", "invisible"], "fde_start": "0x255a948", "fde_end": "0x255b448", "kind": "add", "reg": "x2"}]
~~~asm
0x0255A948: sub      sp, sp, #0x110
0x0255A94C: stp      x29, x30, [sp, #0xb0]
0x0255A950: stp      x28, x27, [sp, #0xc0]
0x0255A954: stp      x26, x25, [sp, #0xd0]
0x0255A958: stp      x24, x23, [sp, #0xe0]
0x0255A95C: stp      x22, x21, [sp, #0xf0]
0x0255A960: stp      x20, x19, [sp, #0x100]
0x0255A964: adrp     x8, #0x517f000
0x0255A968: mov      x28, x0
0x0255A96C: add      x0, x0, #0xcc
0x0255A970: mov      x22, x1
0x0255A974: ldr      x8, [x8, #0x748]
0x0255A978: str      x0, [sp, #0x90]
0x0255A97C: blr      x8
0x0255A980: add      x8, sp, #0x98
0x0255A984: mov      w21, w0
0x0255A988: add      x19, x8, #8
0x0255A98C: ldr      x8, [x22, #0x68]
0x0255A990: ldr      w25, [x22]
0x0255A994: mov      x20, x19
0x0255A998: stp      xzr, xzr, [sp, #0xa0]
0x0255A99C: str      x8, [sp, #0x68]
0x0255A9A0: str      x19, [sp, #0x98]
0x0255A9A4: cbz      xzr, #0x255a9c4
0x0255A9A8: mov      x8, xzr
0x0255A9AC: mov      x24, x20
0x0255A9B0: mov      x23, x20
0x0255A9B4: ldr      x9, [x23]
0x0255A9B8: cbz      x9, #0x255aa3c
0x0255A9BC: cbnz     x8, #0x255aaa8
0x0255A9C0: b        #0x255aa88
0x0255A9C4: mov      w0, #0x20
0x0255A9C8: bl       #0x4b40050
0x0255A9CC: mov      w8, #0x99
0x0255A9D0: mov      x1, x0
0x0255A9D4: stp      xzr, xzr, [x0]
0x0255A9D8: str      x20, [x0, #0x10]
0x0255A9DC: str      w8, [x0, #0x1c]
0x0255A9E0: stp      x0, x0, [sp, #0x98]
0x0255A9E4: bl       #0x2260c4c
0x0255A9E8: ldp      x8, x9, [sp, #0xa0]
0x0255A9EC: add      x9, x9, #1
0x0255A9F0: str      x9, [sp, #0xa8]
0x0255A9F4: cbz      x8, #0x255a9a8
0x0255A9F8: mov      x24, x8
0x0255A9FC: mov      x23, x19
0x0255AA00: ldr      w9, [x24, #0x1c]
0x0255AA04: cmp      w9, #0x75
0x0255AA08: b.lt     #0x255aa20
0x0255AA0C: ldr      x9, [x24]
0x0255AA10: cbz      x9, #0x255b400
0x0255AA14: mov      x23, x24
0x0255AA18: mov      x24, x9
0x0255AA1C: b        #0x255aa00
0x0255AA20: cmp      w9, #0x74
0x0255AA24: b.eq     #0x255a9b4
0x0255AA28: mov      x23, x24
0x0255AA2C: ldr      x9, [x23, #8]!
0x0255AA30: cbz      x9, #0x255a9b4
0x0255AA34: mov      x24, x9
0x0255AA38: b        #0x255aa00
0x0255AA3C: mov      w0, #0x20
0x0255AA40: bl       #0x4b40050
0x0255AA44: mov      x1, x0
0x0255AA48: mov      w8, #0x74
0x0255AA4C: stp      xzr, xzr, [x1]
0x0255AA50: str      x24, [x1, #0x10]
0x0255AA54: str      w8, [x1, #0x1c]
0x0255AA58: str      x1, [x23]
0x0255AA5C: ldr      x8, [sp, #0x98]
0x0255AA60: ldr      x8, [x8]
0x0255AA64: cbz      x8, #0x255aa70
0x0255AA68: str      x8, [sp, #0x98]
0x0255AA6C: ldr      x1, [x23]
0x0255AA70: ldr      x0, [sp, #0xa0]
0x0255AA74: bl       #0x2260c4c
0x0255AA78: ldp      x8, x9, [sp, #0xa0]
0x0255AA7C: add      x9, x9, #1
0x0255AA80: str      x9, [sp, #0xa8]
0x0255AA84: cbnz     x8, #0x255aaa8
0x0255AA88: mov      x19, x20
0x0255AA8C: ldr      x8, [x19]
0x0255AA90: cbnz     x8, #0x255ab30
0x0255AA94: b        #0x255aae8
0x0255AA98: ldr      x9, [x8]
0x0255AA9C: cbz      x9, #0x255aad8
0x0255AAA0: mov      x19, x8
0x0255AAA4: mov      x8, x9
0x0255AAA8: ldr      w9, [x8, #0x1c]
0x0255AAAC: cmp      w9, #0xbe
0x0255AAB0: b.ge     #0x255aa98
0x0255AAB4: cmp      w9, #0xbd
0x0255AAB8: b.eq     #0x255aac8
0x0255AABC: mov      x19, x8
0x0255AAC0: ldr      x9, [x19, #8]!
0x0255AAC4: cbnz     x9, #0x255aaa4
0x0255AAC8: mov      x20, x8
0x0255AACC: ldr      x8, [x19]
0x0255AAD0: cbnz     x8, #0x255ab30
0x0255AAD4: b        #0x255aae8
0x0255AAD8: mov      x20, x8
0x0255AADC: mov      x19, x8
0x0255AAE0: ldr      x8, [x19]
0x0255AAE4: cbnz     x8, #0x255ab30
0x0255AAE8: mov      w0, #0x20
0x0255AAEC: bl       #0x4b40050
0x0255AAF0: mov      x1, x0
0x0255AAF4: mov      w8, #0xbd
0x0255AAF8: stp      xzr, xzr, [x1]
0x0255AAFC: str      x20, [x1, #0x10]
0x0255AB00: str      w8, [x1, #0x1c]
0x0255AB04: str      x1, [x19]
0x0255AB08: ldr      x8, [sp, #0x98]
0x0255AB0C: ldr      x8, [x8]
0x0255AB10: cbz      x8, #0x255ab1c
0x0255AB14: str      x8, [sp, #0x98]
0x0255AB18: ldr      x1, [x19]
0x0255AB1C: ldr      x0, [sp, #0xa0]
0x0255AB20: bl       #0x2260c4c
0x0255AB24: ldr      x8, [sp, #0xa8]
0x0255AB28: add      x8, x8, #1
0x0255AB2C: str      x8, [sp, #0xa8]
0x0255AB30: ldr      w9, [x22, #0x334]
0x0255AB34: sxtw     x29, w21
0x0255AB38: ldr      w8, [x28, #0x1f4]
0x0255AB3C: ldp      x19, x10, [x22, #0x68]
0x0255AB40: cmp      w9, #0
0x0255AB44: csel     w26, w9, w8, gt
0x0255AB48: cmp      x10, x19
0x0255AB4C: b.eq     #0x255aba8
0x0255AB50: add      x9, x28, #0x1d8
0x0255AB54: mov      w8, #0x3f0
0x0255AB58: str      w26, [sp, #0x3c]
0x0255AB5C: mov      x26, #0xefbf
0x0255AB60: str      x29, [sp, #0x40]
0x0255AB64: movk     x26, #0xbefb, lsl #16
0x0255AB68: str      x9, [sp, #0x70]
0x0255AB6C: ldr      x9, [sp, #0x68]
0x0255AB70: movk     x26, #0xfbef, lsl #32
0x0255AB74: str      w25, [sp, #0x5c]
0x0255AB78: mov      x25, xzr
0x0255AB7C: mov      w20, wzr
0x0255AB80: madd     x8, x29, x8, x9
0x0255AB84: mov      w21, #1
0x0255AB88: mov      w23, #0x3f0
0x0255AB8C: movk     x26, #0xefbe, lsl #48
0x0255AB90: add      x29, x8, #0x18
0x0255AB94: add      x8, x8, #0x2c
0x0255AB98: str      x8, [sp, #0x88]
0x0255AB9C: mov      w8, #1
0x0255ABA0: str      w8, [sp, #0x54]
0x0255ABA4: b        #0x255ac28
0x0255ABA8: mov      w22, wzr
0x0255ABAC: mov      w23, wzr
0x0255ABB0: mov      w27, wzr
0x0255ABB4: mov      w24, wzr
0x0255ABB8: mov      w21, #1
0x0255ABBC: mov      w8, #0x2710
0x0255ABC0: str      wzr, [sp, #0x58]
0x0255ABC4: str      w8, [sp, #0x80]
0x0255ABC8: b        #0x255b138
0x0255ABCC: str      x8, [x28, #0x1d0]
0x0255ABD0: ldr      x1, [x24]
0x0255ABD4: ldr      x0, [x28, #0x1d8]
0x0255ABD8: bl       #0x2260c4c
0x0255ABDC: ldr      x8, [x28, #0x1e0]
0x0255ABE0: add      x8, x8, #1
0x0255ABE4: str      x8, [x28, #0x1e0]
0x0255ABE8: ldr      w8, [x25, #0x20]
0x0255ABEC: ldr      w9, [sp, #0x5c]
0x0255ABF0: sub      w8, w9, w8
0x0255ABF4: ldr      w9, [sp, #0x54]
0x0255ABF8: cmp      w8, #0x1d
0x0255ABFC: cset     w8, gt
0x0255AC00: and      w9, w8, w9
0x0255AC04: str      w9, [sp, #0x54]
0x0255AC08: ldp      x19, x8, [x22, #0x68]
0x0255AC0C: add      w25, w20, #1
0x0255AC10: mov      w20, w25
0x0255AC14: sub      x9, x8, x19
0x0255AC18: asr      x9, x9, #4
0x0255AC1C: mul      x9, x9, x26
0x0255AC20: cmp      x9, x25
0x0255AC24: b.ls     #0x255ad5c
0x0255AC28: madd     x8, x25, x23, x19
0x0255AC2C: ldr      w9, [x29]
0x0255AC30: ldr      w10, [x8, #0x18]
0x0255AC34: ldr      w8, [x8, #0x58]
0x0255AC38: cmp      w9, w10
0x0255AC3C: ccmp     w8, #1, #8, ne
0x0255AC40: b.lt     #0x255ac08
0x0255AC44: madd     x8, x25, x23, x19
0x0255AC48: add      x2, x8, #0x2c
0x0255AC4C: adrp     x8, #0x517f000
0x0255AC50: ldr      x8, [x8, #0x388]
0x0255AC54: ldp      x1, x0, [sp, #0x88]
0x0255AC58: mov      w3, #1
0x0255AC5C: blr      x8
0x0255AC60: madd     x8, x25, x23, x19
0x0255AC64: ldr      x9, [x8, #0x298]
0x0255AC68: ldr      w8, [x29]
0x0255AC6C: cmp      x9, x8
0x0255AC70: b.lo     #0x255ac08
0x0255AC74: cmp      w0, #0x77
0x0255AC78: b.gt     #0x255ac08
0x0255AC7C: sub      w8, w8, #1
0x0255AC80: madd     x9, x25, x23, x19
0x0255AC84: sxtw     x8, w8
0x0255AC88: lsr      x10, x8, #3
0x0255AC8C: and      x10, x10, #0x1ffffffffffffff8
0x0255AC90: ldr      x9, [x9, #0x290]
0x0255AC94: lsl      x8, x21, x8
0x0255AC98: ldr      x9, [x9, x10]
0x0255AC9C: and      x8, x9, x8
0x0255ACA0: cbz      x8, #0x255ac08
0x0255ACA4: ldr      x24, [sp, #0x70]
0x0255ACA8: ldr      x27, [x24]
0x0255ACAC: cbz      x27, #0x255ac08
0x0255ACB0: madd     x19, x25, x23, x19
0x0255ACB4: mov      x9, x24
0x0255ACB8: mov      x10, x27
0x0255ACBC: ldr      w8, [x19, #8]!
0x0255ACC0: ldr      w11, [x10, #0x1c]
0x0255ACC4: cmp      w11, w8
0x0255ACC8: cset     w11, lt
0x0255ACCC: csel     x9, x9, x10, lt
0x0255ACD0: ldr      x10, [x10, w11, uxtw #3]
0x0255ACD4: cbnz     x10, #0x255acc0
0x0255ACD8: cmp      x9, x24
0x0255ACDC: b.eq     #0x255ac08
0x0255ACE0: ldr      w9, [x9, #0x1c]
0x0255ACE4: cmp      w8, w9
0x0255ACE8: b.ge     #0x255ad00
0x0255ACEC: b        #0x255ac08
0x0255ACF0: ldr      x9, [x27]
0x0255ACF4: mov      x24, x27
0x0255ACF8: cbz      x9, #0x255ad20
0x0255ACFC: mov      x27, x9
0x0255AD00: ldr      w9, [x27, #0x1c]
0x0255AD04: cmp      w8, w9
~~~

### Function start 0x259bbbc
Hits: [{"pc": "0x259bc10", "adrp": "0x259bbfc", "target": "0x11cb768", "label": "Foundation/Common/include/Type/VInt3.inl", "keywords": ["VInt3"], "fde_start": "0x259bbbc", "fde_end": "0x25a15d4", "kind": "add", "reg": "x0"}]
~~~asm
0x0259BBBC: str      x29, [sp, #-0x30]!
0x0259BBC0: stp      x30, x21, [sp, #0x10]
0x0259BBC4: stp      x20, x19, [sp, #0x20]
0x0259BBC8: sub      sp, sp, #1, lsl #12
0x0259BBCC: sub      sp, sp, #0x270
0x0259BBD0: mov      x19, x8
0x0259BBD4: adrp     x8, #0x508f000
0x0259BBD8: mov      x20, x0
0x0259BBDC: ldr      x9, [x8, #0xc68]
0x0259BBE0: add      x8, sp, #1, lsl #12
0x0259BBE4: add      x8, x8, #0x260
0x0259BBE8: blr      x9
0x0259BBEC: ldr      x8, [sp, #0x1260]
0x0259BBF0: cbz      x8, #0x259bcd8
0x0259BBF4: adrp     x8, #0x5091000
0x0259BBF8: adrp     x9, #0x5091000
0x0259BBFC: adrp     x0, #0x11cb000
0x0259BC00: adrp     x1, #0x116b000
0x0259BC04: adrp     x2, #0x1192000
0x0259BC08: adrp     x4, #0x11eb000
0x0259BC0C: ldr      x21, [x8, #0x208]
0x0259BC10: add      x0, x0, #0x768
0x0259BC14: ldr      x8, [x9, #0x690]
0x0259BC18: add      x1, x1, #0x593
0x0259BC1C: add      x2, x2, #0x26d
0x0259BC20: add      x4, x4, #0xca2
0x0259BC24: mov      w3, #1
0x0259BC28: blr      x8
0x0259BC2C: ldp      x8, x9, [x21]
0x0259BC30: adrp     x21, #0x508f000
0x0259BC34: add      x0, sp, #1, lsl #12
0x0259BC38: ldr      x10, [sp, #0x1268]
0x0259BC3C: add      x0, x0, #0x250
0x0259BC40: ldr      x11, [sp, #0x1260]
0x0259BC44: mul      x8, x10, x8
0x0259BC48: add      x10, sp, #1, lsl #12
0x0259BC4C: mul      x9, x11, x9
0x0259BC50: add      x10, x10, #0x250
0x0259BC54: add      x1, x10, #8
0x0259BC58: ldr      x10, [x21, #0xa30]
0x0259BC5C: str      x8, [sp, #0x1250]
0x0259BC60: str      x9, [sp, #0x1258]
0x0259BC64: blr      x10
0x0259BC68: cbz      x0, #0x259bc84
0x0259BC6C: ldr      x8, [sp, #0x1250]
0x0259BC70: ldr      x9, [sp, #0x1258]
0x0259BC74: sdiv     x8, x8, x0
0x0259BC78: sdiv     x9, x9, x0
0x0259BC7C: str      x8, [sp, #0x1250]
0x0259BC80: str      x9, [sp, #0x1258]
0x0259BC84: ldp      x8, x9, [x20, #0x90]
0x0259BC88: add      x0, sp, #1, lsl #12
0x0259BC8C: ldp      x10, x11, [x20, #0xe0]
0x0259BC90: add      x0, x0, #0x1d0
0x0259BC94: mul      x8, x10, x8
0x0259BC98: add      x10, sp, #1, lsl #12
0x0259BC9C: mul      x9, x11, x9
0x0259BCA0: add      x10, x10, #0x1d0
0x0259BCA4: ldr      x11, [x21, #0xa30]
0x0259BCA8: add      x1, x10, #8
0x0259BCAC: str      x8, [sp, #0x11d0]
0x0259BCB0: str      x9, [sp, #0x11d8]
0x0259BCB4: blr      x11
0x0259BCB8: ldr      x8, [sp, #0x11d0]
0x0259BCBC: cbz      x0, #0x259bd1c
0x0259BCC0: ldr      x9, [sp, #0x11d8]
0x0259BCC4: sdiv     x8, x8, x0
0x0259BCC8: sdiv     x9, x9, x0
0x0259BCCC: str      x8, [sp, #0x11d0]
0x0259BCD0: str      x9, [sp, #0x11d8]
0x0259BCD4: b        #0x259bd20
0x0259BCD8: ldp      q0, q1, [x20]
0x0259BCDC: ldp      q2, q3, [x20, #0x20]
0x0259BCE0: stp      q0, q1, [x19]
0x0259BCE4: ldp      q0, q1, [x20, #0x40]
0x0259BCE8: stp      q2, q3, [x19, #0x20]
0x0259BCEC: ldp      q2, q3, [x20, #0x60]
0x0259BCF0: stp      q0, q1, [x19, #0x40]
0x0259BCF4: ldp      q0, q1, [x20, #0x80]
0x0259BCF8: stp      q2, q3, [x19, #0x60]
0x0259BCFC: ldp      q2, q3, [x20, #0xa0]
0x0259BD00: stp      q0, q1, [x19, #0x80]
0x0259BD04: ldp      q0, q1, [x20, #0xc0]
0x0259BD08: stp      q2, q3, [x19, #0xa0]
0x0259BD0C: ldp      q2, q3, [x20, #0xe0]
0x0259BD10: stp      q0, q1, [x19, #0xc0]
0x0259BD14: stp      q2, q3, [x19, #0xe0]
0x0259BD18: b        #0x25a15bc
0x0259BD1C: ldr      x9, [sp, #0x11d8]
0x0259BD20: ldp      x10, x11, [x20, #0x70]
0x0259BD24: add      x0, sp, #1, lsl #12
0x0259BD28: add      x0, x0, #0x1e0
0x0259BD2C: mul      x8, x10, x8
0x0259BD30: add      x10, sp, #1, lsl #12
0x0259BD34: mul      x9, x11, x9
0x0259BD38: add      x10, x10, #0x1e0
0x0259BD3C: ldr      x11, [x21, #0xa30]
0x0259BD40: add      x1, x10, #8
0x0259BD44: str      x8, [sp, #0x11e0]
0x0259BD48: str      x9, [sp, #0x11e8]
0x0259BD4C: blr      x11
0x0259BD50: cbz      x0, #0x259bd6c
0x0259BD54: ldr      x8, [sp, #0x11e0]
0x0259BD58: ldr      x9, [sp, #0x11e8]
0x0259BD5C: sdiv     x8, x8, x0
0x0259BD60: sdiv     x9, x9, x0
0x0259BD64: str      x8, [sp, #0x11e0]
0x0259BD68: str      x9, [sp, #0x11e8]
0x0259BD6C: ldp      x8, x9, [x20, #0xd0]
0x0259BD70: add      x0, sp, #1, lsl #12
0x0259BD74: ldp      x10, x11, [x20, #0xa0]
0x0259BD78: add      x0, x0, #0x1b0
0x0259BD7C: mul      x8, x10, x8
0x0259BD80: add      x10, sp, #1, lsl #12
0x0259BD84: mul      x9, x11, x9
0x0259BD88: add      x10, x10, #0x1b0
0x0259BD8C: ldr      x11, [x21, #0xa30]
0x0259BD90: add      x1, x10, #8
0x0259BD94: str      x8, [sp, #0x11b0]
0x0259BD98: str      x9, [sp, #0x11b8]
0x0259BD9C: blr      x11
0x0259BDA0: ldr      x8, [sp, #0x11b0]
0x0259BDA4: cbz      x0, #0x259bdc0
0x0259BDA8: ldr      x9, [sp, #0x11b8]
0x0259BDAC: sdiv     x8, x8, x0
0x0259BDB0: sdiv     x9, x9, x0
0x0259BDB4: str      x8, [sp, #0x11b0]
0x0259BDB8: str      x9, [sp, #0x11b8]
0x0259BDBC: b        #0x259bdc4
0x0259BDC0: ldr      x9, [sp, #0x11b8]
0x0259BDC4: ldp      x10, x11, [x20, #0x70]
0x0259BDC8: add      x0, sp, #1, lsl #12
0x0259BDCC: add      x0, x0, #0x1c0
0x0259BDD0: mul      x8, x10, x8
0x0259BDD4: add      x10, sp, #1, lsl #12
0x0259BDD8: mul      x9, x11, x9
0x0259BDDC: add      x10, x10, #0x1c0
0x0259BDE0: ldr      x11, [x21, #0xa30]
0x0259BDE4: add      x1, x10, #8
0x0259BDE8: str      x8, [sp, #0x11c0]
0x0259BDEC: str      x9, [sp, #0x11c8]
0x0259BDF0: blr      x11
0x0259BDF4: cbz      x0, #0x259be14
0x0259BDF8: ldr      x8, [sp, #0x11c0]
0x0259BDFC: ldr      x10, [sp, #0x11c8]
0x0259BE00: sdiv     x9, x8, x0
0x0259BE04: sdiv     x8, x10, x0
0x0259BE08: str      x9, [sp, #0x11c0]
0x0259BE0C: str      x8, [sp, #0x11c8]
0x0259BE10: b        #0x259be1c
0x0259BE14: ldr      x8, [sp, #0x11c8]
0x0259BE18: ldr      x9, [sp, #0x11c0]
0x0259BE1C: ldr      x10, [sp, #0x11e8]
0x0259BE20: add      x0, sp, #1, lsl #12
0x0259BE24: ldr      x11, [sp, #0x11e0]
0x0259BE28: add      x0, x0, #0x1f0
0x0259BE2C: mul      x9, x10, x9
0x0259BE30: neg      x9, x9
0x0259BE34: madd     x9, x11, x8, x9
0x0259BE38: ldr      x11, [x21, #0xa30]
0x0259BE3C: mul      x8, x10, x8
0x0259BE40: add      x10, sp, #1, lsl #12
0x0259BE44: add      x10, x10, #0x1f0
0x0259BE48: add      x1, x10, #8
0x0259BE4C: str      x9, [sp, #0x11f0]
0x0259BE50: str      x8, [sp, #0x11f8]
0x0259BE54: blr      x11
0x0259BE58: cbz      x0, #0x259be74
0x0259BE5C: ldr      x8, [sp, #0x11f0]
0x0259BE60: ldr      x9, [sp, #0x11f8]
0x0259BE64: sdiv     x8, x8, x0
0x0259BE68: sdiv     x9, x9, x0
0x0259BE6C: str      x8, [sp, #0x11f0]
0x0259BE70: str      x9, [sp, #0x11f8]
0x0259BE74: ldp      x8, x9, [x20, #0xd0]
0x0259BE78: add      x0, sp, #1, lsl #12
0x0259BE7C: ldp      x10, x11, [x20, #0x60]
0x0259BE80: add      x0, x0, #0x190
0x0259BE84: mul      x8, x10, x8
0x0259BE88: add      x10, sp, #1, lsl #12
0x0259BE8C: mul      x9, x11, x9
0x0259BE90: add      x10, x10, #0x190
0x0259BE94: ldr      x11, [x21, #0xa30]
0x0259BE98: add      x1, x10, #8
0x0259BE9C: str      x8, [sp, #0x1190]
0x0259BEA0: str      x9, [sp, #0x1198]
0x0259BEA4: blr      x11
0x0259BEA8: ldr      x8, [sp, #0x1190]
0x0259BEAC: cbz      x0, #0x259bec8
0x0259BEB0: ldr      x9, [sp, #0x1198]
0x0259BEB4: sdiv     x8, x8, x0
0x0259BEB8: sdiv     x9, x9, x0
0x0259BEBC: str      x8, [sp, #0x1190]
0x0259BEC0: str      x9, [sp, #0x1198]
0x0259BEC4: b        #0x259becc
0x0259BEC8: ldr      x9, [sp, #0x1198]
0x0259BECC: ldp      x10, x11, [x20, #0xb0]
0x0259BED0: add      x0, sp, #1, lsl #12
0x0259BED4: add      x0, x0, #0x1a0
0x0259BED8: mul      x8, x10, x8
0x0259BEDC: add      x10, sp, #1, lsl #12
0x0259BEE0: mul      x9, x11, x9
0x0259BEE4: add      x10, x10, #0x1a0
0x0259BEE8: ldr      x11, [x21, #0xa30]
0x0259BEEC: add      x1, x10, #8
0x0259BEF0: str      x8, [sp, #0x11a0]
0x0259BEF4: str      x9, [sp, #0x11a8]
0x0259BEF8: blr      x11
0x0259BEFC: cbz      x0, #0x259bf1c
0x0259BF00: ldr      x8, [sp, #0x11a0]
0x0259BF04: ldr      x10, [sp, #0x11a8]
0x0259BF08: sdiv     x9, x8, x0
0x0259BF0C: sdiv     x8, x10, x0
0x0259BF10: str      x9, [sp, #0x11a0]
0x0259BF14: str      x8, [sp, #0x11a8]
0x0259BF18: b        #0x259bf24
0x0259BF1C: ldr      x8, [sp, #0x11a8]
0x0259BF20: ldr      x9, [sp, #0x11a0]
0x0259BF24: ldr      x10, [sp, #0x11f0]
0x0259BF28: add      x0, sp, #1, lsl #12
0x0259BF2C: ldr      x11, [sp, #0x11f8]
0x0259BF30: add      x0, x0, #0x200
0x0259BF34: mul      x10, x10, x8
0x0259BF38: mul      x8, x11, x8
0x0259BF3C: madd     x9, x11, x9, x10
0x0259BF40: add      x10, sp, #1, lsl #12
0x0259BF44: add      x10, x10, #0x200
0x0259BF48: ldr      x11, [x21, #0xa30]
0x0259BF4C: add      x1, x10, #8
0x0259BF50: str      x8, [sp, #0x1208]
0x0259BF54: str      x9, [sp, #0x1200]
0x0259BF58: blr      x11
0x0259BF5C: cbz      x0, #0x259bf78
0x0259BF60: ldr      x8, [sp, #0x1200]
0x0259BF64: ldr      x9, [sp, #0x1208]
0x0259BF68: sdiv     x8, x8, x0
0x0259BF6C: sdiv     x9, x9, x0
0x0259BF70: str      x8, [sp, #0x1200]
0x0259BF74: str      x9, [sp, #0x1208]
0x0259BF78: ldp      x8, x9, [x20, #0x50]
~~~

### Function start 0x25a6288
Hits: [{"pc": "0x25a62cc", "adrp": "0x25a62c4", "target": "0x11a5472", "label": "VInt3", "keywords": ["VInt3"], "fde_start": "0x25a6288", "fde_end": "0x25a6408", "kind": "add", "reg": "x1"}]
~~~asm
0x025A6288: str      x30, [sp, #-0x40]!
0x025A628C: stp      x24, x23, [sp, #0x10]
0x025A6290: stp      x22, x21, [sp, #0x20]
0x025A6294: stp      x20, x19, [sp, #0x30]
0x025A6298: adrp     x22, #0x5271000
0x025A629C: ldr      x0, [x22, #0x950]
0x025A62A0: cbnz     x0, #0x25a63f4
0x025A62A4: mov      w0, #0x178
0x025A62A8: bl       #0x4b40050
0x025A62AC: adrp     x8, #0x5066000
0x025A62B0: mov      x19, x0
0x025A62B4: ldr      x8, [x8, #0x360]
0x025A62B8: cbz      x8, #0x25a62e0
0x025A62BC: adrp     x9, #0x5003000
0x025A62C0: adrp     x10, #0x5003000
0x025A62C4: adrp     x1, #0x11a5000
0x025A62C8: mov      x0, x19
0x025A62CC: add      x1, x1, #0x472
0x025A62D0: mov      w4, #0xc
0x025A62D4: ldr      x3, [x9, #0xc20]
0x025A62D8: ldr      x2, [x10, #0xc18]
0x025A62DC: blr      x8
0x025A62E0: mov      w8, #1
0x025A62E4: mov      w0, #0x80
0x025A62E8: str      x19, [x22, #0x950]
0x025A62EC: strb     w8, [x19, #0x160]
0x025A62F0: bl       #0x4b40050
0x025A62F4: adrp     x20, #0x503f000
0x025A62F8: add      x20, x20, #0xf70
0x025A62FC: mov      x1, x20
0x025A6300: bl       #0x21b054c
0x025A6304: adrp     x23, #0x50b8000
0x025A6308: adrp     x1, #0x11d1000
0x025A630C: mov      x21, x0
0x025A6310: add      x0, x0, #0x10
0x025A6314: add      x1, x1, #0xd6c
0x025A6318: ldr      x8, [x23, #0x3f8]
0x025A631C: blr      x8
0x025A6320: adrp     x24, #0x50b9000
0x025A6324: mov      x0, x21
0x025A6328: mov      w1, #1
0x025A632C: ldr      x8, [x24, #0xa98]
0x025A6330: blr      x8
0x025A6334: ldr      x8, [x19]
0x025A6338: mov      x0, x19
0x025A633C: mov      x1, x21
0x025A6340: ldr      x8, [x8, #0xc0]
0x025A6344: blr      x8
0x025A6348: mov      w0, #0x80
0x025A634C: bl       #0x4b40050
0x025A6350: mov      x1, x20
0x025A6354: bl       #0x21b054c
0x025A6358: adrp     x1, #0x115f000
0x025A635C: mov      x21, x0
0x025A6360: ldr      x8, [x23, #0x3f8]
0x025A6364: add      x0, x0, #0x10
0x025A6368: add      x1, x1, #0x5bd
0x025A636C: blr      x8
0x025A6370: ldr      x8, [x24, #0xa98]
0x025A6374: mov      x0, x21
0x025A6378: mov      w1, #5
0x025A637C: blr      x8
0x025A6380: ldr      x8, [x19]
0x025A6384: mov      x0, x19
0x025A6388: mov      x1, x21
0x025A638C: ldr      x8, [x8, #0xc0]
0x025A6390: blr      x8
0x025A6394: mov      w0, #0x80
0x025A6398: bl       #0x4b40050
0x025A639C: mov      x1, x20
0x025A63A0: bl       #0x21b054c
0x025A63A4: adrp     x1, #0x11f9000
0x025A63A8: mov      x20, x0
0x025A63AC: ldr      x8, [x23, #0x3f8]
0x025A63B0: add      x0, x0, #0x10
0x025A63B4: add      x1, x1, #0xc99
0x025A63B8: blr      x8
0x025A63BC: ldr      x8, [x24, #0xa98]
0x025A63C0: mov      x0, x20
0x025A63C4: mov      w1, #9
0x025A63C8: blr      x8
0x025A63CC: ldr      x8, [x19]
0x025A63D0: mov      x0, x19
0x025A63D4: mov      x1, x20
0x025A63D8: ldr      x8, [x8, #0xc0]
0x025A63DC: blr      x8
0x025A63E0: ldr      x8, [x19]
0x025A63E4: mov      x0, x19
0x025A63E8: ldr      x8, [x8, #0x18]
0x025A63EC: blr      x8
0x025A63F0: ldr      x0, [x22, #0x950]
0x025A63F4: ldp      x20, x19, [sp, #0x30]
0x025A63F8: ldp      x22, x21, [sp, #0x20]
0x025A63FC: ldp      x24, x23, [sp, #0x10]
0x025A6400: ldr      x30, [sp], #0x40
0x025A6404: ret      
~~~

### Function start 0x25d2f9c
Hits: [{"pc": "0x25d2fa0", "adrp": "0x25d2f9c", "target": "0x11a5472", "label": "VInt3", "keywords": ["VInt3"], "fde_start": "0x25d2f9c", "fde_end": "0x25d2fa8", "kind": "add", "reg": "x0"}]
~~~asm
0x025D2F9C: adrp     x0, #0x11a5000
0x025D2FA0: add      x0, x0, #0x472
0x025D2FA4: ret      
~~~

### Function start 0x267180c
Hits: [{"pc": "0x26719c0", "adrp": "0x26719a0", "target": "0x12070a1", "label": "frame %d, mainCid %d, mainRid %d, camp %d, valid %d, visibleEnemyCnt %d, invisibleEnemyCnt %d, useVisibleRule %d, visibleFloor %d, visibleCeil %d, useInvisibleRule %d, invisibleFloor %d, invisibleCeil %d", "keywords": ["invisible", "invisible", "invisible"], "fde_start": "0x267180c", "fde_end": "0x2671a0c", "kind": "add", "reg": "x2"}]
~~~asm
0x0267180C: sub      sp, sp, #0xa0
0x02671810: str      x30, [sp, #0x40]
0x02671814: stp      x28, x27, [sp, #0x50]
0x02671818: stp      x26, x25, [sp, #0x60]
0x0267181C: stp      x24, x23, [sp, #0x70]
0x02671820: stp      x22, x21, [sp, #0x80]
0x02671824: stp      x20, x19, [sp, #0x90]
0x02671828: ldr      w8, [x3, #0x14]
0x0267182C: mov      x19, x3
0x02671830: mov      x23, x1
0x02671834: cmp      w8, #0
0x02671838: b.le     #0x26718c4
0x0267183C: ldp      x9, x10, [x23, #0x88]
0x02671840: mov      x22, x4
0x02671844: mov      x24, x0
0x02671848: cmp      x9, x10
0x0267184C: b.eq     #0x26718f8
0x02671850: sub      w13, w8, #1
0x02671854: mov      w14, #1
0x02671858: mov      w21, wzr
0x0267185C: mov      w20, wzr
0x02671860: sub      x11, x8, #1
0x02671864: lsr      x12, x13, #6
0x02671868: lsl      x13, x14, x13
0x0267186C: b        #0x267187c
0x02671870: add      x9, x9, #0x348
0x02671874: cmp      x9, x10
0x02671878: b.eq     #0x2671900
0x0267187C: ldr      w14, [x9, #0x14]
0x02671880: cmp      w14, w8
0x02671884: b.eq     #0x2671870
0x02671888: ldr      x14, [x9, #0x238]
0x0267188C: cmp      x11, x14
0x02671890: b.hs     #0x2671870
0x02671894: ldr      x14, [x9, #0x230]
0x02671898: ldr      w15, [x9, #0x48]
0x0267189C: ldr      x14, [x14, x12, lsl #3]
0x026718A0: cmp      w15, #1
0x026718A4: cset     w15, lt
0x026718A8: tst      x14, x13
0x026718AC: cset     w14, ne
0x026718B0: orr      w14, w15, w14
0x026718B4: eor      w15, w14, #1
0x026718B8: add      w21, w21, w14
0x026718BC: add      w20, w20, w15
0x026718C0: b        #0x2671870
0x026718C4: adrp     x8, #0x5098000
0x026718C8: ldr      x8, [x8, #0x9f8]
0x026718CC: blr      x8
0x026718D0: ldp      w4, w5, [x19, #4]
0x026718D4: adrp     x1, #0x11c5000
0x026718D8: adrp     x2, #0x1172000
0x026718DC: ldr      w3, [x23]
0x026718E0: add      x1, x1, #0xaa8
0x026718E4: ldr      w6, [x19, #0x14]
0x026718E8: add      x2, x2, #0xbd8
0x026718EC: bl       #0x2185848
0x026718F0: mov      w24, #1
0x026718F4: b        #0x26719e8
0x026718F8: mov      w20, wzr
0x026718FC: mov      w21, wzr
0x02671900: adrp     x26, #0x5097000
0x02671904: mov      x0, x24
0x02671908: ldp      w1, w2, [x22, #0x78]
0x0267190C: ldr      x8, [x26, #0x6d8]
0x02671910: blr      x8
0x02671914: ldp      w1, w2, [x22, #0x80]
0x02671918: mov      w25, w0
0x0267191C: ldr      x8, [x26, #0x6d8]
0x02671920: mov      x0, x24
0x02671924: blr      x8
0x02671928: mov      w26, w0
0x0267192C: tbnz     w25, #0, #0x267193c
0x02671930: tbnz     w26, #0, #0x267193c
0x02671934: mov      w24, #1
0x02671938: b        #0x26719e8
0x0267193C: adrp     x28, #0x5097000
0x02671940: tbz      w25, #0, #0x2671968
0x02671944: ldp      w2, w3, [x22, #0x78]
0x02671948: ldr      x8, [x28, #0x6e8]
0x0267194C: mov      x0, x24
0x02671950: mov      w1, w21
0x02671954: blr      x8
0x02671958: mov      w27, w0
0x0267195C: tbnz     w26, #0, #0x2671970
0x02671960: mov      w0, #1
0x02671964: b        #0x2671984
0x02671968: mov      w27, #1
0x0267196C: tbz      w26, #0, #0x2671960
0x02671970: ldp      w2, w3, [x22, #0x80]
0x02671974: ldr      x8, [x28, #0x6e8]
0x02671978: mov      x0, x24
0x0267197C: mov      w1, w20
0x02671980: blr      x8
0x02671984: adrp     x8, #0x5098000
0x02671988: and      w24, w27, w0
0x0267198C: ldr      x8, [x8, #0x9f8]
0x02671990: blr      x8
0x02671994: ldp      w4, w5, [x19, #4]
0x02671998: ldp      w12, w10, [x22, #0x80]
0x0267199C: adrp     x1, #0x11c5000
0x026719A0: adrp     x2, #0x1207000
0x026719A4: ldr      w3, [x23]
0x026719A8: and      w7, w24, #1
0x026719AC: ldr      w6, [x19, #0x14]
0x026719B0: and      w9, w25, #1
0x026719B4: ldr      w8, [x22, #0x78]
0x026719B8: and      w11, w26, #1
0x026719BC: add      x1, x1, #0xaa8
0x026719C0: add      x2, x2, #0xa1
0x026719C4: str      w10, [sp, #0x38]
0x026719C8: str      w12, [sp, #0x30]
0x026719CC: str      w11, [sp, #0x28]
0x026719D0: str      w10, [sp, #0x20]
0x026719D4: str      w8, [sp, #0x18]
0x026719D8: str      w9, [sp, #0x10]
0x026719DC: str      w20, [sp, #8]
0x026719E0: str      w21, [sp]
0x026719E4: bl       #0x2185848
0x026719E8: and      w0, w24, #1
0x026719EC: ldr      x30, [sp, #0x40]
0x026719F0: ldp      x20, x19, [sp, #0x90]
0x026719F4: ldp      x22, x21, [sp, #0x80]
0x026719F8: ldp      x24, x23, [sp, #0x70]
0x026719FC: ldp      x26, x25, [sp, #0x60]
0x02671A00: ldp      x28, x27, [sp, #0x50]
0x02671A04: add      sp, sp, #0xa0
0x02671A08: ret      
~~~

### Function start 0x269330c
Hits: [{"pc": "0x26934c0", "adrp": "0x26934a0", "target": "0x12070a1", "label": "frame %d, mainCid %d, mainRid %d, camp %d, valid %d, visibleEnemyCnt %d, invisibleEnemyCnt %d, useVisibleRule %d, visibleFloor %d, visibleCeil %d, useInvisibleRule %d, invisibleFloor %d, invisibleCeil %d", "keywords": ["invisible", "invisible", "invisible"], "fde_start": "0x269330c", "fde_end": "0x269350c", "kind": "add", "reg": "x2"}]
~~~asm
0x0269330C: sub      sp, sp, #0xa0
0x02693310: str      x30, [sp, #0x40]
0x02693314: stp      x28, x27, [sp, #0x50]
0x02693318: stp      x26, x25, [sp, #0x60]
0x0269331C: stp      x24, x23, [sp, #0x70]
0x02693320: stp      x22, x21, [sp, #0x80]
0x02693324: stp      x20, x19, [sp, #0x90]
0x02693328: ldr      w8, [x3, #0x14]
0x0269332C: mov      x19, x3
0x02693330: mov      x23, x1
0x02693334: cmp      w8, #0
0x02693338: b.le     #0x26933c4
0x0269333C: ldp      x9, x10, [x23, #0x88]
0x02693340: mov      x22, x4
0x02693344: mov      x24, x0
0x02693348: cmp      x9, x10
0x0269334C: b.eq     #0x26933f8
0x02693350: sub      w13, w8, #1
0x02693354: mov      w14, #1
0x02693358: mov      w21, wzr
0x0269335C: mov      w20, wzr
0x02693360: sub      x11, x8, #1
0x02693364: lsr      x12, x13, #6
0x02693368: lsl      x13, x14, x13
0x0269336C: b        #0x269337c
0x02693370: add      x9, x9, #0x348
0x02693374: cmp      x9, x10
0x02693378: b.eq     #0x2693400
0x0269337C: ldr      w14, [x9, #0x14]
0x02693380: cmp      w14, w8
0x02693384: b.eq     #0x2693370
0x02693388: ldr      x14, [x9, #0x238]
0x0269338C: cmp      x11, x14
0x02693390: b.hs     #0x2693370
0x02693394: ldr      x14, [x9, #0x230]
0x02693398: ldr      w15, [x9, #0x48]
0x0269339C: ldr      x14, [x14, x12, lsl #3]
0x026933A0: cmp      w15, #1
0x026933A4: cset     w15, lt
0x026933A8: tst      x14, x13
0x026933AC: cset     w14, ne
0x026933B0: orr      w14, w15, w14
0x026933B4: eor      w15, w14, #1
0x026933B8: add      w21, w21, w14
0x026933BC: add      w20, w20, w15
0x026933C0: b        #0x2693370
0x026933C4: adrp     x8, #0x5098000
0x026933C8: ldr      x8, [x8, #0x9f8]
0x026933CC: blr      x8
0x026933D0: ldp      w4, w5, [x19, #4]
0x026933D4: adrp     x1, #0x11cb000
0x026933D8: adrp     x2, #0x1172000
0x026933DC: ldr      w3, [x23]
0x026933E0: add      x1, x1, #0xb15
0x026933E4: ldr      w6, [x19, #0x14]
0x026933E8: add      x2, x2, #0xbd8
0x026933EC: bl       #0x2185848
0x026933F0: mov      w24, #1
0x026933F4: b        #0x26934e8
0x026933F8: mov      w20, wzr
0x026933FC: mov      w21, wzr
0x02693400: adrp     x26, #0x5097000
0x02693404: mov      x0, x24
0x02693408: ldp      w1, w2, [x22, #0x78]
0x0269340C: ldr      x8, [x26, #0xd28]
0x02693410: blr      x8
0x02693414: ldp      w1, w2, [x22, #0x80]
0x02693418: mov      w25, w0
0x0269341C: ldr      x8, [x26, #0xd28]
0x02693420: mov      x0, x24
0x02693424: blr      x8
0x02693428: mov      w26, w0
0x0269342C: tbnz     w25, #0, #0x269343c
0x02693430: tbnz     w26, #0, #0x269343c
0x02693434: mov      w24, #1
0x02693438: b        #0x26934e8
0x0269343C: adrp     x28, #0x5097000
0x02693440: tbz      w25, #0, #0x2693468
0x02693444: ldp      w2, w3, [x22, #0x78]
0x02693448: ldr      x8, [x28, #0xd38]
0x0269344C: mov      x0, x24
0x02693450: mov      w1, w21
0x02693454: blr      x8
0x02693458: mov      w27, w0
0x0269345C: tbnz     w26, #0, #0x2693470
0x02693460: mov      w0, #1
0x02693464: b        #0x2693484
0x02693468: mov      w27, #1
0x0269346C: tbz      w26, #0, #0x2693460
0x02693470: ldp      w2, w3, [x22, #0x80]
0x02693474: ldr      x8, [x28, #0xd38]
0x02693478: mov      x0, x24
0x0269347C: mov      w1, w20
0x02693480: blr      x8
0x02693484: adrp     x8, #0x5098000
0x02693488: and      w24, w27, w0
0x0269348C: ldr      x8, [x8, #0x9f8]
0x02693490: blr      x8
0x02693494: ldp      w4, w5, [x19, #4]
0x02693498: ldp      w12, w10, [x22, #0x80]
0x0269349C: adrp     x1, #0x11cb000
0x026934A0: adrp     x2, #0x1207000
0x026934A4: ldr      w3, [x23]
0x026934A8: and      w7, w24, #1
0x026934AC: ldr      w6, [x19, #0x14]
0x026934B0: and      w9, w25, #1
0x026934B4: ldr      w8, [x22, #0x78]
0x026934B8: and      w11, w26, #1
0x026934BC: add      x1, x1, #0xb15
0x026934C0: add      x2, x2, #0xa1
0x026934C4: str      w10, [sp, #0x38]
0x026934C8: str      w12, [sp, #0x30]
0x026934CC: str      w11, [sp, #0x28]
0x026934D0: str      w10, [sp, #0x20]
0x026934D4: str      w8, [sp, #0x18]
0x026934D8: str      w9, [sp, #0x10]
0x026934DC: str      w20, [sp, #8]
0x026934E0: str      w21, [sp]
0x026934E4: bl       #0x2185848
0x026934E8: and      w0, w24, #1
0x026934EC: ldr      x30, [sp, #0x40]
0x026934F0: ldp      x20, x19, [sp, #0x90]
0x026934F4: ldp      x22, x21, [sp, #0x80]
0x026934F8: ldp      x24, x23, [sp, #0x70]
0x026934FC: ldp      x26, x25, [sp, #0x60]
0x02693500: ldp      x28, x27, [sp, #0x50]
0x02693504: add      sp, sp, #0xa0
0x02693508: ret      
~~~

### Function start 0x269dac8
Hits: [{"pc": "0x269e170", "adrp": "0x269e154", "target": "0x11dfac7", "label": "frame:%d rid=%d SKIP unit_invisible_time: friendly hero, range=[%d,%d]", "keywords": ["invisible"], "fde_start": "0x269dac8", "fde_end": "0x269ea98", "kind": "add", "reg": "x2"}, {"pc": "0x269e8dc", "adrp": "0x269e8c8", "target": "0x11795b8", "label": "frame:%d rid=%d SKIP unit_invisible_time: not seen yet since enqueue", "keywords": ["invisible"], "fde_start": "0x269dac8", "fde_end": "0x269ea98", "kind": "add", "reg": "x2"}, {"pc": "0x269e940", "adrp": "0x269e924", "target": "0x11dfb0e", "label": "frame:%d rid=%d SKIP unit_invisible_time: val=%d range=[%d,%d]", "keywords": ["invisible"], "fde_start": "0x269dac8", "fde_end": "0x269ea98", "kind": "add", "reg": "x2"}]
~~~asm
0x0269DAC8: sub      sp, sp, #0xd0
0x0269DACC: stp      x29, x30, [sp, #0x70]
0x0269DAD0: stp      x28, x27, [sp, #0x80]
0x0269DAD4: stp      x26, x25, [sp, #0x90]
0x0269DAD8: stp      x24, x23, [sp, #0xa0]
0x0269DADC: stp      x22, x21, [sp, #0xb0]
0x0269DAE0: stp      x20, x19, [sp, #0xc0]
0x0269DAE4: mov      x21, x4
0x0269DAE8: mov      x22, x3
0x0269DAEC: mov      x28, x2
0x0269DAF0: mov      x19, x1
0x0269DAF4: ldr      x8, [x4, #0x138]
0x0269DAF8: mov      x23, x0
0x0269DAFC: cbnz     x8, #0x269dbc0
0x0269DB00: adrp     x24, #0x5097000
0x0269DB04: ldr      w1, [x21, #0x140]
0x0269DB08: mov      x0, x23
0x0269DB0C: ldr      x8, [x24, #0xd18]
0x0269DB10: blr      x8
0x0269DB14: tbnz     w0, #0, #0x269dbc0
0x0269DB18: adrp     x20, #0x5097000
0x0269DB1C: ldr      w1, [x21, #0x144]
0x0269DB20: ldr      w2, [x21, #0x148]
0x0269DB24: mov      x0, x23
0x0269DB28: ldr      x8, [x20, #0xd28]
0x0269DB2C: blr      x8
0x0269DB30: tbnz     w0, #0, #0x269dbc0
0x0269DB34: ldr      w1, [x21, #0x14c]
0x0269DB38: mov      x0, x23
0x0269DB3C: ldr      x8, [x24, #0xd18]
0x0269DB40: blr      x8
0x0269DB44: tbnz     w0, #0, #0x269dbc0
0x0269DB48: ldr      w1, [x21, #0x150]
0x0269DB4C: mov      x0, x23
0x0269DB50: ldr      w2, [x21, #0x154]
0x0269DB54: ldr      x8, [x20, #0xd28]
0x0269DB58: blr      x8
0x0269DB5C: tbnz     w0, #0, #0x269dbc0
0x0269DB60: ldr      w1, [x21, #0x158]
0x0269DB64: mov      x0, x23
0x0269DB68: ldr      w2, [x21, #0x15c]
0x0269DB6C: ldr      x8, [x20, #0xd28]
0x0269DB70: blr      x8
0x0269DB74: tbnz     w0, #0, #0x269dbc0
0x0269DB78: ldr      w1, [x21, #0x160]
0x0269DB7C: mov      x0, x23
0x0269DB80: ldr      w2, [x21, #0x164]
0x0269DB84: ldr      x8, [x20, #0xd28]
0x0269DB88: blr      x8
0x0269DB8C: tbnz     w0, #0, #0x269dbc0
0x0269DB90: ldr      w1, [x21, #0x184]
0x0269DB94: mov      x0, x23
0x0269DB98: ldr      w2, [x21, #0x188]
0x0269DB9C: ldr      x8, [x20, #0xd28]
0x0269DBA0: blr      x8
0x0269DBA4: tbnz     w0, #0, #0x269dbc0
0x0269DBA8: ldr      w1, [x21, #0x18c]
0x0269DBAC: mov      x0, x23
0x0269DBB0: ldr      w2, [x21, #0x190]
0x0269DBB4: ldr      x8, [x20, #0xd28]
0x0269DBB8: blr      x8
0x0269DBBC: tbz      w0, #0, #0x269ea50
0x0269DBC0: ldp      x25, x8, [x19, #0x88]
0x0269DBC4: mov      w9, #0x8fd9
0x0269DBC8: adrp     x27, #0x5098000
0x0269DBCC: movk     w9, #0xd8fd, lsl #16
0x0269DBD0: sub      x8, x8, x25
0x0269DBD4: lsr      x8, x8, #3
0x0269DBD8: mul      w8, w8, w9
0x0269DBDC: cmp      w8, #1
0x0269DBE0: b.lt     #0x269e978
0x0269DBE4: add      x9, x23, #0x3a0
0x0269DBE8: add      x8, x22, #0x1c
0x0269DBEC: add      x10, x23, #0x3b8
0x0269DBF0: mov      x24, xzr
0x0269DBF4: add      x26, x21, #0x130
0x0269DBF8: str      x28, [sp, #0x18]
0x0269DBFC: stp      x8, x9, [sp, #0x20]
0x0269DC00: add      x8, sp, #0x58
0x0269DC04: add      x11, x8, #8
0x0269DC08: add      x8, x23, #8
0x0269DC0C: add      x9, x23, #0x340
0x0269DC10: str      x26, [sp, #0x40]
0x0269DC14: stp      x11, x8, [sp, #0x48]
0x0269DC18: add      x8, x23, #0x3b0
0x0269DC1C: stp      x8, x10, [sp, #8]
0x0269DC20: add      x8, x23, #0x338
0x0269DC24: stp      x8, x9, [sp, #0x30]
0x0269DC28: b        #0x269dc8c
0x0269DC2C: ldr      x8, [x27, #0x9f8]
0x0269DC30: blr      x8
0x0269DC34: mov      w8, #0x348
0x0269DC38: ldr      w3, [x19]
0x0269DC3C: ldr      w6, [x21, #0x150]
0x0269DC40: adrp     x1, #0x1145000
0x0269DC44: madd     x8, x24, x8, x25
0x0269DC48: ldr      w7, [x21, #0x154]
0x0269DC4C: adrp     x2, #0x1179000
0x0269DC50: add      x1, x1, #0x755
0x0269DC54: add      x2, x2, #0x5fd
0x0269DC58: ldr      w4, [x8, #8]
0x0269DC5C: mov      w5, w26
0x0269DC60: bl       #0x2185848
0x0269DC64: ldr      x26, [sp, #0x40]
0x0269DC68: ldp      x25, x8, [x19, #0x88]
0x0269DC6C: mov      w9, #0x8fd9
0x0269DC70: add      x24, x24, #1
0x0269DC74: movk     w9, #0xd8fd, lsl #16
0x0269DC78: sub      x8, x8, x25
0x0269DC7C: lsr      x8, x8, #3
0x0269DC80: mul      w8, w8, w9
0x0269DC84: cmp      x24, w8, sxtw
0x0269DC88: b.ge     #0x269e978
0x0269DC8C: ldr      x8, [x21, #0x138]
0x0269DC90: cbz      x8, #0x269dcd8
0x0269DC94: ldr      x8, [x26]
0x0269DC98: cbz      x8, #0x269dc68
0x0269DC9C: mov      w9, #0x348
0x0269DCA0: mov      x10, x26
0x0269DCA4: madd     x9, x24, x9, x25
0x0269DCA8: ldr      w9, [x9, #8]
0x0269DCAC: ldr      w11, [x8, #0x1c]
0x0269DCB0: cmp      w11, w9
0x0269DCB4: cset     w11, lt
0x0269DCB8: csel     x10, x10, x8, lt
0x0269DCBC: ldr      x8, [x8, w11, uxtw #3]
0x0269DCC0: cbnz     x8, #0x269dcac
0x0269DCC4: cmp      x10, x26
0x0269DCC8: b.eq     #0x269dc68
0x0269DCCC: ldr      w8, [x10, #0x1c]
0x0269DCD0: cmp      w9, w8
0x0269DCD4: b.lt     #0x269dc68
0x0269DCD8: adrp     x8, #0x5097000
0x0269DCDC: ldr      w1, [x21, #0x140]
0x0269DCE0: mov      x0, x23
0x0269DCE4: ldr      x8, [x8, #0xd18]
0x0269DCE8: blr      x8
0x0269DCEC: tbz      w0, #0, #0x269dd7c
0x0269DCF0: mov      w10, #0x348
0x0269DCF4: madd     x8, x24, x10, x25
0x0269DCF8: ldr      w9, [x8, #0x14]
0x0269DCFC: ldr      w8, [x22, #0x14]
0x0269DD00: cmp      w9, w8
0x0269DD04: b.eq     #0x269dd5c
0x0269DD08: madd     x9, x24, x10, x25
0x0269DD0C: ldr      w9, [x9, #0x48]
0x0269DD10: cmp      w9, #1
0x0269DD14: b.lt     #0x269dd5c
0x0269DD18: mov      w26, wzr
0x0269DD1C: subs     w8, w8, #1
0x0269DD20: b.mi     #0x269dd60
0x0269DD24: mov      w9, #0x348
0x0269DD28: sxtw     x8, w8
0x0269DD2C: madd     x9, x24, x9, x25
0x0269DD30: ldr      x9, [x9, #0x238]
0x0269DD34: cmp      x9, x8
0x0269DD38: b.ls     #0x269dd60
0x0269DD3C: mov      w9, #0x348
0x0269DD40: lsr      x10, x8, #3
0x0269DD44: and      x10, x10, #0x1ffffffffffffff8
0x0269DD48: madd     x9, x24, x9, x25
0x0269DD4C: ldr      x9, [x9, #0x230]
0x0269DD50: ldr      x9, [x9, x10]
0x0269DD54: lsr      x8, x9, x8
0x0269DD58: tbz      w8, #0, #0x269e378
0x0269DD5C: mov      w26, #1
0x0269DD60: adrp     x8, #0x5097000
0x0269DD64: ldr      w1, [x21, #0x140]
0x0269DD68: mov      x0, x23
0x0269DD6C: mov      w2, w26
0x0269DD70: ldr      x8, [x8, #0xd58]
0x0269DD74: blr      x8
0x0269DD78: tbz      w0, #0, #0x269ded8
0x0269DD7C: adrp     x8, #0x5097000
0x0269DD80: ldr      w1, [x21, #0x144]
0x0269DD84: ldr      w2, [x21, #0x148]
0x0269DD88: mov      x0, x23
0x0269DD8C: ldr      x8, [x8, #0xd28]
0x0269DD90: blr      x8
0x0269DD94: tbz      w0, #0, #0x269ddd0
0x0269DD98: mov      w11, #0x348
0x0269DD9C: madd     x8, x24, x11, x25
0x0269DDA0: ldr      w9, [x8, #0x14]
0x0269DDA4: ldr      w8, [x22, #0x14]
0x0269DDA8: cmp      w9, w8
0x0269DDAC: b.ne     #0x269df6c
0x0269DDB0: adrp     x8, #0x5097000
0x0269DDB4: ldr      w2, [x21, #0x144]
0x0269DDB8: ldr      w3, [x21, #0x148]
0x0269DDBC: mov      x0, x23
0x0269DDC0: mov      w1, wzr
0x0269DDC4: ldr      x8, [x8, #0xd38]
0x0269DDC8: blr      x8
0x0269DDCC: tbz      w0, #0, #0x269e144
0x0269DDD0: adrp     x8, #0x5097000
0x0269DDD4: ldr      w1, [x21, #0x14c]
0x0269DDD8: mov      x0, x23
0x0269DDDC: ldr      x8, [x8, #0xd18]
0x0269DDE0: blr      x8
0x0269DDE4: tbz      w0, #0, #0x269de14
0x0269DDE8: mov      w8, #0x348
0x0269DDEC: ldr      w1, [x21, #0x14c]
0x0269DDF0: mov      x0, x23
0x0269DDF4: madd     x20, x24, x8, x25
0x0269DDF8: adrp     x8, #0x5097000
0x0269DDFC: ldr      x8, [x8, #0xd58]
0x0269DE00: ldr      w26, [x20, #0x48]!
0x0269DE04: cmp      w26, #0
0x0269DE08: cset     w2, gt
0x0269DE0C: blr      x8
0x0269DE10: tbz      w0, #0, #0x269e00c
0x0269DE14: adrp     x8, #0x5097000
0x0269DE18: ldr      w1, [x21, #0x150]
0x0269DE1C: ldr      w2, [x21, #0x154]
0x0269DE20: mov      x0, x23
0x0269DE24: ldr      x8, [x8, #0xd28]
0x0269DE28: blr      x8
0x0269DE2C: tbz      w0, #0, #0x269e084
0x0269DE30: ldp      x9, x8, [x19, #0x88]
0x0269DE34: mov      w11, #0x8fd9
0x0269DE38: movk     w11, #0xd8fd, lsl #16
0x0269DE3C: sub      x10, x8, x9
0x0269DE40: lsr      x10, x10, #3
0x0269DE44: mul      w10, w10, w11
0x0269DE48: cmp      w10, #1
0x0269DE4C: b.lt     #0x269e060
0x0269DE50: mov      w10, #0x348
0x0269DE54: mov      x27, xzr
0x0269DE58: mov      w26, #-1
0x0269DE5C: mov      w20, #0x14
0x0269DE60: madd     x10, x24, x10, x25
0x0269DE64: add      x29, x10, #0x1c
0x0269DE68: b        #0x269de90
0x0269DE6C: sub      x10, x8, x9
0x0269DE70: mov      w11, #0x8fd9
0x0269DE74: lsr      x10, x10, #3
0x0269DE78: movk     w11, #0xd8fd, lsl #16
0x0269DE7C: add      x27, x27, #1
0x0269DE80: add      x20, x20, #0x348
0x0269DE84: mul      w10, w10, w11
~~~

### Function start 0x269efdc
Hits: [{"pc": "0x269febc", "adrp": "0x269feb4", "target": "0x11c5cda", "label": "hero_state.invisible_enemy_cnt_floor", "keywords": ["invisible"], "fde_start": "0x269efdc", "fde_end": "0x26a5db8", "kind": "add", "reg": "x1"}, {"pc": "0x269ff70", "adrp": "0x269ff68", "target": "0x1192f25", "label": "hero_state.invisible_enemy_cnt_ceil", "keywords": ["invisible"], "fde_start": "0x269efdc", "fde_end": "0x26a5db8", "kind": "add", "reg": "x1"}]
~~~asm
0x0269EFDC: sub      sp, sp, #0x90
0x0269EFE0: stp      x29, x30, [sp, #0x30]
0x0269EFE4: stp      x28, x27, [sp, #0x40]
0x0269EFE8: stp      x26, x25, [sp, #0x50]
0x0269EFEC: stp      x24, x23, [sp, #0x60]
0x0269EFF0: stp      x22, x21, [sp, #0x70]
0x0269EFF4: stp      x20, x19, [sp, #0x80]
0x0269EFF8: adrp     x8, #0x5098000
0x0269EFFC: mov      x20, x2
0x0269F000: mov      x19, x1
0x0269F004: ldr      x8, [x8, #0x9f8]
0x0269F008: blr      x8
0x0269F00C: adrp     x1, #0x11cb000
0x0269F010: adrp     x2, #0x11b9000
0x0269F014: ldr      w3, [x19]
0x0269F018: add      x1, x1, #0xbc2
0x0269F01C: add      x2, x2, #0x3ae
0x0269F020: bl       #0x2185848
0x0269F024: ldrb     w8, [x20]
0x0269F028: stp      xzr, xzr, [sp, #0x18]
0x0269F02C: ldp      x9, x10, [x20, #8]
0x0269F030: str      xzr, [sp, #0x28]
0x0269F034: lsr      x11, x8, #1
0x0269F038: tst      w8, #1
0x0269F03C: csel     x21, x11, x9, eq
0x0269F040: csinc    x22, x10, x20, ne
0x0269F044: add      x8, x21, #7
0x0269F048: cmn      x8, #0x10
0x0269F04C: b.hs     #0x26a56b0
0x0269F050: cmp      x8, #0x17
0x0269F054: b.hs     #0x269f070
0x0269F058: add      x9, sp, #0x18
0x0269F05C: lsl      w8, w21, #1
0x0269F060: orr      x23, x9, #1
0x0269F064: strb     w8, [sp, #0x18]
0x0269F068: cbnz     x21, #0x269f090
0x0269F06C: b        #0x269f0a0
0x0269F070: add      x8, x21, #0x17
0x0269F074: and      x24, x8, #0xfffffffffffffff0
0x0269F078: mov      x0, x24
0x0269F07C: bl       #0x4b40050
0x0269F080: orr      x8, x24, #1
0x0269F084: mov      x23, x0
0x0269F088: stp      x21, x0, [sp, #0x20]
0x0269F08C: str      x8, [sp, #0x18]
0x0269F090: mov      x0, x23
0x0269F094: mov      x1, x22
0x0269F098: mov      x2, x21
0x0269F09C: bl       #0x4b405c0
0x0269F0A0: strb     wzr, [x23, x21]
0x0269F0A4: adrp     x1, #0x11ec000
0x0269F0A8: add      x0, sp, #0x18
0x0269F0AC: add      x1, x1, #0xdf9
0x0269F0B0: mov      w2, #7
0x0269F0B4: bl       #0x2282a80
0x0269F0B8: adrp     x25, #0x5237000
0x0269F0BC: ldr      x8, [x25, #0xb20]
0x0269F0C0: add      x0, sp, #0x18
0x0269F0C4: mov      x1, x19
0x0269F0C8: blr      x8
0x0269F0CC: ldrb     w8, [sp, #0x18]
0x0269F0D0: add      x27, x20, #1
0x0269F0D4: tbz      w8, #0, #0x269f0e0
0x0269F0D8: ldr      x0, [sp, #0x28]
0x0269F0DC: bl       #0x4b3fb60
0x0269F0E0: ldrb     w8, [x20]
0x0269F0E4: stp      xzr, xzr, [sp, #0x18]
0x0269F0E8: ldp      x9, x10, [x20, #8]
0x0269F0EC: str      xzr, [sp, #0x28]
0x0269F0F0: lsr      x11, x8, #1
0x0269F0F4: tst      w8, #1
0x0269F0F8: csel     x21, x11, x9, eq
0x0269F0FC: csel     x22, x27, x10, eq
0x0269F100: add      x8, x21, #0xf
0x0269F104: cmn      x8, #0x10
0x0269F108: b.hs     #0x26a56b4
0x0269F10C: cmp      x8, #0x17
0x0269F110: b.hs     #0x269f12c
0x0269F114: add      x9, sp, #0x18
0x0269F118: lsl      w8, w21, #1
0x0269F11C: orr      x23, x9, #1
0x0269F120: strb     w8, [sp, #0x18]
0x0269F124: cbnz     x21, #0x269f14c
0x0269F128: b        #0x269f15c
0x0269F12C: add      x8, x21, #0x1f
0x0269F130: and      x24, x8, #0xfffffffffffffff0
0x0269F134: mov      x0, x24
0x0269F138: bl       #0x4b40050
0x0269F13C: orr      x8, x24, #1
0x0269F140: mov      x23, x0
0x0269F144: stp      x21, x0, [sp, #0x20]
0x0269F148: str      x8, [sp, #0x18]
0x0269F14C: mov      x0, x23
0x0269F150: mov      x1, x22
0x0269F154: mov      x2, x21
0x0269F158: bl       #0x4b405c0
0x0269F15C: strb     wzr, [x23, x21]
0x0269F160: adrp     x1, #0x113e000
0x0269F164: add      x0, sp, #0x18
0x0269F168: add      x1, x1, #0xdb8
0x0269F16C: mov      w2, #0xf
0x0269F170: bl       #0x2282a80
0x0269F174: add      x1, x19, #4
0x0269F178: ldr      x8, [x25, #0xb20]
0x0269F17C: add      x0, sp, #0x18
0x0269F180: blr      x8
0x0269F184: ldrb     w8, [sp, #0x18]
0x0269F188: tbz      w8, #0, #0x269f194
0x0269F18C: ldr      x0, [sp, #0x28]
0x0269F190: bl       #0x4b3fb60
0x0269F194: ldrb     w8, [x20]
0x0269F198: stp      xzr, xzr, [sp, #0x18]
0x0269F19C: ldp      x9, x10, [x20, #8]
0x0269F1A0: str      xzr, [sp, #0x28]
0x0269F1A4: lsr      x11, x8, #1
0x0269F1A8: tst      w8, #1
0x0269F1AC: csel     x21, x11, x9, eq
0x0269F1B0: csel     x22, x27, x10, eq
0x0269F1B4: add      x8, x21, #0xa
0x0269F1B8: cmn      x8, #0x10
0x0269F1BC: b.hs     #0x26a56b8
0x0269F1C0: cmp      x8, #0x17
0x0269F1C4: b.hs     #0x269f1e0
0x0269F1C8: add      x9, sp, #0x18
0x0269F1CC: lsl      w8, w21, #1
0x0269F1D0: orr      x23, x9, #1
0x0269F1D4: strb     w8, [sp, #0x18]
0x0269F1D8: cbnz     x21, #0x269f200
0x0269F1DC: b        #0x269f210
0x0269F1E0: add      x8, x21, #0x1a
0x0269F1E4: and      x24, x8, #0xfffffffffffffff0
0x0269F1E8: mov      x0, x24
0x0269F1EC: bl       #0x4b40050
0x0269F1F0: orr      x8, x24, #1
0x0269F1F4: mov      x23, x0
0x0269F1F8: stp      x21, x0, [sp, #0x20]
0x0269F1FC: str      x8, [sp, #0x18]
0x0269F200: mov      x0, x23
0x0269F204: mov      x1, x22
0x0269F208: mov      x2, x21
0x0269F20C: bl       #0x4b405c0
0x0269F210: strb     wzr, [x23, x21]
0x0269F214: adrp     x1, #0x11c5000
0x0269F218: add      x0, sp, #0x18
0x0269F21C: add      x1, x1, #0xc9d
0x0269F220: mov      w2, #0xa
0x0269F224: bl       #0x2282a80
0x0269F228: add      x1, x19, #8
0x0269F22C: ldr      x8, [x25, #0xb20]
0x0269F230: add      x0, sp, #0x18
0x0269F234: blr      x8
0x0269F238: ldrb     w8, [sp, #0x18]
0x0269F23C: tbz      w8, #0, #0x269f248
0x0269F240: ldr      x0, [sp, #0x28]
0x0269F244: bl       #0x4b3fb60
0x0269F248: ldrb     w8, [x20]
0x0269F24C: stp      xzr, xzr, [sp, #0x18]
0x0269F250: ldp      x9, x10, [x20, #8]
0x0269F254: str      xzr, [sp, #0x28]
0x0269F258: lsr      x11, x8, #1
0x0269F25C: tst      w8, #1
0x0269F260: csel     x21, x11, x9, eq
0x0269F264: csel     x22, x27, x10, eq
0x0269F268: add      x8, x21, #9
0x0269F26C: cmn      x8, #0x10
0x0269F270: b.hs     #0x26a56bc
0x0269F274: cmp      x8, #0x17
0x0269F278: b.hs     #0x269f294
0x0269F27C: add      x9, sp, #0x18
0x0269F280: lsl      w8, w21, #1
0x0269F284: orr      x23, x9, #1
0x0269F288: strb     w8, [sp, #0x18]
0x0269F28C: cbnz     x21, #0x269f2b4
0x0269F290: b        #0x269f2c4
0x0269F294: add      x8, x21, #0x19
0x0269F298: and      x24, x8, #0xfffffffffffffff0
0x0269F29C: mov      x0, x24
0x0269F2A0: bl       #0x4b40050
0x0269F2A4: orr      x8, x24, #1
0x0269F2A8: mov      x23, x0
0x0269F2AC: stp      x21, x0, [sp, #0x20]
0x0269F2B0: str      x8, [sp, #0x18]
0x0269F2B4: mov      x0, x23
0x0269F2B8: mov      x1, x22
0x0269F2BC: mov      x2, x21
0x0269F2C0: bl       #0x4b405c0
0x0269F2C4: strb     wzr, [x23, x21]
0x0269F2C8: adrp     x1, #0x11cb000
0x0269F2CC: add      x0, sp, #0x18
0x0269F2D0: add      x1, x1, #0xbff
0x0269F2D4: mov      w2, #9
0x0269F2D8: bl       #0x2282a80
0x0269F2DC: add      x1, x19, #0xc
0x0269F2E0: ldr      x8, [x25, #0xb20]
0x0269F2E4: add      x0, sp, #0x18
0x0269F2E8: blr      x8
0x0269F2EC: ldrb     w8, [sp, #0x18]
0x0269F2F0: tbz      w8, #0, #0x269f2fc
0x0269F2F4: ldr      x0, [sp, #0x28]
0x0269F2F8: bl       #0x4b3fb60
0x0269F2FC: ldrb     w8, [x20]
0x0269F300: stp      xzr, xzr, [sp, #0x18]
0x0269F304: ldp      x9, x10, [x20, #8]
0x0269F308: str      xzr, [sp, #0x28]
0x0269F30C: lsr      x11, x8, #1
0x0269F310: tst      w8, #1
0x0269F314: csel     x21, x11, x9, eq
0x0269F318: csel     x22, x27, x10, eq
0x0269F31C: add      x8, x21, #0xf
0x0269F320: cmn      x8, #0x10
0x0269F324: b.hs     #0x26a56c0
0x0269F328: cmp      x8, #0x17
0x0269F32C: b.hs     #0x269f348
0x0269F330: add      x9, sp, #0x18
0x0269F334: lsl      w8, w21, #1
0x0269F338: orr      x23, x9, #1
0x0269F33C: strb     w8, [sp, #0x18]
0x0269F340: cbnz     x21, #0x269f368
0x0269F344: b        #0x269f378
0x0269F348: add      x8, x21, #0x1f
0x0269F34C: and      x24, x8, #0xfffffffffffffff0
0x0269F350: mov      x0, x24
0x0269F354: bl       #0x4b40050
0x0269F358: orr      x8, x24, #1
0x0269F35C: mov      x23, x0
0x0269F360: stp      x21, x0, [sp, #0x20]
0x0269F364: str      x8, [sp, #0x18]
0x0269F368: mov      x0, x23
0x0269F36C: mov      x1, x22
0x0269F370: mov      x2, x21
0x0269F374: bl       #0x4b405c0
0x0269F378: strb     wzr, [x23, x21]
0x0269F37C: adrp     x1, #0x1198000
0x0269F380: add      x0, sp, #0x18
0x0269F384: add      x1, x1, #0xe48
0x0269F388: mov      w2, #0xf
0x0269F38C: bl       #0x2282a80
0x0269F390: add      x1, x19, #0x10
0x0269F394: ldr      x8, [x25, #0xb20]
0x0269F398: add      x0, sp, #0x18
~~~

### Function start 0x26cb1a8
Hits: [{"pc": "0x26cdc70", "adrp": "0x26cdc68", "target": "0x11d8792", "label": "invisible_range", "keywords": ["invisible"], "fde_start": "0x26cb1a8", "fde_end": "0x26cf18c", "kind": "add", "reg": "x1"}, {"pc": "0x26cdcac", "adrp": "0x26cdca4", "target": "0x11d8792", "label": "invisible_range", "keywords": ["invisible"], "fde_start": "0x26cb1a8", "fde_end": "0x26cf18c", "kind": "add", "reg": "x1"}]
~~~asm
0x026CB1A8: stp      x29, x30, [sp, #-0x60]!
0x026CB1AC: stp      x28, x27, [sp, #0x10]
0x026CB1B0: stp      x26, x25, [sp, #0x20]
0x026CB1B4: stp      x24, x23, [sp, #0x30]
0x026CB1B8: stp      x22, x21, [sp, #0x40]
0x026CB1BC: stp      x20, x19, [sp, #0x50]
0x026CB1C0: sub      sp, sp, #0x1c0
0x026CB1C4: ldr      w8, [sp, #0x268]
0x026CB1C8: adrp     x9, #0x5098000
0x026CB1CC: ldr      w29, [sp, #0x228]
0x026CB1D0: str      x7, [sp, #0xb0]
0x026CB1D4: ldr      w21, [sp, #0x220]
0x026CB1D8: str      w5, [sp, #0xb8]
0x026CB1DC: stp      w6, w8, [sp, #0x78]
0x026CB1E0: mov      w8, #0x2924
0x026CB1E4: add      x8, x0, x8
0x026CB1E8: ldr      w19, [sp, #0x260]
0x026CB1EC: ldrb     w28, [sp, #0x238]
0x026CB1F0: str      w4, [sp, #0xd0]
0x026CB1F4: ldr      w20, [sp, #0x230]
0x026CB1F8: mov      w26, w3
0x026CB1FC: str      x8, [sp, #0xa8]
0x026CB200: ldr      x8, [x9, #0x9f8]
0x026CB204: ldr      w24, [sp, #0x248]
0x026CB208: str      x2, [sp, #0xc0]
0x026CB20C: ldr      w25, [sp, #0x250]
0x026CB210: str      w1, [sp, #0x80]
0x026CB214: ldr      w27, [sp, #0x258]
0x026CB218: mov      x23, x0
0x026CB21C: ldr      w22, [sp, #0x240]
0x026CB220: blr      x8
0x026CB224: adrp     x1, #0x11cb000
0x026CB228: adrp     x2, #0x1159000
0x026CB22C: add      x1, x1, #0xda6
0x026CB230: add      x2, x2, #0x444
0x026CB234: mov      w3, w26
0x026CB238: mov      w4, w21
0x026CB23C: mov      w5, w29
0x026CB240: ldr      w6, [sp, #0xd0]
0x026CB244: mov      w7, w20
0x026CB248: str      w22, [sp, #0x18]
0x026CB24C: str      w21, [sp, #0x98]
0x026CB250: str      w29, [sp, #0xa0]
0x026CB254: str      w27, [sp, #0x10]
0x026CB258: str      w25, [sp, #8]
0x026CB25C: str      w24, [sp]
0x026CB260: bl       #0x2185848
0x026CB264: cmp      w19, #0x1a
0x026CB268: ldr      w9, [x23, #0xb44]
0x026CB26C: cset     w8, lt
0x026CB270: str      w20, [x23, #0xb34]
0x026CB274: strb     w28, [x23, #0xb40]
0x026CB278: str      w22, [x23, #0x2bb8]
0x026CB27C: str      w27, [x23, #0x2a98]
0x026CB280: str      w24, [x23, #0x29f8]
0x026CB284: str      w25, [x23, #0x29fc]
0x026CB288: str      w19, [x23, #0xa20]
0x026CB28C: str      w8, [x23, #0xa24]
0x026CB290: cbnz     w9, #0x26cb2c4
0x026CB294: ldr      w0, [sp, #0x80]
0x026CB298: bl       #0x4b40380
0x026CB29C: bl       #0x4b40370
0x026CB2A0: mov      w8, #0x851f
0x026CB2A4: movk     w8, #0x51eb, lsl #16
0x026CB2A8: smull    x8, w0, w8
0x026CB2AC: lsr      x9, x8, #0x3f
0x026CB2B0: asr      x8, x8, #0x25
0x026CB2B4: add      w8, w8, w9
0x026CB2B8: mov      w9, #0x64
0x026CB2BC: msub     w8, w8, w9, w0
0x026CB2C0: str      w8, [x23, #0xb44]
0x026CB2C4: ands     w24, w26, #0xfffffffd
0x026CB2C8: mov      w21, w26
0x026CB2CC: b.eq     #0x26cb2e4
0x026CB2D0: adrp     x25, #0x5098000
0x026CB2D4: cmp      w21, #1
0x026CB2D8: b.ls     #0x26cb378
0x026CB2DC: mov      w0, #1
0x026CB2E0: b        #0x26cecac
0x026CB2E4: mov      w8, #0x2a10
0x026CB2E8: ldr      x1, [sp, #0xb0]
0x026CB2EC: add      x26, x23, x8
0x026CB2F0: ldr      w20, [sp, #0x270]
0x026CB2F4: mov      x0, x26
0x026CB2F8: ldr      w19, [sp, #0x278]
0x026CB2FC: bl       #0x2282510
0x026CB300: adrp     x25, #0x5098000
0x026CB304: ldr      w9, [sp, #0x98]
0x026CB308: ldr      x8, [x25, #0x9f8]
0x026CB30C: str      w9, [x23, #0x2a28]
0x026CB310: ldr      w9, [sp, #0xa0]
0x026CB314: str      w9, [x23, #0x2a2c]
0x026CB318: blr      x8
0x026CB31C: adrp     x8, #0x5098000
0x026CB320: ldr      w2, [x23, #0x2a28]
0x026CB324: ldr      w3, [x23, #0x2a2c]
0x026CB328: mov      x1, x26
0x026CB32C: mov      w4, wzr
0x026CB330: ldr      x8, [x8, #0x9c8]
0x026CB334: blr      x8
0x026CB338: ldr      x8, [x25, #0x9f8]
0x026CB33C: blr      x8
0x026CB340: adrp     x8, #0x5098000
0x026CB344: mov      w1, w20
0x026CB348: ldr      x8, [x8, #0x9d8]
0x026CB34C: blr      x8
0x026CB350: ldr      w8, [sp, #0xb8]
0x026CB354: str      w19, [x23, #0xbd4]
0x026CB358: tbz      w8, #0, #0x26cb364
0x026CB35C: mov      w8, #1
0x026CB360: str      w8, [x23, #0xbcc]
0x026CB364: movi     v0.2s, #1
0x026CB368: ldr      x8, [sp, #0xa8]
0x026CB36C: cmp      w21, #2
0x026CB370: str      d0, [x8, #0x110]
0x026CB374: b.hs     #0x26cec6c
0x026CB378: adrp     x8, #0x5178000
0x026CB37C: mov      w10, #0x1268
0x026CB380: add      x3, x23, x10
0x026CB384: mov      w10, #0x1910
0x026CB388: mov      w9, #0x3d02
0x026CB38C: add      x0, x23, x10
0x026CB390: ldr      x8, [x8, #0xb70]
0x026CB394: strb     wzr, [sp, #0x152]
0x026CB398: strh     w9, [sp, #0x150]
0x026CB39C: add      x2, sp, #0x150
0x026CB3A0: ldr      x1, [sp, #0xc0]
0x026CB3A4: str      x0, [sp, #0xd0]
0x026CB3A8: str      x3, [sp, #0xb0]
0x026CB3AC: blr      x8
0x026CB3B0: mov      w26, w0
0x026CB3B4: ldrb     w8, [sp, #0x150]
0x026CB3B8: tbz      w8, #0, #0x26cb3c4
0x026CB3BC: ldr      x0, [sp, #0x160]
0x026CB3C0: bl       #0x4b3fb60
0x026CB3C4: tbz      w26, #0, #0x26cb4c8
0x026CB3C8: ldr      x9, [sp, #0xa8]
0x026CB3CC: mov      w8, #0x120a
0x026CB3D0: add      x8, x23, x8
0x026CB3D4: add      x27, sp, #0x150
0x026CB3D8: str      wzr, [x23, #0x120c]
0x026CB3DC: strb     wzr, [x9, #0x11c]
0x026CB3E0: ldr      x9, [x25, #0x9f8]
0x026CB3E4: strb     wzr, [x8]
0x026CB3E8: strb     wzr, [x8, #6]
0x026CB3EC: blr      x9
0x026CB3F0: adrp     x20, #0x5098000
0x026CB3F4: mov      w1, #0xa
0x026CB3F8: ldr      x8, [x20, #0x9a8]
0x026CB3FC: blr      x8
0x026CB400: adrp     x8, #0x11a6000
0x026CB404: ldr      x26, [sp, #0xb0]
0x026CB408: add      x8, x8, #0x942
0x026CB40C: mov      w19, #0x12
0x026CB410: mov      w22, #0x6c
0x026CB414: add      x1, sp, #0x150
0x026CB418: mov      x0, x26
0x026CB41C: ldr      x21, [x8]
0x026CB420: add      x8, sp, #0x52
0x026CB424: strb     w19, [sp, #0x150]
0x026CB428: sturh    w22, [x27, #9]
0x026CB42C: stur     x21, [x8, #0xff]
0x026CB430: bl       #0x227e510
0x026CB434: mov      w8, #0x1270
0x026CB438: add      x8, x23, x8
0x026CB43C: cmp      x8, x0
0x026CB440: str      x8, [sp, #0xb8]
0x026CB444: b.eq     #0x26cb4d0
0x026CB448: add      x8, sp, #0x52
0x026CB44C: add      x1, sp, #0x1a8
0x026CB450: add      x2, sp, #0x150
0x026CB454: mov      x0, x26
0x026CB458: strb     w19, [sp, #0x150]
0x026CB45C: sturh    w22, [x27, #9]
0x026CB460: stur     x21, [x8, #0xff]
0x026CB464: bl       #0x227e070
0x026CB468: ldr      x27, [x0]
0x026CB46C: cbnz     x27, #0x26cb4f0
0x026CB470: mov      x26, x0
0x026CB474: mov      w0, #0x50
0x026CB478: bl       #0x4b40050
0x026CB47C: ldr      x8, [sp, #0x160]
0x026CB480: str      xzr, [sp, #0x160]
0x026CB484: ldr      q0, [sp, #0x150]
0x026CB488: stp      xzr, xzr, [sp, #0x150]
0x026CB48C: ldr      x9, [sp, #0xb0]
0x026CB490: stp      xzr, xzr, [x0, #0x40]
0x026CB494: stp      x8, xzr, [x0, #0x30]
0x026CB498: ldr      x8, [sp, #0x1a8]
0x026CB49C: str      q0, [x0, #0x20]
0x026CB4A0: mov      x27, x0
0x026CB4A4: stp      xzr, xzr, [x0]
0x026CB4A8: str      x8, [x0, #0x10]
0x026CB4AC: str      x0, [x26]
0x026CB4B0: ldr      x8, [x9]
0x026CB4B4: ldr      x8, [x8]
0x026CB4B8: cbz      x8, #0x26cb4d8
0x026CB4BC: str      x8, [x9]
0x026CB4C0: ldr      x1, [x26]
0x026CB4C4: b        #0x26cb4dc
0x026CB4C8: mov      w0, wzr
0x026CB4CC: b        #0x26cecac
0x026CB4D0: mov      w26, wzr
0x026CB4D4: b        #0x26cb50c
0x026CB4D8: mov      x1, x27
0x026CB4DC: ldr      x0, [x23, #0x1270]
0x026CB4E0: bl       #0x2260c4c
0x026CB4E4: ldr      x8, [x23, #0x1278]
0x026CB4E8: add      x8, x8, #1
0x026CB4EC: str      x8, [x23, #0x1278]
0x026CB4F0: ldrb     w8, [x27, #0x38]
0x026CB4F4: add      x10, x27, #0x39
0x026CB4F8: ldr      x9, [x27, #0x48]
0x026CB4FC: tst      w8, #1
0x026CB500: csel     x0, x10, x9, eq
0x026CB504: bl       #0x4b400f0
0x026CB508: mov      w26, w0
0x026CB50C: ldr      x8, [x25, #0x9f8]
0x026CB510: blr      x8
0x026CB514: ldr      x8, [x20, #0x9a8]
0x026CB518: mov      w1, w26
0x026CB51C: blr      x8
0x026CB520: mov      w20, #0x7067
0x026CB524: add      x8, sp, #0x52
0x026CB528: movk     w20, #0x5f75, lsl #16
0x026CB52C: ldr      x26, [sp, #0xb0]
0x026CB530: mov      w19, #0xc
0x026CB534: mov      w21, #0x6469
0x026CB538: add      x1, sp, #0x150
0x026CB53C: str      wzr, [x23, #0xad4]
0x026CB540: stur     w20, [x8, #0xff]
0x026CB544: add      x8, sp, #0x56
0x026CB548: mov      x0, x26
0x026CB54C: strb     w19, [sp, #0x150]
0x026CB550: strb     wzr, [sp, #0x157]
0x026CB554: sturh    w21, [x8, #0xff]
0x026CB558: bl       #0x227e510
0x026CB55C: ldr      x8, [sp, #0xb8]
0x026CB560: cmp      x8, x0
0x026CB564: b.eq     #0x26cb648
~~~

### Function start 0x26d54fc
Hits: [{"pc": "0x26d55d0", "adrp": "0x26d55c0", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x1"}, {"pc": "0x26d5ac0", "adrp": "0x26d5ab4", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x1"}, {"pc": "0x26d5ac4", "adrp": "0x26d5ab8", "target": "0x11ac0c5", "label": "mian_hero [%d-%d-%d] tgt_hero [%d-%d-%d] cur_frame %d, last_invisible_ingrass %d --> visible_ingrass less than 6 frame", "keywords": ["invisible"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x2"}, {"pc": "0x26d5b34", "adrp": "0x26d5b2c", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x1"}, {"pc": "0x26d5b38", "adrp": "0x26d5b30", "target": "0x118d061", "label": "hero:%d invisible2visible", "keywords": ["invisible"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x2"}, {"pc": "0x26d5c1c", "adrp": "0x26d5c0c", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x1"}, {"pc": "0x26d5c24", "adrp": "0x26d5c14", "target": "0x116c7eb", "label": "lanlingwang use skill3, invisible, real_location = (%d,%d), main_hero_location = (%d, %d)", "keywords": ["real_location", "invisible"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x2"}, {"pc": "0x26d5e04", "adrp": "0x26d5df8", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x1"}, {"pc": "0x26d5e0c", "adrp": "0x26d5dfc", "target": "0x11b25de", "label": "ake use skill3, invisible, real_location = (%d,%d), modify to (%d,%d)", "keywords": ["real_location", "invisible"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x2"}, {"pc": "0x26d5e60", "adrp": "0x26d5e58", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x1"}, {"pc": "0x26d5e80", "adrp": "0x26d5e7c", "target": "0x11dfda4", "label": "lanlingwang use skill3, invisible and far to main hero, real location = (%d, %d), modified location = (50000, 50000), main_hero_location = (%d, %d)", "keywords": ["invisible"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x2"}, {"pc": "0x26d5f20", "adrp": "0x26d5f18", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x23"}, {"pc": "0x26d5f38", "adrp": "0x26d5f24", "target": "0x119f627", "label": "ake use skill3, invisible and dist to main hero < 100, real location = (%d, %d), main_hero_location = (%d, %d)", "keywords": ["invisible"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x2"}, {"pc": "0x26d5f94", "adrp": "0x26d5f80", "target": "0x119f696", "label": "ake use skill3, invisible and dist to main hero < 100, modified_location = (%d, %d), main_hero_location = (%d, %d)", "keywords": ["invisible"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x2"}, {"pc": "0x26d6014", "adrp": "0x26d6004", "target": "0x11e6222", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPosition", "keywords": ["ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d54fc", "fde_end": "0x26d6380", "kind": "add", "reg": "x1"}]
~~~asm
0x026D54FC: sub      sp, sp, #0x130
0x026D5500: stp      d11, d10, [sp, #0xb0]
0x026D5504: stp      d9, d8, [sp, #0xc0]
0x026D5508: stp      x29, x30, [sp, #0xd0]
0x026D550C: stp      x28, x27, [sp, #0xe0]
0x026D5510: stp      x26, x25, [sp, #0xf0]
0x026D5514: stp      x24, x23, [sp, #0x100]
0x026D5518: stp      x22, x21, [sp, #0x110]
0x026D551C: stp      x20, x19, [sp, #0x120]
0x026D5520: ldp      x29, x8, [x1, #0x88]
0x026D5524: str      x0, [sp, #0x90]
0x026D5528: cmp      x29, x8
0x026D552C: b.eq     #0x26d6354
0x026D5530: ldr      x11, [sp, #0x90]
0x026D5534: mov      w9, #0x348
0x026D5538: ldrsw    x8, [x1, #0x18]
0x026D553C: mov      x24, x2
0x026D5540: mov      x19, x1
0x026D5544: str      x2, [sp, #0x88]
0x026D5548: add      x10, x11, #0x9e0
0x026D554C: madd     x8, x8, x9, x29
0x026D5550: add      x9, x11, #0x9e8
0x026D5554: str      x10, [sp, #0x70]
0x026D5558: mov      w10, #0x2210
0x026D555C: str      x9, [sp, #0x80]
0x026D5560: add      x9, x11, x10
0x026D5564: add      x10, x8, #4
0x026D5568: add      x25, x8, #0x14
0x026D556C: str      x9, [sp, #0x68]
0x026D5570: add      x9, x8, #0x1c
0x026D5574: str      x9, [sp, #0x98]
0x026D5578: add      x9, x8, #8
0x026D557C: str      x9, [sp, #0x40]
0x026D5580: add      x9, x8, #0x30c
0x026D5584: str      x9, [sp, #0x78]
0x026D5588: add      x9, x8, #0x24
0x026D558C: stp      x9, x10, [sp, #0x48]
0x026D5590: add      x9, x8, #0x2c8
0x026D5594: add      x8, x2, #0x980
0x026D5598: stp      x9, x8, [sp, #0x58]
0x026D559C: adrp     x8, #0x1212000
0x026D55A0: adrp     x9, #0x1212000
0x026D55A4: ldr      d8, [x8, #0x18]
0x026D55A8: ldr      d9, [x9, #0x568]
0x026D55AC: b        #0x26d55fc
0x026D55B0: adrp     x8, #0x5098000
0x026D55B4: ldr      x8, [x8, #0x9f8]
0x026D55B8: blr      x8
0x026D55BC: ldr      x8, [sp, #0x50]
0x026D55C0: adrp     x1, #0x11e6000
0x026D55C4: adrp     x2, #0x11ac000
0x026D55C8: ldr      w3, [x23]
0x026D55CC: ldrb     w4, [x20]
0x026D55D0: add      x1, x1, #0x222
0x026D55D4: ldr      w5, [x8]
0x026D55D8: add      x2, x2, #0x6d
0x026D55DC: ldr      x8, [sp, #0x58]
0x026D55E0: mov      w7, w27
0x026D55E4: ldrb     w6, [x8]
0x026D55E8: bl       #0x2185848
0x026D55EC: ldr      x8, [x19, #0x90]
0x026D55F0: add      x29, x29, #0x348
0x026D55F4: cmp      x29, x8
0x026D55F8: b.eq     #0x26d6354
0x026D55FC: ldr      w20, [x25]
0x026D5600: ldr      w8, [x29, #0x14]
0x026D5604: cmp      w8, w20
0x026D5608: b.eq     #0x26d55ec
0x026D560C: adrp     x8, #0x5098000
0x026D5610: add      x28, x29, #0x1c
0x026D5614: ldp      x0, x1, [sp, #0x90]
0x026D5618: mov      x2, x28
0x026D561C: ldr      x8, [x8, #0x938]
0x026D5620: blr      x8
0x026D5624: tbz      w0, #0, #0x26d55ec
0x026D5628: cmp      w20, #1
0x026D562C: b.lt     #0x26d563c
0x026D5630: ldr      x8, [x29, #0x238]
0x026D5634: cmp      x8, x20
0x026D5638: b.hs     #0x26d5644
0x026D563C: mov      w26, wzr
0x026D5640: b        #0x26d5660
0x026D5644: sub      w8, w20, #1
0x026D5648: ldr      x10, [x29, #0x230]
0x026D564C: lsr      x9, x8, #3
0x026D5650: and      x9, x9, #0x1ffffff8
0x026D5654: ldr      x9, [x10, x9]
0x026D5658: lsr      x8, x9, x8
0x026D565C: and      w26, w8, #1
0x026D5660: adrp     x27, #0x5266000
0x026D5664: ldr      x21, [x24, #0x9d0]
0x026D5668: cbz      x21, #0x26d5754
0x026D566C: mov      x9, x21
0x026D5670: ldr      x22, [x9, #8]!
0x026D5674: cbz      x22, #0x26d5754
0x026D5678: ldr      w8, [x29, #4]
0x026D567C: mov      x10, x9
0x026D5680: mov      x11, x22
0x026D5684: ldr      w12, [x11, #0x1c]
0x026D5688: cmp      w12, w8
0x026D568C: cset     w12, lt
0x026D5690: csel     x10, x10, x11, lt
0x026D5694: ldr      x11, [x11, w12, uxtw #3]
0x026D5698: cbnz     x11, #0x26d5684
0x026D569C: cmp      x10, x9
0x026D56A0: b.eq     #0x26d5754
0x026D56A4: ldr      w9, [x10, #0x1c]
0x026D56A8: cmp      w8, w9
0x026D56AC: b.lt     #0x26d5754
0x026D56B0: add      x23, x21, #8
0x026D56B4: b        #0x26d56c8
0x026D56B8: ldr      x9, [x22]
0x026D56BC: mov      x23, x22
0x026D56C0: cbz      x9, #0x26d56e8
0x026D56C4: mov      x22, x9
0x026D56C8: ldr      w9, [x22, #0x1c]
0x026D56CC: cmp      w8, w9
0x026D56D0: b.lt     #0x26d56b8
0x026D56D4: cmp      w9, w8
0x026D56D8: b.ge     #0x26d56e8
0x026D56DC: mov      x23, x22
0x026D56E0: ldr      x9, [x23, #8]!
0x026D56E4: cbnz     x9, #0x26d56c4
0x026D56E8: ldr      x20, [x23]
0x026D56EC: cbnz     x20, #0x26d5740
0x026D56F0: mov      w0, #0x28
0x026D56F4: bl       #0x4b40050
0x026D56F8: ldr      w8, [x29, #4]
0x026D56FC: stp      xzr, xzr, [x0]
0x026D5700: str      x22, [x0, #0x10]
0x026D5704: mov      x20, x0
0x026D5708: stp      w8, wzr, [x0, #0x1c]
0x026D570C: str      x0, [x23]
0x026D5710: ldr      x8, [x21]
0x026D5714: ldr      x8, [x8]
0x026D5718: cbz      x8, #0x26d5728
0x026D571C: str      x8, [x21]
0x026D5720: ldr      x1, [x23]
0x026D5724: b        #0x26d572c
0x026D5728: mov      x1, x20
0x026D572C: ldr      x0, [x21, #8]
0x026D5730: bl       #0x2260c4c
0x026D5734: ldr      x8, [x21, #0x10]
0x026D5738: add      x8, x8, #1
0x026D573C: str      x8, [x21, #0x10]
0x026D5740: ldr      w8, [x20, #0x20]
0x026D5744: ldr      w9, [x19]
0x026D5748: add      w8, w8, #6
0x026D574C: cmp      w8, w9
0x026D5750: b.ge     #0x26d59a8
0x026D5754: ldp      x24, x21, [sp, #0x70]
0x026D5758: mov      w22, #1
0x026D575C: ldr      x20, [sp, #0x80]
0x026D5760: ldr      x8, [x27, #0xb38]
0x026D5764: mov      x0, x24
0x026D5768: mov      x1, x21
0x026D576C: blr      x8
0x026D5770: cmp      x20, x0
0x026D5774: b.eq     #0x26d578c
0x026D5778: adrp     x8, #0x5266000
0x026D577C: mov      x0, x24
0x026D5780: mov      x1, x21
0x026D5784: ldr      x8, [x8, #0xb88]
0x026D5788: b        #0x26d57bc
0x026D578C: ldr      x8, [x27, #0xb38]
0x026D5790: add      x1, sp, #0xac
0x026D5794: mov      x0, x24
0x026D5798: str      wzr, [sp, #0xac]
0x026D579C: blr      x8
0x026D57A0: cmp      x20, x0
0x026D57A4: b.eq     #0x26d59a0
0x026D57A8: adrp     x8, #0x5266000
0x026D57AC: add      x1, sp, #0xa8
0x026D57B0: mov      x0, x24
0x026D57B4: str      wzr, [sp, #0xa8]
0x026D57B8: ldr      x8, [x8, #0xb98]
0x026D57BC: blr      x8
0x026D57C0: ldr      w27, [x0]
0x026D57C4: mov      x23, x29
0x026D57C8: ldr      w8, [x23, #4]!
0x026D57CC: cmp      w8, #0x74
0x026D57D0: b.eq     #0x26d57dc
0x026D57D4: cmp      w8, #0x99
0x026D57D8: b.ne     #0x26d58cc
0x026D57DC: ldr      x24, [sp, #0x88]
0x026D57E0: and      w8, w26, w22
0x026D57E4: cmp      w8, #1
0x026D57E8: b.ne     #0x26d5b44
0x026D57EC: ldr      w8, [x23]
0x026D57F0: cmp      w8, #0x99
0x026D57F4: b.eq     #0x26d5800
0x026D57F8: cmp      w8, #0x74
0x026D57FC: b.ne     #0x26d55ec
0x026D5800: ldr      x21, [x24, #0x9d8]
0x026D5804: cbz      x21, #0x26d55ec
0x026D5808: mov      x9, x21
0x026D580C: ldr      x26, [x9, #8]!
0x026D5810: cbz      x26, #0x26d55ec
0x026D5814: ldr      w8, [x29, #8]
0x026D5818: mov      x10, x9
0x026D581C: mov      x11, x26
0x026D5820: ldr      w12, [x11, #0x1c]
0x026D5824: cmp      w12, w8
0x026D5828: cset     w12, lt
0x026D582C: csel     x10, x10, x11, lt
0x026D5830: ldr      x11, [x11, w12, uxtw #3]
0x026D5834: cbnz     x11, #0x26d5820
0x026D5838: cmp      x10, x9
0x026D583C: b.eq     #0x26d55ec
0x026D5840: ldr      w9, [x10, #0x1c]
0x026D5844: cmp      w8, w9
0x026D5848: b.lt     #0x26d55ec
0x026D584C: ldr      w10, [x19]
0x026D5850: add      x24, x21, #8
0x026D5854: b        #0x26d5868
0x026D5858: ldr      x9, [x26]
0x026D585C: mov      x24, x26
0x026D5860: cbz      x9, #0x26d5888
0x026D5864: mov      x26, x9
0x026D5868: ldr      w9, [x26, #0x1c]
0x026D586C: cmp      w8, w9
0x026D5870: b.lt     #0x26d5858
0x026D5874: cmp      w9, w8
0x026D5878: b.ge     #0x26d5888
0x026D587C: mov      x24, x26
0x026D5880: ldr      x9, [x24, #8]!
0x026D5884: cbnz     x9, #0x26d5864
0x026D5888: ldr      x20, [x24]
0x026D588C: cbnz     x20, #0x26d5b08
0x026D5890: mov      w0, #0x28
0x026D5894: str      w10, [sp, #0x38]
0x026D5898: bl       #0x4b40050
0x026D589C: ldr      w8, [x29, #8]
0x026D58A0: stp      xzr, xzr, [x0]
0x026D58A4: str      x26, [x0, #0x10]
0x026D58A8: mov      x20, x0
0x026D58AC: stp      w8, wzr, [x0, #0x1c]
0x026D58B0: str      x0, [x24]
0x026D58B4: ldr      x8, [x21]
0x026D58B8: ldr      x8, [x8]
~~~

### Function start 0x26d63cc
Hits: [{"pc": "0x26d65a4", "adrp": "0x26d6594", "target": "0x11c5f0b", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPositionByTimeDynamic", "keywords": ["ModifyEnemyInvisibleHeroPositionByTimeDynamic", "ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d63cc", "fde_end": "0x26d6b48", "kind": "add", "reg": "x1"}, {"pc": "0x26d6a00", "adrp": "0x26d69f0", "target": "0x11c5f0b", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPositionByTimeDynamic", "keywords": ["ModifyEnemyInvisibleHeroPositionByTimeDynamic", "ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d63cc", "fde_end": "0x26d6b48", "kind": "add", "reg": "x1"}, {"pc": "0x26d6a08", "adrp": "0x26d69f8", "target": "0x11d87a2", "label": "frame:%d main_hero:%d hero:%d, not visible duration(sec) = %d, dist = %d, last_dist = %d, enemy true location = (%d, %d), main_hero_location = (%d, %d), invisible_range:%d", "keywords": ["invisible"], "fde_start": "0x26d63cc", "fde_end": "0x26d6b48", "kind": "add", "reg": "x2"}, {"pc": "0x26d6ab0", "adrp": "0x26d6aa0", "target": "0x11c5f0b", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPositionByTimeDynamic", "keywords": ["ModifyEnemyInvisibleHeroPositionByTimeDynamic", "ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d63cc", "fde_end": "0x26d6b48", "kind": "add", "reg": "x1"}, {"pc": "0x26d6ab8", "adrp": "0x26d6aa4", "target": "0x1185459", "label": "frame:%d camp:%d, main_hero:%d, modify emy_hero:%d to spring, frame_diff:%d, last_visible_dist:%d, dist:%d, invisible_range:%d", "keywords": ["invisible"], "fde_start": "0x26d63cc", "fde_end": "0x26d6b48", "kind": "add", "reg": "x2"}, {"pc": "0x26d6b14", "adrp": "0x26d6b08", "target": "0x11c5f0b", "label": "game_aivoice::AiProcess::ModifyEnemyInvisibleHeroPositionByTimeDynamic", "keywords": ["ModifyEnemyInvisibleHeroPositionByTimeDynamic", "ModifyEnemyInvisibleHeroPosition", "HeroPosition"], "fde_start": "0x26d63cc", "fde_end": "0x26d6b48", "kind": "add", "reg": "x1"}]
~~~asm
0x026D63CC: sub      sp, sp, #0xf0
0x026D63D0: stp      d9, d8, [sp, #0x80]
0x026D63D4: stp      x29, x30, [sp, #0x90]
0x026D63D8: stp      x28, x27, [sp, #0xa0]
0x026D63DC: stp      x26, x25, [sp, #0xb0]
0x026D63E0: stp      x24, x23, [sp, #0xc0]
0x026D63E4: stp      x22, x21, [sp, #0xd0]
0x026D63E8: stp      x20, x19, [sp, #0xe0]
0x026D63EC: adrp     x8, #0x5098000
0x026D63F0: str      w4, [sp, #0x6c]
0x026D63F4: mov      w23, w3
0x026D63F8: mov      x19, x1
0x026D63FC: mov      x22, x0
0x026D6400: str      x2, [sp, #0x78]
0x026D6404: ldr      x8, [x8, #0x7b8]
0x026D6408: blr      x8
0x026D640C: ldr      w8, [x19]
0x026D6410: cmp      w8, #0x1c2
0x026D6414: mov      w8, #0xf
0x026D6418: csel     w8, w8, w23, lt
0x026D641C: cmp      w8, #0xe0f
0x026D6420: str      w8, [sp, #0x5c]
0x026D6424: b.gt     #0x26d6b20
0x026D6428: ldp      x23, x8, [x19, #0x88]
0x026D642C: cmp      x23, x8
0x026D6430: b.eq     #0x26d6b20
0x026D6434: ldrsw    x8, [x19, #0x18]
0x026D6438: mov      w9, #0x348
0x026D643C: mov      w10, #0x2210
0x026D6440: mov      w11, #0x2b00
0x026D6444: add      x20, x22, x11
0x026D6448: madd     x8, x8, x9, x23
0x026D644C: add      x9, x22, x10
0x026D6450: add      x26, x8, #0x14
0x026D6454: add      x25, x8, #0x1c
0x026D6458: str      x9, [sp, #0x70]
0x026D645C: add      x9, x8, #0x2c8
0x026D6460: str      x9, [sp, #0x60]
0x026D6464: add      x9, x8, #4
0x026D6468: str      x9, [sp, #0x50]
0x026D646C: add      x9, x8, #0x24
0x026D6470: ldr      x8, [sp, #0x78]
0x026D6474: add      x8, x8, #0x980
0x026D6478: stp      x8, x9, [sp, #0x38]
0x026D647C: b        #0x26d64ac
0x026D6480: sub      w8, w21, #1
0x026D6484: ldr      x10, [x23, #0x230]
0x026D6488: lsr      x9, x8, #3
0x026D648C: and      x9, x9, #0x1ffffff8
0x026D6490: ldr      x9, [x10, x9]
0x026D6494: lsr      x8, x9, x8
0x026D6498: tbz      w8, #0, #0x26d64d0
0x026D649C: ldr      x8, [x19, #0x90]
0x026D64A0: add      x23, x23, #0x348
0x026D64A4: cmp      x23, x8
0x026D64A8: b.eq     #0x26d6b20
0x026D64AC: ldr      w21, [x26]
0x026D64B0: ldr      w8, [x23, #0x14]
0x026D64B4: cmp      w8, w21
0x026D64B8: b.eq     #0x26d649c
0x026D64BC: cmp      w21, #1
0x026D64C0: b.lt     #0x26d64d0
0x026D64C4: ldr      x8, [x23, #0x238]
0x026D64C8: cmp      x8, x21
0x026D64CC: b.hs     #0x26d6480
0x026D64D0: ldr      w8, [x23, #4]
0x026D64D4: cmp      w8, #0x99
0x026D64D8: b.eq     #0x26d64e4
0x026D64DC: cmp      w8, #0x74
0x026D64E0: b.ne     #0x26d6538
0x026D64E4: adrp     x8, #0x5098000
0x026D64E8: add      x2, x23, #0x1c
0x026D64EC: mov      x0, x22
0x026D64F0: mov      x1, x25
0x026D64F4: ldr      x8, [x8, #0x938]
0x026D64F8: blr      x8
0x026D64FC: tbz      w0, #0, #0x26d6538
0x026D6500: cmp      w21, #1
0x026D6504: b.lt     #0x26d6538
0x026D6508: ldr      x8, [x23, #0x238]
0x026D650C: cmp      x8, x21
0x026D6510: b.lo     #0x26d6538
0x026D6514: sub      w8, w21, #1
0x026D6518: ldr      x10, [x23, #0x230]
0x026D651C: lsr      x9, x8, #3
0x026D6520: and      x9, x9, #0x1ffffff8
0x026D6524: ldr      x9, [x10, x9]
0x026D6528: lsr      x8, x9, x8
0x026D652C: tbnz     w8, #0, #0x26d6538
0x026D6530: ldrb     w8, [x23, #0x2c8]
0x026D6534: cbz      w8, #0x26d649c
0x026D6538: adrp     x8, #0x517e000
0x026D653C: add      x29, x23, #0x1c
0x026D6540: ldr      x0, [sp, #0x70]
0x026D6544: mov      x1, x29
0x026D6548: mov      x2, x25
0x026D654C: mov      w3, #1
0x026D6550: ldr      x8, [x8, #0x4f8]
0x026D6554: blr      x8
0x026D6558: ldr      w8, [x23, #4]
0x026D655C: cmp      w8, #0xc4
0x026D6560: b.ne     #0x26d65c4
0x026D6564: ldrb     w8, [x23, #0x2c8]
0x026D6568: cbz      w8, #0x26d65c4
0x026D656C: mov      w27, w0
0x026D6570: cmp      w0, #0x1d
0x026D6574: b.gt     #0x26d65c4
0x026D6578: ldr      x8, [sp, #0x60]
0x026D657C: ldrb     w8, [x8]
0x026D6580: cbz      w8, #0x26d65c4
0x026D6584: adrp     x8, #0x5098000
0x026D6588: ldr      x8, [x8, #0x9f8]
0x026D658C: blr      x8
0x026D6590: ldr      x8, [sp, #0x50]
0x026D6594: adrp     x1, #0x11c5000
0x026D6598: adrp     x2, #0x11a5000
0x026D659C: ldr      w3, [x23, #4]
0x026D65A0: ldrb     w4, [x23, #0x2c8]
0x026D65A4: add      x1, x1, #0xf0b
0x026D65A8: ldr      w5, [x8]
0x026D65AC: add      x2, x2, #0x888
0x026D65B0: ldr      x8, [sp, #0x60]
0x026D65B4: mov      w7, w27
0x026D65B8: ldrb     w6, [x8]
0x026D65BC: bl       #0x2185848
0x026D65C0: b        #0x26d649c
0x026D65C4: ldr      x24, [x20]
0x026D65C8: cbz      x24, #0x26d6818
0x026D65CC: ldr      w8, [x23, #8]
0x026D65D0: mov      x9, x20
0x026D65D4: mov      x10, x24
0x026D65D8: ldr      w11, [x10, #0x1c]
0x026D65DC: cmp      w11, w8
0x026D65E0: cset     w11, lt
0x026D65E4: csel     x9, x9, x10, lt
0x026D65E8: ldr      x10, [x10, w11, uxtw #3]
0x026D65EC: cbnz     x10, #0x26d65d8
0x026D65F0: cmp      x9, x20
0x026D65F4: b.eq     #0x26d6818
0x026D65F8: ldr      w9, [x9, #0x1c]
0x026D65FC: cmp      w8, w9
0x026D6600: b.lt     #0x26d6818
0x026D6604: mov      x21, x20
0x026D6608: b        #0x26d661c
0x026D660C: ldr      x9, [x24]
0x026D6610: mov      x21, x24
0x026D6614: cbz      x9, #0x26d663c
0x026D6618: mov      x24, x9
0x026D661C: ldr      w9, [x24, #0x1c]
0x026D6620: cmp      w8, w9
0x026D6624: b.lt     #0x26d660c
0x026D6628: cmp      w9, w8
0x026D662C: b.ge     #0x26d663c
0x026D6630: mov      x21, x24
0x026D6634: ldr      x9, [x21, #8]!
0x026D6638: cbnz     x9, #0x26d6618
0x026D663C: ldr      x27, [x21]
0x026D6640: cbnz     x27, #0x26d6694
0x026D6644: mov      w0, #0x28
0x026D6648: bl       #0x4b40050
0x026D664C: ldr      w8, [x23, #8]
0x026D6650: stp      xzr, xzr, [x0]
0x026D6654: str      x24, [x0, #0x10]
0x026D6658: mov      x27, x0
0x026D665C: stp      w8, wzr, [x0, #0x1c]
0x026D6660: str      x0, [x21]
0x026D6664: ldr      x8, [x22, #0x2af8]
0x026D6668: ldr      x8, [x8]
0x026D666C: cbz      x8, #0x26d667c
0x026D6670: str      x8, [x22, #0x2af8]
0x026D6674: ldr      x1, [x21]
0x026D6678: b        #0x26d6680
0x026D667C: mov      x1, x27
0x026D6680: ldr      x0, [x22, #0x2b00]
0x026D6684: bl       #0x2260c4c
0x026D6688: ldr      x8, [x22, #0x2b08]
0x026D668C: add      x8, x8, #1
0x026D6690: str      x8, [x22, #0x2b08]
0x026D6694: ldr      w8, [x27, #0x20]
0x026D6698: cmp      w8, #1
0x026D669C: b.lt     #0x26d6818
0x026D66A0: ldr      x21, [x20]
0x026D66A4: cbz      x21, #0x26d66ec
0x026D66A8: ldr      w8, [x23, #8]
0x026D66AC: mov      x24, x20
0x026D66B0: ldr      w9, [x21, #0x1c]
0x026D66B4: cmp      w8, w9
0x026D66B8: b.ge     #0x26d66d0
0x026D66BC: ldr      x9, [x21]
0x026D66C0: cbz      x9, #0x26d6734
0x026D66C4: mov      x24, x21
0x026D66C8: mov      x21, x9
0x026D66CC: b        #0x26d66b0
0x026D66D0: cmp      w9, w8
0x026D66D4: b.ge     #0x26d66f4
0x026D66D8: mov      x24, x21
0x026D66DC: ldr      x9, [x24, #8]!
0x026D66E0: cbz      x9, #0x26d66f4
0x026D66E4: mov      x21, x9
0x026D66E8: b        #0x26d66b0
0x026D66EC: mov      x21, x20
0x026D66F0: mov      x24, x20
0x026D66F4: ldr      x27, [x24]
0x026D66F8: cbnz     x27, #0x26d675c
0x026D66FC: mov      w0, #0x28
0x026D6700: bl       #0x4b40050
0x026D6704: ldr      w8, [x23, #8]
0x026D6708: stp      xzr, xzr, [x0]
0x026D670C: str      x21, [x0, #0x10]
0x026D6710: mov      x27, x0
0x026D6714: stp      w8, wzr, [x0, #0x1c]
0x026D6718: str      x0, [x24]
0x026D671C: ldr      x8, [x22, #0x2af8]
0x026D6720: ldr      x8, [x8]
0x026D6724: cbz      x8, #0x26d6744
0x026D6728: str      x8, [x22, #0x2af8]
0x026D672C: ldr      x1, [x24]
0x026D6730: b        #0x26d6748
0x026D6734: mov      x24, x21
0x026D6738: ldr      x27, [x24]
0x026D673C: cbnz     x27, #0x26d675c
0x026D6740: b        #0x26d66fc
0x026D6744: mov      x1, x27
0x026D6748: ldr      x0, [x22, #0x2b00]
0x026D674C: bl       #0x2260c4c
0x026D6750: ldr      x8, [x22, #0x2b08]
0x026D6754: add      x8, x8, #1
0x026D6758: str      x8, [x22, #0x2b08]
0x026D675C: ldr      w8, [x27, #0x20]
0x026D6760: ldr      w9, [x22, #0x2ad4]
0x026D6764: cmp      w8, w9
0x026D6768: b.ge     #0x26d6818
0x026D676C: mov      x0, xzr
0x026D6770: bl       #0x4b40500
0x026D6774: bl       #0x4b40380
0x026D6778: bl       #0x4b40370
0x026D677C: mov      w21, #0x851f
0x026D6780: mov      w24, #0xc8
0x026D6784: movk     w21, #0x51eb, lsl #16
0x026D6788: smull    x8, w0, w21
~~~

### Function start 0x276df9c
Hits: [{"pc": "0x2770044", "adrp": "0x277003c", "target": "0x1145b4b", "label": "_invisible_visible_rule_case1", "keywords": ["invisible"], "fde_start": "0x276df9c", "fde_end": "0x27702e0", "kind": "add", "reg": "x1"}, {"pc": "0x277010c", "adrp": "0x2770104", "target": "0x1152f26", "label": "_invisible_visible_rule_case2", "keywords": ["invisible"], "fde_start": "0x276df9c", "fde_end": "0x27702e0", "kind": "add", "reg": "x1"}]
~~~asm
0x0276DF9C: sub      sp, sp, #0xd0
0x0276DFA0: stp      d9, d8, [sp, #0x60]
0x0276DFA4: stp      x29, x30, [sp, #0x70]
0x0276DFA8: stp      x28, x27, [sp, #0x80]
0x0276DFAC: stp      x26, x25, [sp, #0x90]
0x0276DFB0: stp      x24, x23, [sp, #0xa0]
0x0276DFB4: stp      x22, x21, [sp, #0xb0]
0x0276DFB8: stp      x20, x19, [sp, #0xc0]
0x0276DFBC: mov      w8, #6
0x0276DFC0: ldr      w9, [x2, #0x15c8]
0x0276DFC4: adrp     x10, #0x113d000
0x0276DFC8: mov      x22, x1
0x0276DFCC: add      x21, x0, #0x3a0
0x0276DFD0: mov      x28, x2
0x0276DFD4: fmov     s0, w8
0x0276DFD8: fmov     s1, w9
0x0276DFDC: adrp     x8, #0x113c000
0x0276DFE0: ldr      q2, [x10, #0x530]
0x0276DFE4: cmp      w9, #6
0x0276DFE8: mov      w9, #0xe
0x0276DFEC: cmeq     v0.4s, v1.4s, v0.4s
0x0276DFF0: mov      x19, x0
0x0276DFF4: ldr      q1, [x8, #0xdc0]
0x0276DFF8: mov      w8, #9
0x0276DFFC: csel     w8, w9, w8, eq
0x0276E000: add      x9, x0, #0x7b4
0x0276E004: dup      v0.4s, v0.s[0]
0x0276E008: str      w8, [x0, #0x7c4]
0x0276E00C: bsl      v0.16b, v2.16b, v1.16b
0x0276E010: str      q0, [x9]
0x0276E014: mov      w9, #0x15f0
0x0276E018: ldr      w8, [x1]
0x0276E01C: add      x20, x2, x9
0x0276E020: adrp     x1, #0x11fa000
0x0276E024: add      x1, x1, #0x13
0x0276E028: str      w8, [x0, #0x390]
0x0276E02C: str      wzr, [x2, #0x15ec]
0x0276E030: mov      w2, #0xb
0x0276E034: strb     wzr, [x20]
0x0276E038: strb     wzr, [x0, #0x43c]
0x0276E03C: mov      x0, x21
0x0276E040: bl       #0x2282f58
0x0276E044: ldr      w8, [x22, #0x2a4]
0x0276E048: cmp      w8, #0x64
0x0276E04C: b.ne     #0x276e080
0x0276E050: ldr      w8, [x19, #0x390]
0x0276E054: cmp      w8, #0x95
0x0276E058: b.gt     #0x276e080
0x0276E05C: adrp     x1, #0x1186000
0x0276E060: mov      w8, #0x10
0x0276E064: add      x1, x1, #0x707
0x0276E068: mov      x0, x21
0x0276E06C: mov      w2, #0x19
0x0276E070: str      w8, [x28, #0x150]
0x0276E074: bl       #0x2282f58
0x0276E078: mov      w0, #1
0x0276E07C: b        #0x2770280
0x0276E080: ldr      w8, [x19, #8]
0x0276E084: tbz      w8, #0x1f, #0x276e090
0x0276E088: ldr      w8, [x28, #0xd7c]
0x0276E08C: str      w8, [x19, #8]
0x0276E090: adrp     x8, #0x509b000
0x0276E094: mov      x0, x19
0x0276E098: mov      x1, x22
0x0276E09C: mov      x2, x28
0x0276E0A0: ldr      x8, [x8, #0x7e0]
0x0276E0A4: blr      x8
0x0276E0A8: tbz      w0, #0, #0x276e108
0x0276E0AC: adrp     x8, #0x509c000
0x0276E0B0: ldr      x8, [x8, #0x70]
0x0276E0B4: blr      x8
0x0276E0B8: adrp     x1, #0x11d2000
0x0276E0BC: adrp     x2, #0x11a6000
0x0276E0C0: add      x1, x1, #0xc77
0x0276E0C4: add      x2, x2, #0xd2a
0x0276E0C8: bl       #0x2185854
0x0276E0CC: ldr      x8, [x19]
0x0276E0D0: mov      x0, x19
0x0276E0D4: ldr      x8, [x8, #0x20]
0x0276E0D8: blr      x8
0x0276E0DC: adrp     x8, #0x542b000
0x0276E0E0: mov      w0, #1
0x0276E0E4: add      x8, x8, #0x410
0x0276E0E8: strb     w0, [x28, #0x690]
0x0276E0EC: ldr      x9, [x8]
0x0276E0F0: ldr      w8, [x8, #8]
0x0276E0F4: str      x9, [x28, #0x170]
0x0276E0F8: str      w8, [x28, #0x178]
0x0276E0FC: stp      xzr, x9, [x28, #0x150]
0x0276E100: str      w8, [x28, #0x160]
0x0276E104: b        #0x2770280
0x0276E108: ldr      x9, [x19, #0x308]
0x0276E10C: str      x20, [sp, #0x40]
0x0276E110: ldr      x8, [x19, #0x300]
0x0276E114: ldrsw    x20, [x28, #0x1c]
0x0276E118: sub      x9, x9, x8
0x0276E11C: lsr      x9, x9, #2
0x0276E120: cmp      w20, w9
0x0276E124: b.ge     #0x276e17c
0x0276E128: ldr      w9, [x19, #0x340]
0x0276E12C: tbnz     w9, #0x1f, #0x276e1b8
0x0276E130: adrp     x8, #0x526d000
0x0276E134: ldr      w9, [x19, #0x368]
0x0276E138: add      x1, x19, #0x2cc
0x0276E13C: add      x0, x19, #0x1e0
0x0276E140: ldr      x8, [x8, #0x1b0]
0x0276E144: str      w9, [x19, #0x2cc]
0x0276E148: blr      x8
0x0276E14C: ldr      x8, [x28, #0xa78]
0x0276E150: mov      w10, #0x18
0x0276E154: ldrsw    x9, [x0]
0x0276E158: nop      
0x0276E15C: madd     x0, x9, x10, x8
0x0276E160: add      x8, x19, #0x350
0x0276E164: cmp      x0, x8
0x0276E168: b.eq     #0x276e1e8
0x0276E16C: ldr      x1, [x19, #0x350]
0x0276E170: ldr      x2, [x19, #0x358]
0x0276E174: bl       #0x2253ad8
0x0276E178: b        #0x276e1e8
0x0276E17C: adrp     x8, #0x509c000
0x0276E180: ldr      x8, [x8, #0x70]
0x0276E184: blr      x8
0x0276E188: ldr      x8, [x19, #0x308]
0x0276E18C: adrp     x1, #0x11d2000
0x0276E190: ldr      x9, [x19, #0x300]
0x0276E194: adrp     x2, #0x1160000
0x0276E198: add      x1, x1, #0xc77
0x0276E19C: add      x2, x2, #0x1f0
0x0276E1A0: mov      w3, w20
0x0276E1A4: sub      x8, x8, x9
0x0276E1A8: asr      x4, x8, #2
0x0276E1AC: bl       #0x2185854
0x0276E1B0: mov      w0, wzr
0x0276E1B4: b        #0x2770280
0x0276E1B8: adrp     x9, #0x509c000
0x0276E1BC: ldr      w8, [x8, x20, lsl #2]
0x0276E1C0: ldr      x9, [x9, #0x70]
0x0276E1C4: str      w8, [x19, #0x2cc]
0x0276E1C8: blr      x9
0x0276E1CC: adrp     x1, #0x11d2000
0x0276E1D0: adrp     x2, #0x1152000
0x0276E1D4: ldr      w4, [x19, #0x2cc]
0x0276E1D8: add      x1, x1, #0xc77
0x0276E1DC: add      x2, x2, #0xedd
0x0276E1E0: mov      w3, w20
0x0276E1E4: bl       #0x2185854
0x0276E1E8: mov      w8, #1
0x0276E1EC: strb     wzr, [x28, #0x690]
0x0276E1F0: str      wzr, [x28, #0x150]
0x0276E1F4: strb     w8, [x19, #0x140]
0x0276E1F8: ldr      w8, [x28, #0x3f0]
0x0276E1FC: cmp      w8, #0xf
0x0276E200: b.eq     #0x276e230
0x0276E204: cmp      w8, #0x1b
0x0276E208: b.eq     #0x276e230
0x0276E20C: adrp     x8, #0x509c000
0x0276E210: ldr      x8, [x8, #0x70]
0x0276E214: blr      x8
0x0276E218: adrp     x1, #0x11d2000
0x0276E21C: adrp     x2, #0x11b9000
0x0276E220: add      x1, x1, #0xc77
0x0276E224: add      x2, x2, #0x7de
0x0276E228: bl       #0x2185854
0x0276E22C: str      wzr, [x19, #0x2a8]
0x0276E230: str      xzr, [x19, #0x1c0]
0x0276E234: mov      w10, #0x3f0
0x0276E238: ldrsw    x8, [x22, #0x10]
0x0276E23C: ldr      x9, [x22, #0x68]
0x0276E240: nop      
0x0276E244: madd     x8, x8, x10, x9
0x0276E248: str      x8, [x19, #0x1c0]
0x0276E24C: ldr      w8, [x8, #4]
0x0276E250: cmp      w8, #0x279
0x0276E254: b.ne     #0x276e294
0x0276E258: ldr      w8, [x19, #0x2cc]
0x0276E25C: cmp      w8, #1
0x0276E260: b.ne     #0x276e294
0x0276E264: adrp     x8, #0x517f000
0x0276E268: add      x0, x19, #0x58
0x0276E26C: mov      x1, x22
0x0276E270: mov      w2, #1
0x0276E274: mov      w3, wzr
0x0276E278: mov      w4, #0x5a
0x0276E27C: ldr      x8, [x8, #0x2d8]
0x0276E280: mov      w5, #1
0x0276E284: blr      x8
0x0276E288: cbz      w0, #0x276e294
0x0276E28C: mov      w8, #2
0x0276E290: str      w8, [x19, #0x2cc]
0x0276E294: ldr      w8, [x28, #0x3f0]
0x0276E298: cmp      w8, #0x15
0x0276E29C: b.hi     #0x276e2c4
0x0276E2A0: mov      w9, #1
0x0276E2A4: lsl      w8, w9, w8
0x0276E2A8: mov      w9, #0xe0
0x0276E2AC: movk     w9, #0x20, lsl #16
0x0276E2B0: tst      w8, w9
0x0276E2B4: b.eq     #0x276e2c4
0x0276E2B8: ldr      w8, [x22]
0x0276E2BC: sub      w8, w8, #1
0x0276E2C0: str      w8, [x19, #0x834]
0x0276E2C4: ldr      x8, [x19, #0x1c0]
0x0276E2C8: ldp      x9, x10, [x8, #0x130]
0x0276E2CC: cmp      x10, x9
0x0276E2D0: b.eq     #0x276e390
0x0276E2D4: mov      x14, #0x6db7
0x0276E2D8: mov      w13, #0xe14a
0x0276E2DC: movk     x14, #0xb6db, lsl #16
0x0276E2E0: mov      w15, #0x10e7
0x0276E2E4: movk     x14, #0xdb6d, lsl #32
0x0276E2E8: mov      w16, #0xe29e
0x0276E2EC: mov      w17, #0x1c4c
0x0276E2F0: mov      x11, xzr
0x0276E2F4: mov      w12, #0x38
0x0276E2F8: movk     w13, #1, lsl #16
0x0276E2FC: movk     x14, #0x6db6, lsl #48
0x0276E300: movk     w15, #2, lsl #16
0x0276E304: movk     w16, #1, lsl #16
0x0276E308: movk     w17, #0xfffc, lsl #16
0x0276E30C: b        #0x276e334
0x0276E310: ldr      w9, [x22]
0x0276E314: str      w9, [x19, #0x834]
0x0276E318: ldp      x9, x10, [x8, #0x130]
0x0276E31C: sub      x0, x10, x9
0x0276E320: add      w11, w11, #1
0x0276E324: asr      x0, x0, #3
0x0276E328: mul      x0, x0, x14
0x0276E32C: cmp      x0, x11
0x0276E330: b.ls     #0x276e394
0x0276E334: mul      x0, x11, x12
0x0276E338: ldr      w0, [x9, x0]
0x0276E33C: cmp      w0, w13
0x0276E340: b.eq     #0x276e354
0x0276E344: cmp      w0, w15
0x0276E348: b.eq     #0x276e364
0x0276E34C: cmp      w0, w16
0x0276E350: b.ne     #0x276e374
0x0276E354: ldr      w0, [x8, #4]
0x0276E358: cmp      w0, #0x7b
~~~

### Function start 0x27a9820
Hits: [{"pc": "0x27a98d0", "adrp": "0x27a98c0", "target": "0x11a6f31", "label": "last_enemy_visible_frame %d last_enemy_invisible_frame %d", "keywords": ["invisible"], "fde_start": "0x27a9820", "fde_end": "0x27a9d7c", "kind": "add", "reg": "x2"}]
~~~asm
0x027A9820: sub      sp, sp, #0x80
0x027A9824: stp      x29, x30, [sp, #0x20]
0x027A9828: stp      x28, x27, [sp, #0x30]
0x027A982C: stp      x26, x25, [sp, #0x40]
0x027A9830: stp      x24, x23, [sp, #0x50]
0x027A9834: stp      x22, x21, [sp, #0x60]
0x027A9838: stp      x20, x19, [sp, #0x70]
0x027A983C: adrp     x8, #0x509c000
0x027A9840: mov      x20, x2
0x027A9844: mov      x19, x1
0x027A9848: ldr      x8, [x8, #0x70]
0x027A984C: blr      x8
0x027A9850: adrp     x1, #0x11b3000
0x027A9854: adrp     x2, #0x1207000
0x027A9858: add      x1, x1, #0x8eb
0x027A985C: add      x2, x2, #0xc50
0x027A9860: bl       #0x2185854
0x027A9864: ldr      x8, [x20, #0x258]
0x027A9868: add      x9, x20, #0x248
0x027A986C: ldr      x22, [x19, #0x70]
0x027A9870: str      x9, [sp, #0x18]
0x027A9874: cbz      x8, #0x27a9bc4
0x027A9878: ldr      x24, [x19, #0x68]
0x027A987C: cmp      x22, x24
0x027A9880: b.eq     #0x27a9ba0
0x027A9884: mov      x29, xzr
0x027A9888: add      x8, x20, #0x260
0x027A988C: add      x26, x20, #0x250
0x027A9890: add      x21, x20, #0x268
0x027A9894: mov      w22, #0x3f0
0x027A9898: stp      x20, x8, [sp, #8]
0x027A989C: b        #0x27a9910
0x027A98A0: str      x8, [x9]
0x027A98A4: ldr      x1, [x28]
0x027A98A8: ldr      x0, [x20, #0x268]
0x027A98AC: bl       #0x2260c4c
0x027A98B0: ldr      x8, [x20, #0x270]
0x027A98B4: add      x8, x8, #1
0x027A98B8: str      x8, [x20, #0x270]
0x027A98BC: adrp     x1, #0x11b3000
0x027A98C0: adrp     x2, #0x11a6000
0x027A98C4: ldr      w4, [x25, #0x20]
0x027A98C8: mov      x0, x23
0x027A98CC: add      x1, x1, #0x8eb
0x027A98D0: add      x2, x2, #0xf31
0x027A98D4: mov      w3, w24
0x027A98D8: bl       #0x2185854
0x027A98DC: ldp      x24, x8, [x19, #0x68]
0x027A98E0: mov      x10, #0xefbf
0x027A98E4: add      w9, w29, #1
0x027A98E8: movk     x10, #0xbefb, lsl #16
0x027A98EC: sxtw     x29, w9
0x027A98F0: movk     x10, #0xfbef, lsl #32
0x027A98F4: mov      w22, #0x3f0
0x027A98F8: movk     x10, #0xefbe, lsl #48
0x027A98FC: sub      x8, x8, x24
0x027A9900: asr      x8, x8, #4
0x027A9904: mul      x8, x8, x10
0x027A9908: cmp      x8, x29
0x027A990C: b.ls     #0x27a9ba0
0x027A9910: madd     x8, x29, x22, x24
0x027A9914: ldr      w9, [x8, #0x18]
0x027A9918: ldr      x10, [x8, #0x298]
0x027A991C: mov      w8, #1
0x027A9920: cmp      w9, #1
0x027A9924: cinc     w8, w8, eq
0x027A9928: cmp      x10, x8
0x027A992C: b.lo     #0x27a9a20
0x027A9930: madd     x9, x29, x22, x24
0x027A9934: sub      w8, w8, #1
0x027A9938: add      x28, x9, #8
0x027A993C: ldr      x10, [x9, #0x290]
0x027A9940: ldr      x10, [x10]
0x027A9944: lsr      x8, x10, x8
0x027A9948: tst      x8, #1
0x027A994C: ldp      x10, x8, [sp, #0x10]
0x027A9950: csel     x25, x10, x8, eq
0x027A9954: mov      x27, x25
0x027A9958: ldr      x22, [x27, #8]!
0x027A995C: cbz      x22, #0x27a99a4
0x027A9960: add      x27, x25, #8
0x027A9964: ldr      w8, [x28]
0x027A9968: ldr      w9, [x22, #0x1c]
0x027A996C: cmp      w8, w9
0x027A9970: b.ge     #0x27a9988
0x027A9974: ldr      x9, [x22]
0x027A9978: cbz      x9, #0x27a99ac
0x027A997C: mov      x27, x22
0x027A9980: mov      x22, x9
0x027A9984: b        #0x27a9968
0x027A9988: cmp      w9, w8
0x027A998C: b.ge     #0x27a99b0
0x027A9990: mov      x27, x22
0x027A9994: ldr      x9, [x27, #8]!
0x027A9998: cbz      x9, #0x27a99b0
0x027A999C: mov      x22, x9
0x027A99A0: b        #0x27a9968
0x027A99A4: mov      x22, x27
0x027A99A8: b        #0x27a99b0
0x027A99AC: mov      x27, x22
0x027A99B0: ldr      x23, [x27]
0x027A99B4: mov      x20, x19
0x027A99B8: ldr      w19, [x19]
0x027A99BC: cbnz     x23, #0x27a9a10
0x027A99C0: mov      w0, #0x28
0x027A99C4: bl       #0x4b40050
0x027A99C8: ldr      w8, [x28]
0x027A99CC: stp      xzr, xzr, [x0]
0x027A99D0: str      x22, [x0, #0x10]
0x027A99D4: mov      x23, x0
0x027A99D8: stp      w8, wzr, [x0, #0x1c]
0x027A99DC: str      x0, [x27]
0x027A99E0: ldr      x8, [x25]
0x027A99E4: ldr      x8, [x8]
0x027A99E8: cbz      x8, #0x27a99f8
0x027A99EC: str      x8, [x25]
0x027A99F0: ldr      x1, [x27]
0x027A99F4: b        #0x27a99fc
0x027A99F8: mov      x1, x23
0x027A99FC: ldr      x0, [x25, #8]
0x027A9A00: bl       #0x2260c4c
0x027A9A04: ldr      x8, [x25, #0x10]
0x027A9A08: add      x8, x8, #1
0x027A9A0C: str      x8, [x25, #0x10]
0x027A9A10: str      w19, [x23, #0x20]
0x027A9A14: mov      x19, x20
0x027A9A18: ldr      x20, [sp, #8]
0x027A9A1C: mov      w22, #0x3f0
0x027A9A20: adrp     x8, #0x509c000
0x027A9A24: ldr      x8, [x8, #0x70]
0x027A9A28: blr      x8
0x027A9A2C: madd     x8, x29, x22, x24
0x027A9A30: mov      x23, x0
0x027A9A34: ldr      x22, [x26]
0x027A9A38: add      x27, x8, #8
0x027A9A3C: cbz      x22, #0x27a9a84
0x027A9A40: ldr      w8, [x27]
0x027A9A44: mov      x25, x26
0x027A9A48: ldr      w9, [x22, #0x1c]
0x027A9A4C: cmp      w8, w9
0x027A9A50: b.ge     #0x27a9a68
0x027A9A54: ldr      x9, [x22]
0x027A9A58: cbz      x9, #0x27a9ad0
0x027A9A5C: mov      x25, x22
0x027A9A60: mov      x22, x9
0x027A9A64: b        #0x27a9a48
0x027A9A68: cmp      w9, w8
0x027A9A6C: b.ge     #0x27a9a8c
0x027A9A70: mov      x25, x22
0x027A9A74: ldr      x9, [x25, #8]!
0x027A9A78: cbz      x9, #0x27a9a8c
0x027A9A7C: mov      x22, x9
0x027A9A80: b        #0x27a9a48
0x027A9A84: mov      x22, x26
0x027A9A88: mov      x25, x26
0x027A9A8C: ldr      x24, [x25]
0x027A9A90: cbnz     x24, #0x27a9af8
0x027A9A94: mov      w0, #0x28
0x027A9A98: bl       #0x4b40050
0x027A9A9C: ldr      w8, [x27]
0x027A9AA0: stp      xzr, xzr, [x0]
0x027A9AA4: ldr      x9, [sp, #0x18]
0x027A9AA8: str      x22, [x0, #0x10]
0x027A9AAC: mov      x24, x0
0x027A9AB0: stp      w8, wzr, [x0, #0x1c]
0x027A9AB4: str      x0, [x25]
0x027A9AB8: ldr      x8, [x9]
0x027A9ABC: ldr      x8, [x8]
0x027A9AC0: cbz      x8, #0x27a9ae0
0x027A9AC4: str      x8, [x9]
0x027A9AC8: ldr      x1, [x25]
0x027A9ACC: b        #0x27a9ae4
0x027A9AD0: mov      x25, x22
0x027A9AD4: ldr      x24, [x25]
0x027A9AD8: cbnz     x24, #0x27a9af8
0x027A9ADC: b        #0x27a9a94
0x027A9AE0: mov      x1, x24
0x027A9AE4: ldr      x0, [x20, #0x250]
0x027A9AE8: bl       #0x2260c4c
0x027A9AEC: ldr      x8, [x20, #0x258]
0x027A9AF0: add      x8, x8, #1
0x027A9AF4: str      x8, [x20, #0x258]
0x027A9AF8: ldr      x22, [x21]
0x027A9AFC: ldr      w24, [x24, #0x20]
0x027A9B00: cbz      x22, #0x27a9b48
0x027A9B04: ldr      w8, [x27]
0x027A9B08: mov      x28, x21
0x027A9B0C: ldr      w9, [x22, #0x1c]
0x027A9B10: cmp      w8, w9
0x027A9B14: b.ge     #0x27a9b2c
0x027A9B18: ldr      x9, [x22]
0x027A9B1C: cbz      x9, #0x27a9b90
0x027A9B20: mov      x28, x22
0x027A9B24: mov      x22, x9
0x027A9B28: b        #0x27a9b0c
0x027A9B2C: cmp      w9, w8
0x027A9B30: b.ge     #0x27a9b50
0x027A9B34: mov      x28, x22
0x027A9B38: ldr      x9, [x28, #8]!
0x027A9B3C: cbz      x9, #0x27a9b50
0x027A9B40: mov      x22, x9
0x027A9B44: b        #0x27a9b0c
0x027A9B48: mov      x22, x21
0x027A9B4C: mov      x28, x21
0x027A9B50: ldr      x25, [x28]
0x027A9B54: cbnz     x25, #0x27a98bc
0x027A9B58: mov      w0, #0x28
0x027A9B5C: bl       #0x4b40050
0x027A9B60: ldr      w8, [x27]
0x027A9B64: stp      xzr, xzr, [x0]
0x027A9B68: ldr      x9, [sp, #0x10]
0x027A9B6C: str      x22, [x0, #0x10]
0x027A9B70: mov      x25, x0
0x027A9B74: stp      w8, wzr, [x0, #0x1c]
0x027A9B78: str      x0, [x28]
0x027A9B7C: ldr      x8, [x9]
0x027A9B80: ldr      x8, [x8]
0x027A9B84: cbnz     x8, #0x27a98a0
0x027A9B88: mov      x1, x25
0x027A9B8C: b        #0x27a98a8
0x027A9B90: mov      x28, x22
0x027A9B94: ldr      x25, [x28]
0x027A9B98: cbnz     x25, #0x27a98bc
0x027A9B9C: b        #0x27a9b58
0x027A9BA0: ldp      x20, x19, [sp, #0x70]
0x027A9BA4: mov      w0, #1
0x027A9BA8: ldp      x22, x21, [sp, #0x60]
0x027A9BAC: ldp      x24, x23, [sp, #0x50]
0x027A9BB0: ldp      x26, x25, [sp, #0x40]
0x027A9BB4: ldp      x28, x27, [sp, #0x30]
0x027A9BB8: ldp      x29, x30, [sp, #0x20]
0x027A9BBC: add      sp, sp, #0x80
0x027A9BC0: ret      
0x027A9BC4: ldr      x8, [x19, #0x68]
0x027A9BC8: cmp      x22, x8
0x027A9BCC: b.eq     #0x27a9878
0x027A9BD0: add      x23, x20, #0x250
0x027A9BD4: add      x24, x20, #0x268
0x027A9BD8: mov      w25, #-0x4b
0x027A9BDC: mov      w26, #1
~~~

### Function start 0x27c003c
Hits: [{"pc": "0x27c31dc", "adrp": "0x27c31d4", "target": "0x11d1fed", "label": "invisible_visible_rule_case1", "keywords": ["invisible"], "fde_start": "0x27c003c", "fde_end": "0x27cee04", "kind": "add", "reg": "x8"}, {"pc": "0x27c501c", "adrp": "0x27c5014", "target": "0x1173977", "label": "kUseMoveDirRandom", "keywords": ["MoveDir"], "fde_start": "0x27c003c", "fde_end": "0x27cee04", "kind": "add", "reg": "x9"}]
~~~asm
0x027C003C: stp      x29, x30, [sp, #-0x60]!
0x027C0040: stp      x28, x27, [sp, #0x10]
0x027C0044: stp      x26, x25, [sp, #0x20]
0x027C0048: stp      x24, x23, [sp, #0x30]
0x027C004C: stp      x22, x21, [sp, #0x40]
0x027C0050: stp      x20, x19, [sp, #0x50]
0x027C0054: sub      sp, sp, #0x1d0
0x027C0058: adrp     x25, #0x542b000
0x027C005C: add      x8, x0, #0x944
0x027C0060: add      x25, x25, #0x410
0x027C0064: add      x11, x0, #0x98c
0x027C0068: movi     v0.2d, #0000000000000000
0x027C006C: add      x24, x0, #0xacc
0x027C0070: movi     v1.2d, #0000000000000000
0x027C0074: mov      w12, #-1
0x027C0078: ldr      x9, [x25]
0x027C007C: mov      x19, x0
0x027C0080: ldr      w10, [x25, #8]
0x027C0084: str      wzr, [x0, #0x560]
0x027C0088: str      w12, [x0, #0xa78]
0x027C008C: mov      x29, x1
0x027C0090: str      x9, [x8]
0x027C0094: str      w10, [x8, #8]
0x027C0098: add      x8, x0, #0xa68
0x027C009C: str      x9, [x11]
0x027C00A0: str      w10, [x11, #8]
0x027C00A4: add      x11, x0, #0xa7c
0x027C00A8: str      q0, [x8]
0x027C00AC: add      x8, x0, #0x95c
0x027C00B0: str      x9, [x0, #0xa88]
0x027C00B4: str      x9, [x11]
0x027C00B8: str      x9, [x8]
0x027C00BC: mov      w9, #0x4240
0x027C00C0: movk     w9, #0xf, lsl #16
0x027C00C4: str      d1, [x24]
0x027C00C8: str      d1, [x0, #0x1ad0]
0x027C00CC: movi     v1.2d, #0xffffffffffffffff
0x027C00D0: str      w10, [x11, #8]
0x027C00D4: str      w10, [x0, #0xa90]
0x027C00D8: add      x11, x0, #0x968
0x027C00DC: str      w10, [x8, #8]
0x027C00E0: mov      w10, #0x1b24
0x027C00E4: str      w9, [x8, #8]
0x027C00E8: add      x8, x0, #0x9c0
0x027C00EC: str      w9, [x0, #0x95c]
0x027C00F0: mov      w9, #0x1ae4
0x027C00F4: str      wzr, [x0, #0x1c9c]
0x027C00F8: add      x9, x0, x9
0x027C00FC: strb     wzr, [x0, x10]
0x027C0100: str      wzr, [x0, #0xad4]
0x027C0104: str      wzr, [x0, #0xc1c]
0x027C0108: strb     wzr, [x0, #0xadc]
0x027C010C: str      wzr, [x0, #0xaec]
0x027C0110: str      wzr, [x0, #0xae0]
0x027C0114: str      wzr, [x0, #0xb54]
0x027C0118: str      wzr, [x0, #0xb60]
0x027C011C: strh     wzr, [x0, #0xa94]
0x027C0120: str      xzr, [x0, #0x9c0]
0x027C0124: stur     xzr, [x8, #6]
0x027C0128: add      x8, x0, #0xa98
0x027C012C: str      d1, [x0, #0x1b18]
0x027C0130: str      w12, [x0, #0x1b20]
0x027C0134: strb     wzr, [x0, x10]
0x027C0138: mov      w0, #0x30
0x027C013C: stp      q0, q0, [x11]
0x027C0140: str      wzr, [x11, #0x20]
0x027C0144: strb     wzr, [x9, #0x18]
0x027C0148: str      xzr, [x9, #0x10]
0x027C014C: str      q0, [x9]
0x027C0150: str      xzr, [x8, #0x10]
0x027C0154: str      q0, [x8]
0x027C0158: bl       #0x4b40050
0x027C015C: adrp     x9, #0x11f4000
0x027C0160: adrp     x8, #0x113d000
0x027C0164: add      x9, x9, #0x2d5
0x027C0168: add      x21, x19, #0xf0
0x027C016C: mov      x22, x0
0x027C0170: str      x0, [sp, #0x1c0]
0x027C0174: ldr      q3, [x8, #0xb70]
0x027C0178: strb     wzr, [x0, #0x2b]
0x027C017C: ldp      q0, q1, [x9]
0x027C0180: add      x1, sp, #0x178
0x027C0184: add      x2, sp, #0x1b0
0x027C0188: str      q3, [sp, #0x1b0]
0x027C018C: ldur     q2, [x9, #0x1b]
0x027C0190: stp      q0, q1, [x0]
0x027C0194: stur     q2, [x0, #0x1b]
0x027C0198: mov      x0, x21
0x027C019C: bl       #0x226b36c
0x027C01A0: ldr      x8, [x0]
0x027C01A4: cbz      x8, #0x27c01b4
0x027C01A8: mov      x0, x22
0x027C01AC: bl       #0x4b3fb60
0x027C01B0: b        #0x27c0214
0x027C01B4: mov      x23, x0
0x027C01B8: mov      w0, #0x38
0x027C01BC: bl       #0x4b40050
0x027C01C0: mov      x1, x0
0x027C01C4: ldr      x8, [sp, #0x1c0]
0x027C01C8: stp      xzr, xzr, [x1]
0x027C01CC: ldr      q0, [sp, #0x1b0]
0x027C01D0: stp      xzr, xzr, [sp, #0x1b8]
0x027C01D4: str      xzr, [sp, #0x1b0]
0x027C01D8: str      x8, [x1, #0x30]
0x027C01DC: ldr      x8, [sp, #0x178]
0x027C01E0: str      q0, [x1, #0x20]
0x027C01E4: str      x8, [x1, #0x10]
0x027C01E8: str      x1, [x23]
0x027C01EC: ldr      x8, [x21]
0x027C01F0: ldr      x8, [x8]
0x027C01F4: cbz      x8, #0x27c0200
0x027C01F8: str      x8, [x21]
0x027C01FC: ldr      x1, [x23]
0x027C0200: ldr      x0, [x19, #0xf8]
0x027C0204: bl       #0x2260c4c
0x027C0208: ldr      x8, [x19, #0x100]
0x027C020C: add      x8, x8, #1
0x027C0210: str      x8, [x19, #0x100]
0x027C0214: mov      w8, #0x24
0x027C0218: adrp     x10, #0x1166000
0x027C021C: mov      w9, #0x6b63
0x027C0220: add      x10, x10, #0x647
0x027C0224: add      x1, sp, #0x178
0x027C0228: add      x2, sp, #0x1b0
0x027C022C: strb     w8, [sp, #0x1b0]
0x027C0230: add      x8, sp, #0xc2
0x027C0234: ldr      q0, [x10]
0x027C0238: mov      x0, x21
0x027C023C: strb     wzr, [sp, #0x1c3]
0x027C0240: sturh    w9, [x8, #0xff]
0x027C0244: add      x8, sp, #0xb2
0x027C0248: stur     q0, [x8, #0xff]
0x027C024C: bl       #0x226b36c
0x027C0250: ldr      x8, [x0]
0x027C0254: cbnz     x8, #0x27c02bc
0x027C0258: mov      x22, x0
0x027C025C: mov      w0, #0x38
0x027C0260: bl       #0x4b40050
0x027C0264: ldr      x8, [sp, #0x1c0]
0x027C0268: str      xzr, [sp, #0x1c0]
0x027C026C: ldr      q0, [sp, #0x1b0]
0x027C0270: stp      xzr, xzr, [sp, #0x1b0]
0x027C0274: stp      xzr, xzr, [x0]
0x027C0278: str      x8, [x0, #0x30]
0x027C027C: ldr      x8, [sp, #0x178]
0x027C0280: str      q0, [x0, #0x20]
0x027C0284: str      x8, [x0, #0x10]
0x027C0288: str      x0, [x22]
0x027C028C: ldr      x8, [x21]
0x027C0290: ldr      x8, [x8]
0x027C0294: cbz      x8, #0x27c02a4
0x027C0298: str      x8, [x21]
0x027C029C: ldr      x1, [x22]
0x027C02A0: b        #0x27c02a8
0x027C02A4: mov      x1, x0
0x027C02A8: ldr      x0, [x19, #0xf8]
0x027C02AC: bl       #0x2260c4c
0x027C02B0: ldr      x8, [x19, #0x100]
0x027C02B4: add      x8, x8, #1
0x027C02B8: str      x8, [x19, #0x100]
0x027C02BC: adrp     x9, #0x1179000
0x027C02C0: mov      w8, #0x2c
0x027C02C4: add      x9, x9, #0xc45
0x027C02C8: add      x1, sp, #0x178
0x027C02CC: add      x2, sp, #0x1b0
0x027C02D0: mov      x0, x21
0x027C02D4: strb     w8, [sp, #0x1b0]
0x027C02D8: add      x8, sp, #0xb2
0x027C02DC: ldr      q0, [x9]
0x027C02E0: strb     wzr, [sp, #0x1c7]
0x027C02E4: ldur     x9, [x9, #0xe]
0x027C02E8: stur     q0, [x8, #0xff]
0x027C02EC: add      x8, sp, #0xc0
0x027C02F0: stur     x9, [x8, #0xff]
0x027C02F4: bl       #0x226b36c
0x027C02F8: ldr      x8, [x0]
0x027C02FC: cbnz     x8, #0x27c0364
0x027C0300: mov      x22, x0
0x027C0304: mov      w0, #0x38
0x027C0308: bl       #0x4b40050
0x027C030C: ldr      x8, [sp, #0x1c0]
0x027C0310: str      xzr, [sp, #0x1c0]
0x027C0314: ldr      q0, [sp, #0x1b0]
0x027C0318: stp      xzr, xzr, [sp, #0x1b0]
0x027C031C: stp      xzr, xzr, [x0]
0x027C0320: str      x8, [x0, #0x30]
0x027C0324: ldr      x8, [sp, #0x178]
0x027C0328: str      q0, [x0, #0x20]
0x027C032C: str      x8, [x0, #0x10]
0x027C0330: str      x0, [x22]
0x027C0334: ldr      x8, [x21]
0x027C0338: ldr      x8, [x8]
0x027C033C: cbz      x8, #0x27c034c
0x027C0340: str      x8, [x21]
0x027C0344: ldr      x1, [x22]
0x027C0348: b        #0x27c0350
0x027C034C: mov      x1, x0
0x027C0350: ldr      x0, [x19, #0xf8]
0x027C0354: bl       #0x2260c4c
0x027C0358: ldr      x8, [x19, #0x100]
0x027C035C: add      x8, x8, #1
0x027C0360: str      x8, [x19, #0x100]
0x027C0364: mov      w0, #0x30
0x027C0368: bl       #0x4b40050
0x027C036C: adrp     x9, #0x1173000
0x027C0370: adrp     x8, #0x113c000
0x027C0374: add      x9, x9, #0x8fc
0x027C0378: mov      x22, x0
0x027C037C: str      x0, [sp, #0x1c0]
0x027C0380: add      x1, sp, #0x178
0x027C0384: ldr      q2, [x8, #0xb90]
0x027C0388: strb     wzr, [x0, #0x25]
0x027C038C: ldp      q0, q1, [x9]
0x027C0390: add      x2, sp, #0x1b0
0x027C0394: str      q2, [sp, #0x80]
0x027C0398: str      q2, [sp, #0x1b0]
0x027C039C: ldur     x9, [x9, #0x1d]
0x027C03A0: stp      q0, q1, [x0]
0x027C03A4: stur     x9, [x0, #0x1d]
0x027C03A8: mov      x0, x21
0x027C03AC: bl       #0x226b36c
0x027C03B0: ldr      x8, [x0]
0x027C03B4: cbz      x8, #0x27c03c4
0x027C03B8: mov      x0, x22
0x027C03BC: bl       #0x4b3fb60
0x027C03C0: b        #0x27c0424
0x027C03C4: mov      x23, x0
0x027C03C8: mov      w0, #0x38
0x027C03CC: bl       #0x4b40050
0x027C03D0: mov      x1, x0
0x027C03D4: ldr      x8, [sp, #0x1c0]
0x027C03D8: stp      xzr, xzr, [x1]
0x027C03DC: ldr      q0, [sp, #0x1b0]
0x027C03E0: stp      xzr, xzr, [sp, #0x1b8]
0x027C03E4: str      xzr, [sp, #0x1b0]
0x027C03E8: str      x8, [x1, #0x30]
0x027C03EC: ldr      x8, [sp, #0x178]
0x027C03F0: str      q0, [x1, #0x20]
0x027C03F4: str      x8, [x1, #0x10]
0x027C03F8: str      x1, [x23]
~~~

### Function start 0x27e5438
Hits: [{"pc": "0x27e5a48", "adrp": "0x27e5a40", "target": "0x1207f17", "label": "target_monster_hp_rate is less than STAY_WITH_MONSTER_HP threshold. Change MoveDir to NormAtk", "keywords": ["MoveDir"], "fde_start": "0x27e5438", "fde_end": "0x27e5ed8", "kind": "add", "reg": "x2"}, {"pc": "0x27e5bf0", "adrp": "0x27e5be8", "target": "0x11fb2c5", "label": "more restrict Laye rule for bailixuance. Change MoveDir to MovePos", "keywords": ["MoveDir"], "fde_start": "0x27e5438", "fde_end": "0x27e5ed8", "kind": "add", "reg": "x2"}]
~~~asm
0x027E5438: sub      sp, sp, #0x90
0x027E543C: stp      d9, d8, [sp, #0x20]
0x027E5440: stp      x29, x30, [sp, #0x30]
0x027E5444: stp      x28, x27, [sp, #0x40]
0x027E5448: stp      x26, x25, [sp, #0x50]
0x027E544C: stp      x24, x23, [sp, #0x60]
0x027E5450: stp      x22, x21, [sp, #0x70]
0x027E5454: stp      x20, x19, [sp, #0x80]
0x027E5458: ldr      x8, [x0, #0xfc0]
0x027E545C: mov      x20, x2
0x027E5460: ldr      x9, [x0, #0xfc8]
0x027E5464: mov      x19, x0
0x027E5468: mov      x21, x1
0x027E546C: cmp      x8, x9
0x027E5470: b.eq     #0x27e549c
0x027E5474: ldr      x10, [x19, #0x900]
0x027E5478: ldr      w10, [x10, #4]
0x027E547C: ldr      w11, [x8]
0x027E5480: cmp      w11, w10
0x027E5484: b.eq     #0x27e549c
0x027E5488: add      x8, x8, #4
0x027E548C: cmp      x8, x9
0x027E5490: b.ne     #0x27e547c
0x027E5494: mov      w8, #1
0x027E5498: b        #0x27e54d4
0x027E549C: cmp      x8, x9
0x027E54A0: ldrb     w10, [x19, #0xfd8]
0x027E54A4: cset     w8, eq
0x027E54A8: cbz      w10, #0x27e54d4
0x027E54AC: b.eq     #0x27e54d4
0x027E54B0: adrp     x8, #0x509c000
0x027E54B4: ldr      x8, [x8, #0x70]
0x027E54B8: blr      x8
0x027E54BC: ldr      x8, [x19, #0x900]
0x027E54C0: adrp     x1, #0x1146000
0x027E54C4: adrp     x2, #0x1193000
0x027E54C8: add      x1, x1, #0x1af
0x027E54CC: add      x2, x2, #0x919
0x027E54D0: b        #0x27e5500
0x027E54D4: ldrb     w9, [x19, #0xfd9]
0x027E54D8: cbz      w9, #0x27e550c
0x027E54DC: cbz      w8, #0x27e550c
0x027E54E0: adrp     x8, #0x509c000
0x027E54E4: ldr      x8, [x8, #0x70]
0x027E54E8: blr      x8
0x027E54EC: ldr      x8, [x19, #0x900]
0x027E54F0: adrp     x1, #0x1146000
0x027E54F4: adrp     x2, #0x11fb000
0x027E54F8: add      x1, x1, #0x1af
0x027E54FC: add      x2, x2, #0x2a0
0x027E5500: ldr      w3, [x8, #4]
0x027E5504: bl       #0x2185854
0x027E5508: b        #0x27e5678
0x027E550C: ldr      w8, [x19, #0xef4]
0x027E5510: cbz      w8, #0x27e55bc
0x027E5514: adrp     x8, #0x5089000
0x027E5518: add      x23, x19, #0xef4
0x027E551C: add      x0, x19, #0xed8
0x027E5520: mov      x1, x23
0x027E5524: ldr      x8, [x8, #0x210]
0x027E5528: blr      x8
0x027E552C: add      x8, x19, #0xee0
0x027E5530: cmp      x8, x0
0x027E5534: b.eq     #0x27e55dc
0x027E5538: ldr      s0, [x19, #0xf1c]
0x027E553C: adrp     x8, #0x1212000
0x027E5540: ldr      s1, [x19, #0xf24]
0x027E5544: scvtf    s0, s0
0x027E5548: scvtf    s1, s1
0x027E554C: fdiv     s8, s0, s1
0x027E5550: ldr      d0, [x8, #0x768]
0x027E5554: fcvt     d9, s8
0x027E5558: fcmp     d9, d0
0x027E555C: b.le     #0x27e5570
0x027E5560: ldr      s1, [x19, #0x9a4]
0x027E5564: ldr      s2, [x19, #0x1324]
0x027E5568: fcmp     s1, s2
0x027E556C: b.mi     #0x27e5590
0x027E5570: fcmp     d9, d0
0x027E5574: b.hi     #0x27e55fc
0x027E5578: ldr      s0, [x19, #0x1324]
0x027E557C: fmov     s1, #0.50000000
0x027E5580: fmul     s0, s0, s1
0x027E5584: ldr      s1, [x19, #0x9a4]
0x027E5588: fcmp     s1, s0
0x027E558C: b.pl     #0x27e55fc
0x027E5590: adrp     x8, #0x509c000
0x027E5594: ldr      x8, [x8, #0x70]
0x027E5598: blr      x8
0x027E559C: ldr      s0, [x19, #0x9a4]
0x027E55A0: adrp     x1, #0x1146000
0x027E55A4: adrp     x2, #0x1166000
0x027E55A8: add      x1, x1, #0x1af
0x027E55AC: add      x2, x2, #0xc64
0x027E55B0: fcvt     d0, s0
0x027E55B4: bl       #0x2185854
0x027E55B8: b        #0x27e5678
0x027E55BC: adrp     x8, #0x509c000
0x027E55C0: ldr      x8, [x8, #0x70]
0x027E55C4: blr      x8
0x027E55C8: adrp     x1, #0x1146000
0x027E55CC: adrp     x2, #0x1199000
0x027E55D0: add      x1, x1, #0x1af
0x027E55D4: add      x2, x2, #0xa98
0x027E55D8: b        #0x27e5674
0x027E55DC: adrp     x8, #0x509c000
0x027E55E0: ldr      x8, [x8, #0x70]
0x027E55E4: blr      x8
0x027E55E8: adrp     x1, #0x1146000
0x027E55EC: adrp     x2, #0x1173000
0x027E55F0: add      x1, x1, #0x1af
0x027E55F4: add      x2, x2, #0xc13
0x027E55F8: b        #0x27e5674
0x027E55FC: adrp     x8, #0x509c000
0x027E5600: mov      x0, x19
0x027E5604: mov      x1, x21
0x027E5608: mov      w2, #0x96
0x027E560C: ldr      x8, [x8, #0x800]
0x027E5610: blr      x8
0x027E5614: tbz      w0, #0, #0x27e5638
0x027E5618: adrp     x8, #0x509c000
0x027E561C: ldr      x8, [x8, #0x70]
0x027E5620: blr      x8
0x027E5624: adrp     x1, #0x1146000
0x027E5628: adrp     x2, #0x11a0000
0x027E562C: add      x1, x1, #0x1af
0x027E5630: add      x2, x2, #6
0x027E5634: b        #0x27e5674
0x027E5638: adrp     x8, #0x517f000
0x027E563C: add      x22, x19, #0x134
0x027E5640: ldr      w2, [x19, #0xef0]
0x027E5644: mov      x0, x22
0x027E5648: mov      x1, x21
0x027E564C: ldr      x8, [x8, #0xbe8]
0x027E5650: blr      x8
0x027E5654: tbz      w0, #0, #0x27e56a0
0x027E5658: adrp     x8, #0x509c000
0x027E565C: ldr      x8, [x8, #0x70]
0x027E5660: blr      x8
0x027E5664: adrp     x1, #0x1146000
0x027E5668: adrp     x2, #0x1180000
0x027E566C: add      x1, x1, #0x1af
0x027E5670: add      x2, x2, #0x5bd
0x027E5674: bl       #0x2185854
0x027E5678: mov      w0, wzr
0x027E567C: ldp      x20, x19, [sp, #0x80]
0x027E5680: ldp      x22, x21, [sp, #0x70]
0x027E5684: ldp      x24, x23, [sp, #0x60]
0x027E5688: ldp      x26, x25, [sp, #0x50]
0x027E568C: ldp      x28, x27, [sp, #0x40]
0x027E5690: ldp      x29, x30, [sp, #0x30]
0x027E5694: ldp      d9, d8, [sp, #0x20]
0x027E5698: add      sp, sp, #0x90
0x027E569C: ret      
0x027E56A0: add      x24, x19, #0xef0
0x027E56A4: mov      w0, wzr
0x027E56A8: mov      w9, #0xc4df
0x027E56AC: ldr      w8, [x24]
0x027E56B0: cmp      w8, w9
0x027E56B4: b.le     #0x27e56e0
0x027E56B8: mov      w9, #0xc4e0
0x027E56BC: cmp      w8, w9
0x027E56C0: b.eq     #0x27e567c
0x027E56C4: mov      w9, #0x56b8
0x027E56C8: movk     w9, #0x19, lsl #16
0x027E56CC: cmp      w8, w9
0x027E56D0: b.eq     #0x27e567c
0x027E56D4: mov      w9, #0x56c2
0x027E56D8: movk     w9, #0x19, lsl #16
0x027E56DC: b        #0x27e56f0
0x027E56E0: mov      w9, #0x401a
0x027E56E4: cmp      w8, w9
0x027E56E8: b.eq     #0x27e56fc
0x027E56EC: mov      w9, #0x4524
0x027E56F0: cmp      w8, w9
0x027E56F4: b.eq     #0x27e567c
0x027E56F8: b        #0x27e570c
0x027E56FC: ldr      x9, [x19, #0x900]
0x027E5700: ldr      w9, [x9, #0x90]
0x027E5704: cmp      w9, #3
0x027E5708: b.ne     #0x27e5678
0x027E570C: adrp     x9, #0x542b000
0x027E5710: ldr      x9, [x9, #0xfe8]
0x027E5714: cbz      x9, #0x27e5750
0x027E5718: adrp     x11, #0x542b000
0x027E571C: add      x11, x11, #0xfe8
0x027E5720: mov      x10, x11
0x027E5724: ldr      w12, [x9, #0x1c]
0x027E5728: cmp      w12, w8
0x027E572C: cset     w12, lt
0x027E5730: csel     x10, x10, x9, lt
0x027E5734: ldr      x9, [x9, w12, uxtw #3]
0x027E5738: cbnz     x9, #0x27e5724
0x027E573C: cmp      x10, x11
0x027E5740: b.eq     #0x27e5750
0x027E5744: ldr      w9, [x10, #0x1c]
0x027E5748: cmp      w8, w9
0x027E574C: b.ge     #0x27e5678
0x027E5750: adrp     x8, #0x517f000
0x027E5754: mov      x0, x22
0x027E5758: mov      x1, x24
0x027E575C: ldr      x8, [x8, #0xb58]
0x027E5760: blr      x8
0x027E5764: adrp     x8, #0x1211000
0x027E5768: tbz      w0, #0, #0x27e5778
0x027E576C: ldr      d0, [x8, #0xd50]
0x027E5770: fcmp     d9, d0
0x027E5774: b.ls     #0x27e5798
0x027E5778: adrp     x8, #0x517f000
0x027E577C: add      x2, x19, #0xf04
0x027E5780: mov      x0, x22
0x027E5784: mov      x1, x21
0x027E5788: mov      w3, #1
0x027E578C: ldr      x8, [x8, #0xee8]
0x027E5790: blr      x8
0x027E5794: tbz      w0, #0, #0x27e5678
0x027E5798: ldr      w8, [x19, #0xc20]
0x027E579C: cmp      w8, #0xf
0x027E57A0: b.ne     #0x27e57e8
0x027E57A4: ldr      x8, [x19, #0x900]
0x027E57A8: adrp     x9, #0x517f000
0x027E57AC: add      x2, x19, #0xf04
0x027E57B0: mov      x0, x22
0x027E57B4: add      x1, x8, #0x20
0x027E57B8: ldr      x8, [x9, #0x308]
0x027E57BC: blr      x8
0x027E57C0: adrp     x8, #0x517f000
0x027E57C4: add      x2, x20, #0x158
0x027E57C8: str      x0, [sp, #0x10]
0x027E57CC: mov      x0, x22
0x027E57D0: str      w1, [sp, #0x18]
0x027E57D4: add      x1, sp, #0x10
0x027E57D8: ldr      x8, [x8, #0x6c8]
0x027E57DC: blr      x8
0x027E57E0: cmp      w0, #0x10
0x027E57E4: b.lt     #0x27e5678
0x027E57E8: ldr      x8, [x19, #0x900]
0x027E57EC: stp      x24, x22, [sp]
0x027E57F0: ldp      x9, x10, [x8, #0x130]
0x027E57F4: cmp      x10, x9
~~~

### Function start 0x27fac24
Hits: [{"pc": "0x27fb474", "adrp": "0x27fb46c", "target": "0x11537ac", "label": "mask skill3 -> kMoveDir, hp_rate:%.2f", "keywords": ["MoveDir"], "fde_start": "0x27fac24", "fde_end": "0x27fbde0", "kind": "add", "reg": "x2"}]
~~~asm
0x027FAC24: sub      sp, sp, #0xb0
0x027FAC28: str      d8, [sp, #0x40]
0x027FAC2C: stp      x29, x30, [sp, #0x50]
0x027FAC30: stp      x28, x27, [sp, #0x60]
0x027FAC34: stp      x26, x25, [sp, #0x70]
0x027FAC38: stp      x24, x23, [sp, #0x80]
0x027FAC3C: stp      x22, x21, [sp, #0x90]
0x027FAC40: stp      x20, x19, [sp, #0xa0]
0x027FAC44: ldr      x8, [x0, #0x900]
0x027FAC48: ldr      w9, [x8, #4]
0x027FAC4C: cmp      w9, #0x8a
0x027FAC50: b.ne     #0x27fb47c
0x027FAC54: ldp      x8, x9, [x8, #0x1c0]
0x027FAC58: mov      w10, #0x1bfc
0x027FAC5C: mov      x19, x2
0x027FAC60: mov      x20, x0
0x027FAC64: mov      x21, x1
0x027FAC68: add      x26, x0, x10
0x027FAC6C: sub      x9, x9, x8
0x027FAC70: cmp      x9, #0x101
0x027FAC74: b.lo     #0x27facf0
0x027FAC78: ldr      w8, [x8, #0x114]
0x027FAC7C: mov      x28, x26
0x027FAC80: mov      w9, #0x3608
0x027FAC84: cmp      w8, w9
0x027FAC88: ldrb     w10, [x28, #0x38]!
0x027FAC8C: cset     w22, eq
0x027FAC90: cbz      w10, #0x27fad28
0x027FAC94: cmp      w8, w9
0x027FAC98: b.ne     #0x27facfc
0x027FAC9C: ldr      w8, [x20, #0x1c38]
0x027FACA0: cmp      w8, #1
0x027FACA4: b.lt     #0x27fb020
0x027FACA8: ldr      w9, [x21]
0x027FACAC: sub      w8, w9, w8
0x027FACB0: cmp      w8, #0x1f
0x027FACB4: b.lt     #0x27fb020
0x027FACB8: adrp     x8, #0x509c000
0x027FACBC: ldr      x8, [x8, #0x70]
0x027FACC0: blr      x8
0x027FACC4: adrp     x1, #0x1208000
0x027FACC8: adrp     x2, #0x1199000
0x027FACCC: ldr      w3, [x20, #0x1c38]
0x027FACD0: add      x1, x1, #0x162
0x027FACD4: ldr      w4, [x21]
0x027FACD8: add      x2, x2, #0xc36
0x027FACDC: bl       #0x2185854
0x027FACE0: mov      w22, #1
0x027FACE4: strb     wzr, [x28]
0x027FACE8: str      wzr, [x20, #0x1c38]
0x027FACEC: b        #0x27fad28
0x027FACF0: mov      x28, x26
0x027FACF4: ldrb     w8, [x28, #0x38]!
0x027FACF8: cbz      w8, #0x27fad24
0x027FACFC: adrp     x8, #0x509c000
0x027FAD00: strb     wzr, [x28]
0x027FAD04: str      wzr, [x20, #0x1c38]
0x027FAD08: ldr      x8, [x8, #0x70]
0x027FAD0C: blr      x8
0x027FAD10: adrp     x1, #0x1208000
0x027FAD14: adrp     x2, #0x117a000
0x027FAD18: add      x1, x1, #0x162
0x027FAD1C: add      x2, x2, #0xba
0x027FAD20: bl       #0x2185854
0x027FAD24: mov      w22, wzr
0x027FAD28: ldr      w8, [x20, #0x1c3c]
0x027FAD2C: ldr      s8, [x20, #0x9a4]
0x027FAD30: ldr      w27, [x19, #0x150]
0x027FAD34: cmp      w8, #1
0x027FAD38: b.lt     #0x27fadb8
0x027FAD3C: ldr      w9, [x21]
0x027FAD40: sub      w8, w9, w8
0x027FAD44: cmp      w8, #0xf
0x027FAD48: b.gt     #0x27fadb4
0x027FAD4C: cmp      w27, #7
0x027FAD50: b.ne     #0x27fb47c
0x027FAD54: mov      w8, #0xf
0x027FAD58: adrp     x1, #0x11b3000
0x027FAD5C: add      x0, x19, #0xa48
0x027FAD60: add      x1, x1, #0xed6
0x027FAD64: mov      w2, #0x19
0x027FAD68: str      w8, [x19, #0x150]
0x027FAD6C: ldr      w8, [x20, #0xc38]
0x027FAD70: ldr      x9, [x20, #0xc30]
0x027FAD74: str      w8, [x19, #0x160]
0x027FAD78: str      x9, [x19, #0x158]
0x027FAD7C: bl       #0x2282f58
0x027FAD80: adrp     x8, #0x509c000
0x027FAD84: ldr      x8, [x8, #0x70]
0x027FAD88: blr      x8
0x027FAD8C: ldr      w8, [x21]
0x027FAD90: adrp     x1, #0x1208000
0x027FAD94: ldr      w9, [x20, #0x1c3c]
0x027FAD98: adrp     x2, #0x1166000
0x027FAD9C: add      x1, x1, #0x162
0x027FADA0: add      x2, x2, #0xe29
0x027FADA4: mov      w4, w22
0x027FADA8: sub      w3, w8, w9
0x027FADAC: bl       #0x2185854
0x027FADB0: b        #0x27fb47c
0x027FADB4: str      wzr, [x20, #0x1c3c]
0x027FADB8: tbz      w22, #0, #0x27fae84
0x027FADBC: adrp     x8, #0x517f000
0x027FADC0: add      x23, x20, #0x134
0x027FADC4: ldr      x2, [x20, #0x900]
0x027FADC8: add      x3, sp, #0x30
0x027FADCC: mov      x0, x23
0x027FADD0: mov      x1, x21
0x027FADD4: ldr      x8, [x8, #0xfe8]
0x027FADD8: blr      x8
0x027FADDC: adrp     x8, #0x517f000
0x027FADE0: mov      w24, w0
0x027FADE4: ldr      x2, [x20, #0x900]
0x027FADE8: mov      x0, x23
0x027FADEC: mov      x1, x21
0x027FADF0: ldr      x8, [x8, #0xff8]
0x027FADF4: blr      x8
0x027FADF8: mov      w22, w0
0x027FADFC: tbnz     w0, #0x1f, #0x27fafb4
0x027FAE00: ldr      w8, [x21]
0x027FAE04: sub      w8, w8, w22
0x027FAE08: bic      w25, w8, w8, asr #31
0x027FAE0C: cmp      w25, #4
0x027FAE10: b.ls     #0x27fafb8
0x027FAE14: add      w8, w25, w25, lsl #5
0x027FAE18: ldrb     w9, [x28]
0x027FAE1C: lsl      w22, w8, #1
0x027FAE20: cbz      w9, #0x27fb028
0x027FAE24: mov      w8, #7
0x027FAE28: str      w8, [x19, #0x150]
0x027FAE2C: tbz      w24, #0, #0x27fae40
0x027FAE30: ldr      x8, [sp, #0x30]
0x027FAE34: ldr      w9, [sp, #0x38]
0x027FAE38: str      x8, [x19, #0x170]
0x027FAE3C: str      w9, [x19, #0x178]
0x027FAE40: adrp     x1, #0x118d000
0x027FAE44: add      x0, x19, #0xa48
0x027FAE48: add      x1, x1, #0xbb7
0x027FAE4C: mov      w2, #0x17
0x027FAE50: bl       #0x2282f58
0x027FAE54: adrp     x8, #0x509c000
0x027FAE58: ldr      x8, [x8, #0x70]
0x027FAE5C: blr      x8
0x027FAE60: fcvt     d0, s8
0x027FAE64: adrp     x1, #0x1208000
0x027FAE68: adrp     x2, #0x1193000
0x027FAE6C: add      x1, x1, #0x162
0x027FAE70: add      x2, x2, #0xac5
0x027FAE74: mov      w3, w22
0x027FAE78: mov      w4, w25
0x027FAE7C: bl       #0x2185854
0x027FAE80: b        #0x27fb47c
0x027FAE84: ldrb     w8, [x26]
0x027FAE88: cbz      w8, #0x27fae94
0x027FAE8C: strb     wzr, [x26]
0x027FAE90: str      wzr, [x20, #0x1c00]
0x027FAE94: ldrb     w8, [x26, #0x28]
0x027FAE98: cbz      w8, #0x27faea0
0x027FAE9C: strb     wzr, [x26, #0x28]
0x027FAEA0: ldr      w8, [x20, #0x1bb8]
0x027FAEA4: cmp      w8, #1
0x027FAEA8: b.lt     #0x27fb110
0x027FAEAC: ldr      s0, [x20, #0x1be8]
0x027FAEB0: fcmp     s8, s0
0x027FAEB4: b.le     #0x27fb110
0x027FAEB8: ldr      x8, [x20, #0x900]
0x027FAEBC: ldp      x8, x9, [x8, #0x1c0]
0x027FAEC0: sub      x9, x9, x8
0x027FAEC4: cmp      x9, #0x101
0x027FAEC8: b.lo     #0x27fb110
0x027FAECC: ldrb     w8, [x8, #0x108]
0x027FAED0: cbz      w8, #0x27fb110
0x027FAED4: ldp      x28, x29, [x21, #0x68]
0x027FAED8: cmp      x28, x29
0x027FAEDC: b.eq     #0x27fb110
0x027FAEE0: mov      x23, xzr
0x027FAEE4: mov      w22, wzr
0x027FAEE8: add      x24, x20, #0x134
0x027FAEEC: adrp     x25, #0x517f000
0x027FAEF0: b        #0x27faf00
0x027FAEF4: add      x28, x28, #0x3f0
0x027FAEF8: cmp      x28, x29
0x027FAEFC: b.eq     #0x27fb070
0x027FAF00: ldr      w9, [x28, #0x58]
0x027FAF04: cmp      w9, #1
0x027FAF08: b.lt     #0x27faef4
0x027FAF0C: ldr      x8, [x20, #0x900]
0x027FAF10: ldr      w11, [x28, #0x18]
0x027FAF14: ldr      w10, [x8, #0x18]
0x027FAF18: cmp      w11, w10
0x027FAF1C: b.eq     #0x27faef4
0x027FAF20: cmp      w10, #1
0x027FAF24: b.lt     #0x27faf50
0x027FAF28: ldr      x11, [x28, #0x298]
0x027FAF2C: cmp      x11, x10
0x027FAF30: b.lo     #0x27faf50
0x027FAF34: sub      w10, w10, #1
0x027FAF38: ldr      x12, [x28, #0x290]
0x027FAF3C: lsr      x11, x10, #3
0x027FAF40: and      x11, x11, #0x1ffffff8
0x027FAF44: ldr      x11, [x12, x11]
0x027FAF48: lsr      x10, x11, x10
0x027FAF4C: tbz      w10, #0, #0x27faef4
0x027FAF50: ldr      s0, [x28, #0x60]
0x027FAF54: scvtf    s1, w9
0x027FAF58: scvtf    s0, s0
0x027FAF5C: fdiv     s0, s1, s0
0x027FAF60: ldr      s1, [x20, #0x1be0]
0x027FAF64: fcmp     s0, s1
0x027FAF68: b.ge     #0x27faef4
0x027FAF6C: add      x1, x8, #0x20
0x027FAF70: add      x2, x28, #0x20
0x027FAF74: ldr      x8, [x25, #0x388]
0x027FAF78: mov      x0, x24
0x027FAF7C: mov      w3, #1
0x027FAF80: blr      x8
0x027FAF84: ldr      w8, [x20, #0x1be4]
0x027FAF88: cmp      w0, w8
0x027FAF8C: b.gt     #0x27faef4
0x027FAF90: cmp      x23, #0
0x027FAF94: cset     w8, eq
0x027FAF98: cmp      w0, w22
0x027FAF9C: cset     w9, lt
0x027FAFA0: orr      w8, w8, w9
0x027FAFA4: cmp      w8, #0
0x027FAFA8: csel     w22, w0, w22, ne
0x027FAFAC: csel     x23, x28, x23, ne
0x027FAFB0: b        #0x27faef4
0x027FAFB4: mov      w25, wzr
0x027FAFB8: cmp      w27, #7
0x027FAFBC: b.ne     #0x27fb47c
0x027FAFC0: mov      w8, #0xf
0x027FAFC4: adrp     x1, #0x1193000
0x027FAFC8: add      x0, x19, #0xa48
0x027FAFCC: add      x1, x1, #0xaa0
0x027FAFD0: mov      w2, #0x24
0x027FAFD4: str      w8, [x19, #0x150]
0x027FAFD8: ldr      w8, [x20, #0xc38]
0x027FAFDC: ldr      x9, [x20, #0xc30]
0x027FAFE0: str      w8, [x19, #0x160]
~~~

### Function start 0x2812960
Hits: [{"pc": "0x2812d14", "adrp": "0x2812d0c", "target": "0x11c046c", "label": "CurFrame[%d] Enter Alert Because In HeroAlert, EnemyPos[%d;%d:%d:%d] MainHeroPos[%d;%d:%d:%d] MovePos[%d:%d:%d]\n", "keywords": ["EnemyPos", "MainHeroPos"], "fde_start": "0x2812960", "fde_end": "0x2812d6c", "kind": "add", "reg": "x2"}]
~~~asm
0x02812960: str      x29, [sp, #-0x40]!
0x02812964: stp      x30, x23, [sp, #0x10]
0x02812968: stp      x22, x21, [sp, #0x20]
0x0281296C: stp      x20, x19, [sp, #0x30]
0x02812970: sub      sp, sp, #0x830
0x02812974: mov      x19, x0
0x02812978: add      x0, sp, #0x440
0x0281297C: mov      x20, x2
0x02812980: mov      x21, x1
0x02812984: str      xzr, [sp, #0x838]
0x02812988: bl       #0x4a49db4
0x0281298C: add      x0, sp, #0x50
0x02812990: bl       #0x4a49db4
0x02812994: ldr      w8, [x20]
0x02812998: strb     wzr, [sp, #0x4c]
0x0281299C: ldr      w9, [x19, #0x524]
0x028129A0: strb     wzr, [sp, #0x48]
0x028129A4: ldr      w22, [x21, #0x18]
0x028129A8: sub      w12, w8, w9
0x028129AC: cmp      w12, #2
0x028129B0: b.lt     #0x2812a1c
0x028129B4: ldr      w11, [x19, #0x508]
0x028129B8: cmp      w11, #1
0x028129BC: b.lt     #0x2812a1c
0x028129C0: ldr      w10, [x19, #0x4fc]
0x028129C4: add      w12, w11, w12
0x028129C8: cmp      w12, w10
0x028129CC: b.le     #0x2812a1c
0x028129D0: sub      w8, w9, w11
0x028129D4: adrp     x23, #0x509c000
0x028129D8: add      w8, w8, w10
0x028129DC: str      wzr, [x19, #0x508]
0x028129E0: add      w8, w8, #1
0x028129E4: ldr      x9, [x23, #0x70]
0x028129E8: str      w8, [x19, #0x510]
0x028129EC: blr      x9
0x028129F0: ldr      w3, [x20]
0x028129F4: ldr      w4, [x19, #0x510]
0x028129F8: adrp     x1, #0x1201000
0x028129FC: adrp     x2, #0x11e0000
0x02812A00: add      x1, x1, #0x89b
0x02812A04: add      x2, x2, #0x7fb
0x02812A08: bl       #0x2185854
0x02812A0C: ldr      w9, [x19, #0x510]
0x02812A10: ldr      w8, [x20]
0x02812A14: cmp      w9, w8
0x02812A18: b.ge     #0x2812c04
0x02812A1C: ldr      w9, [x19, #0x504]
0x02812A20: tbnz     w9, #0x1f, #0x2812a8c
0x02812A24: sub      w9, w8, w9
0x02812A28: cmp      w9, #1
0x02812A2C: b.lt     #0x2812a8c
0x02812A30: ldr      w10, [x19, #0x4f8]
0x02812A34: cmp      w9, w10
0x02812A38: b.ge     #0x2812a8c
0x02812A3C: ldr      w9, [x19, #0x524]
0x02812A40: ldr      w10, [x19, #0x508]
0x02812A44: sub      w8, w8, w9
0x02812A48: adrp     x9, #0x509c000
0x02812A4C: add      w8, w8, w10
0x02812A50: ldr      x9, [x9, #0x70]
0x02812A54: str      w8, [x19, #0x508]
0x02812A58: ldr      w8, [x20]
0x02812A5C: str      w8, [x19, #0x524]
0x02812A60: blr      x9
0x02812A64: ldr      w3, [x20]
0x02812A68: ldr      w4, [x19, #0x504]
0x02812A6C: ldr      w5, [x19, #0x508]
0x02812A70: adrp     x1, #0x1201000
0x02812A74: adrp     x2, #0x113f000
0x02812A78: add      x1, x1, #0x89b
0x02812A7C: add      x2, x2, #0xec8
0x02812A80: bl       #0x2185854
0x02812A84: mov      w20, #1
0x02812A88: b        #0x2812c78
0x02812A8C: ldr      w9, [x19, #0x508]
0x02812A90: ldr      w10, [x19, #0x4fc]
0x02812A94: cmp      w9, w10
0x02812A98: b.ge     #0x2812af0
0x02812A9C: ldr      w9, [x19, #0x510]
0x02812AA0: cmp      w9, #1
0x02812AA4: b.lt     #0x2812b30
0x02812AA8: sub      w9, w8, w9
0x02812AAC: cmp      w9, #1
0x02812AB0: b.lt     #0x2812b30
0x02812AB4: ldr      w10, [x19, #0x500]
0x02812AB8: cmp      w9, w10
0x02812ABC: b.ge     #0x2812b30
0x02812AC0: adrp     x9, #0x509c000
0x02812AC4: str      w8, [x19, #0x524]
0x02812AC8: ldr      x9, [x9, #0x70]
0x02812ACC: blr      x9
0x02812AD0: ldr      w3, [x20]
0x02812AD4: ldr      w4, [x19, #0x510]
0x02812AD8: adrp     x1, #0x1201000
0x02812ADC: adrp     x2, #0x11e6000
0x02812AE0: add      x1, x1, #0x89b
0x02812AE4: add      x2, x2, #0xf9d
0x02812AE8: bl       #0x2185854
0x02812AEC: b        #0x2812c74
0x02812AF0: adrp     x9, #0x509c000
0x02812AF4: str      w8, [x19, #0x510]
0x02812AF8: ldr      w8, [x20]
0x02812AFC: ldr      x9, [x9, #0x70]
0x02812B00: str      w8, [x19, #0x524]
0x02812B04: blr      x9
0x02812B08: ldr      w3, [x20]
0x02812B0C: ldr      w4, [x19, #0x508]
0x02812B10: adrp     x1, #0x1201000
0x02812B14: adrp     x2, #0x1160000
0x02812B18: add      x1, x1, #0x89b
0x02812B1C: add      x2, x2, #0xcab
0x02812B20: bl       #0x2185854
0x02812B24: mov      w20, wzr
0x02812B28: str      wzr, [x19, #0x508]
0x02812B2C: b        #0x2812c78
0x02812B30: adrp     x8, #0x509d000
0x02812B34: ldr      x8, [x8, #0x560]
0x02812B38: mov      w3, wzr
0x02812B3C: add      x9, sp, #0x48
0x02812B40: add      x10, sp, #0x838
0x02812B44: add      x11, sp, #0x440
0x02812B48: add      x4, sp, #0x50
0x02812B4C: add      x5, sp, #0x83c
0x02812B50: add      x6, sp, #0x4c
0x02812B54: mov      x0, x19
0x02812B58: mov      x1, x21
0x02812B5C: mov      x2, x20
0x02812B60: mov      w7, #1
0x02812B64: stp      x10, x9, [sp, #8]
0x02812B68: str      x11, [sp]
0x02812B6C: blr      x8
0x02812B70: ldrb     w8, [sp, #0x48]
0x02812B74: cbz      w8, #0x2812c30
0x02812B78: ldr      w8, [x20]
0x02812B7C: ldr      w9, [x19, #0x524]
0x02812B80: ldr      w10, [x19, #0x508]
0x02812B84: sub      w8, w8, w9
0x02812B88: add      w8, w8, w10
0x02812B8C: str      w8, [x19, #0x508]
0x02812B90: ldr      w8, [x20]
0x02812B94: str      w8, [x19, #0x524]
0x02812B98: ldr      w8, [sp, #0x838]
0x02812B9C: ldr      w9, [x20]
0x02812BA0: cmp      w8, #1
0x02812BA4: str      w9, [x19, #0x504]
0x02812BA8: b.lt     #0x2812ca4
0x02812BAC: ldp      w10, w12, [x21, #0x20]
0x02812BB0: ldr      w9, [sp, #0x460]
0x02812BB4: ldr      w13, [sp, #0x464]
0x02812BB8: ldr      w14, [x21, #0x28]
0x02812BBC: ldr      w15, [sp, #0x468]
0x02812BC0: sub      w9, w9, w10
0x02812BC4: ldr      w11, [x19, #0x514]
0x02812BC8: sub      w13, w13, w12
0x02812BCC: sub      w15, w15, w14
0x02812BD0: mul      w9, w9, w11
0x02812BD4: mul      w13, w13, w11
0x02812BD8: mul      w11, w15, w11
0x02812BDC: sdiv     w9, w9, w8
0x02812BE0: sub      w9, w10, w9
0x02812BE4: sdiv     w13, w13, w8
0x02812BE8: str      w9, [x19, #0x518]
0x02812BEC: sub      w10, w12, w13
0x02812BF0: sdiv     w8, w11, w8
0x02812BF4: str      w10, [x19, #0x51c]
0x02812BF8: sub      w8, w14, w8
0x02812BFC: str      w8, [x19, #0x520]
0x02812C00: b        #0x2812cd0
0x02812C04: ldr      x9, [x23, #0x70]
0x02812C08: str      w8, [x19, #0x524]
0x02812C0C: blr      x9
0x02812C10: ldr      w3, [x20]
0x02812C14: ldr      w4, [x19, #0x510]
0x02812C18: adrp     x1, #0x1201000
0x02812C1C: adrp     x2, #0x1199000
0x02812C20: add      x1, x1, #0x89b
0x02812C24: add      x2, x2, #0xda1
0x02812C28: bl       #0x2185854
0x02812C2C: b        #0x2812a84
0x02812C30: ldr      w8, [x19, #0x508]
0x02812C34: cmp      w8, #1
0x02812C38: b.lt     #0x2812c44
0x02812C3C: ldr      w8, [x20]
0x02812C40: str      w8, [x19, #0x50c]
0x02812C44: adrp     x8, #0x509c000
0x02812C48: ldr      w9, [x20]
0x02812C4C: str      wzr, [x19, #0x508]
0x02812C50: ldr      x8, [x8, #0x70]
0x02812C54: str      w9, [x19, #0x524]
0x02812C58: blr      x8
0x02812C5C: ldr      w3, [x20]
0x02812C60: adrp     x1, #0x1201000
0x02812C64: adrp     x2, #0x1153000
0x02812C68: add      x1, x1, #0x89b
0x02812C6C: add      x2, x2, #0x95e
0x02812C70: bl       #0x2185854
0x02812C74: mov      w20, wzr
0x02812C78: add      x0, sp, #0x50
0x02812C7C: bl       #0x4a4a07c
0x02812C80: add      x0, sp, #0x440
0x02812C84: bl       #0x4a4a07c
0x02812C88: mov      w0, w20
0x02812C8C: add      sp, sp, #0x830
0x02812C90: ldp      x20, x19, [sp, #0x30]
0x02812C94: ldp      x22, x21, [sp, #0x20]
0x02812C98: ldp      x30, x23, [sp, #0x10]
0x02812C9C: ldr      x29, [sp], #0x40
0x02812CA0: ret      
0x02812CA4: adrp     x8, #0x509d000
0x02812CA8: ldr      x8, [x8, #0x540]
0x02812CAC: add      x3, sp, #0x38
0x02812CB0: mov      x0, x19
0x02812CB4: mov      x1, x20
0x02812CB8: mov      w2, w22
0x02812CBC: blr      x8
0x02812CC0: ldr      x8, [sp, #0x38]
0x02812CC4: ldr      w9, [sp, #0x40]
0x02812CC8: str      x8, [x19, #0x518]
0x02812CCC: str      w9, [x19, #0x520]
0x02812CD0: adrp     x8, #0x509c000
0x02812CD4: ldr      x8, [x8, #0x70]
0x02812CD8: blr      x8
0x02812CDC: ldp      w9, w10, [x21, #0x20]
0x02812CE0: ldr      w3, [x20]
0x02812CE4: ldr      w4, [sp, #0x444]
0x02812CE8: ldr      w5, [sp, #0x460]
0x02812CEC: ldr      w6, [sp, #0x464]
0x02812CF0: ldr      w7, [sp, #0x468]
0x02812CF4: ldr      w8, [x21, #4]
0x02812CF8: ldr      w11, [x21, #0x28]
0x02812CFC: ldr      w12, [x19, #0x518]
0x02812D00: ldr      w13, [x19, #0x51c]
0x02812D04: ldr      w14, [x19, #0x520]
0x02812D08: adrp     x1, #0x1201000
0x02812D0C: adrp     x2, #0x11c0000
0x02812D10: add      x1, x1, #0x89b
0x02812D14: add      x2, x2, #0x46c
0x02812D18: str      w14, [sp, #0x30]
0x02812D1C: str      w13, [sp, #0x28]
~~~

### Function start 0x2812d6c
Hits: [{"pc": "0x281315c", "adrp": "0x2813154", "target": "0x114d690", "label": "CurFrame[%d] Enter Danger Because In HeroDanger, EnemyPos[%d;%d:%d:%d] MainHeroPos[%d;%d:%d:%d] MovePos[%d:%d:%d]\n", "keywords": ["EnemyPos", "MainHeroPos"], "fde_start": "0x2812d6c", "fde_end": "0x28131b4", "kind": "add", "reg": "x2"}]
~~~asm
0x02812D6C: str      x29, [sp, #-0x40]!
0x02812D70: stp      x30, x23, [sp, #0x10]
0x02812D74: stp      x22, x21, [sp, #0x20]
0x02812D78: stp      x20, x19, [sp, #0x30]
0x02812D7C: sub      sp, sp, #0x830
0x02812D80: mov      x19, x0
0x02812D84: add      x0, sp, #0x440
0x02812D88: mov      x20, x2
0x02812D8C: mov      x21, x1
0x02812D90: str      xzr, [sp, #0x838]
0x02812D94: bl       #0x4a49db4
0x02812D98: add      x0, sp, #0x50
0x02812D9C: bl       #0x4a49db4
0x02812DA0: ldr      w8, [x20]
0x02812DA4: strb     wzr, [sp, #0x4c]
0x02812DA8: ldr      w9, [x19, #0x4f0]
0x02812DAC: strb     wzr, [sp, #0x48]
0x02812DB0: ldr      w22, [x21, #0x18]
0x02812DB4: sub      w12, w8, w9
0x02812DB8: cmp      w12, #2
0x02812DBC: b.lt     #0x2812e28
0x02812DC0: ldr      w11, [x19, #0x4d8]
0x02812DC4: cmp      w11, #1
0x02812DC8: b.lt     #0x2812e28
0x02812DCC: ldr      w10, [x19, #0x4b4]
0x02812DD0: add      w12, w11, w12
0x02812DD4: cmp      w12, w10
0x02812DD8: b.le     #0x2812e28
0x02812DDC: sub      w8, w9, w11
0x02812DE0: adrp     x23, #0x509c000
0x02812DE4: add      w8, w8, w10
0x02812DE8: str      wzr, [x19, #0x4d8]
0x02812DEC: add      w8, w8, #1
0x02812DF0: ldr      x9, [x23, #0x70]
0x02812DF4: str      w8, [x19, #0x4e0]
0x02812DF8: blr      x9
0x02812DFC: ldr      w3, [x20]
0x02812E00: ldr      w4, [x19, #0x4e0]
0x02812E04: adrp     x1, #0x1201000
0x02812E08: adrp     x2, #0x11f4000
0x02812E0C: add      x1, x1, #0x89b
0x02812E10: add      x2, x2, #0xe69
0x02812E14: bl       #0x2185854
0x02812E18: ldr      w9, [x19, #0x4e0]
0x02812E1C: ldr      w8, [x20]
0x02812E20: cmp      w9, w8
0x02812E24: b.ge     #0x2812fa0
0x02812E28: ldr      w9, [x19, #0x4d4]
0x02812E2C: tbnz     w9, #0x1f, #0x2812ea8
0x02812E30: sub      w9, w8, w9
0x02812E34: cmp      w9, #1
0x02812E38: b.lt     #0x2812ea8
0x02812E3C: ldr      w10, [x19, #0x4b0]
0x02812E40: cmp      w9, w10
0x02812E44: b.ge     #0x2812ea8
0x02812E48: ldr      w9, [x19, #0x4f0]
0x02812E4C: ldr      w10, [x19, #0x4d8]
0x02812E50: sub      w8, w8, w9
0x02812E54: adrp     x9, #0x509c000
0x02812E58: add      w8, w8, w10
0x02812E5C: ldr      x9, [x9, #0x70]
0x02812E60: str      w8, [x19, #0x4d8]
0x02812E64: ldr      w8, [x20]
0x02812E68: str      w8, [x19, #0x4f0]
0x02812E6C: blr      x9
0x02812E70: ldr      w3, [x20]
0x02812E74: ldr      w4, [x19, #0x4d4]
0x02812E78: ldr      w5, [x19, #0x4d8]
0x02812E7C: ldr      w6, [x19, #0x4e4]
0x02812E80: ldr      w7, [x19, #0x4e8]
0x02812E84: ldr      w8, [x19, #0x4ec]
0x02812E88: adrp     x1, #0x1201000
0x02812E8C: adrp     x2, #0x11da000
0x02812E90: add      x1, x1, #0x89b
0x02812E94: add      x2, x2, #0x2d9
0x02812E98: str      w8, [sp]
0x02812E9C: bl       #0x2185854
0x02812EA0: mov      w20, #1
0x02812EA4: b        #0x2812f74
0x02812EA8: ldr      w9, [x19, #0x4d8]
0x02812EAC: ldr      w10, [x19, #0x4b4]
0x02812EB0: cmp      w9, w10
0x02812EB4: b.ge     #0x2812f38
0x02812EB8: ldr      w10, [x19, #0x4e0]
0x02812EBC: ldr      w9, [x19, #0x4dc]
0x02812EC0: cmp      w10, #1
0x02812EC4: b.lt     #0x2812ee0
0x02812EC8: sub      w10, w8, w10
0x02812ECC: cmp      w10, #1
0x02812ED0: b.lt     #0x2812ee0
0x02812ED4: ldr      w11, [x19, #0x4bc]
0x02812ED8: cmp      w10, w11
0x02812EDC: b.lt     #0x2812f00
0x02812EE0: cmp      w9, #1
0x02812EE4: b.lt     #0x2812fcc
0x02812EE8: sub      w9, w8, w9
0x02812EEC: cmp      w9, #1
0x02812EF0: b.lt     #0x2812fcc
0x02812EF4: ldr      w10, [x19, #0x4b8]
0x02812EF8: cmp      w9, w10
0x02812EFC: b.ge     #0x2812fcc
0x02812F00: adrp     x9, #0x509c000
0x02812F04: str      w8, [x19, #0x4f0]
0x02812F08: ldr      x9, [x9, #0x70]
0x02812F0C: blr      x9
0x02812F10: ldr      w3, [x20]
0x02812F14: ldr      w4, [x19, #0x4e0]
0x02812F18: ldr      w5, [x19, #0x4dc]
0x02812F1C: adrp     x1, #0x1201000
0x02812F20: adrp     x2, #0x11c0000
0x02812F24: add      x1, x1, #0x89b
0x02812F28: add      x2, x2, #0x4dd
0x02812F2C: bl       #0x2185854
0x02812F30: mov      w20, wzr
0x02812F34: b        #0x2812f74
0x02812F38: adrp     x9, #0x509c000
0x02812F3C: str      w8, [x19, #0x4e0]
0x02812F40: ldr      w8, [x20]
0x02812F44: ldr      x9, [x9, #0x70]
0x02812F48: str      w8, [x19, #0x4f0]
0x02812F4C: blr      x9
0x02812F50: ldr      w3, [x20]
0x02812F54: ldr      w4, [x19, #0x4d8]
0x02812F58: adrp     x1, #0x1201000
0x02812F5C: adrp     x2, #0x11a7000
0x02812F60: add      x1, x1, #0x89b
0x02812F64: add      x2, x2, #0x8bc
0x02812F68: bl       #0x2185854
0x02812F6C: mov      w20, wzr
0x02812F70: str      wzr, [x19, #0x4d8]
0x02812F74: add      x0, sp, #0x50
0x02812F78: bl       #0x4a4a07c
0x02812F7C: add      x0, sp, #0x440
0x02812F80: bl       #0x4a4a07c
0x02812F84: mov      w0, w20
0x02812F88: add      sp, sp, #0x830
0x02812F8C: ldp      x20, x19, [sp, #0x30]
0x02812F90: ldp      x22, x21, [sp, #0x20]
0x02812F94: ldp      x30, x23, [sp, #0x10]
0x02812F98: ldr      x29, [sp], #0x40
0x02812F9C: ret      
0x02812FA0: ldr      x9, [x23, #0x70]
0x02812FA4: str      w8, [x19, #0x4f0]
0x02812FA8: blr      x9
0x02812FAC: ldr      w3, [x20]
0x02812FB0: ldr      w4, [x19, #0x4e0]
0x02812FB4: adrp     x1, #0x1201000
0x02812FB8: adrp     x2, #0x11a0000
0x02812FBC: add      x1, x1, #0x89b
0x02812FC0: add      x2, x2, #0x3ca
0x02812FC4: bl       #0x2185854
0x02812FC8: b        #0x2812ea0
0x02812FCC: adrp     x8, #0x509d000
0x02812FD0: ldr      x8, [x8, #0x560]
0x02812FD4: mov      w7, wzr
0x02812FD8: add      x9, sp, #0x48
0x02812FDC: add      x10, sp, #0x838
0x02812FE0: add      x11, sp, #0x50
0x02812FE4: add      x4, sp, #0x440
0x02812FE8: add      x5, sp, #0x83c
0x02812FEC: add      x6, sp, #0x4c
0x02812FF0: mov      x0, x19
0x02812FF4: mov      x1, x21
0x02812FF8: mov      x2, x20
0x02812FFC: mov      w3, #1
0x02813000: stp      x10, x9, [sp, #8]
0x02813004: str      x11, [sp]
0x02813008: blr      x8
0x0281300C: ldrb     w8, [sp, #0x4c]
0x02813010: cbz      w8, #0x28130a0
0x02813014: ldr      w8, [x20]
0x02813018: ldr      w9, [x19, #0x4f0]
0x0281301C: ldr      w10, [x19, #0x4d8]
0x02813020: sub      w8, w8, w9
0x02813024: add      w8, w8, w10
0x02813028: str      w8, [x19, #0x4d8]
0x0281302C: ldr      w8, [x20]
0x02813030: str      w8, [x19, #0x4f0]
0x02813034: ldr      w8, [sp, #0x83c]
0x02813038: ldr      w9, [x20]
0x0281303C: cmp      w8, #1
0x02813040: str      w9, [x19, #0x4d4]
0x02813044: b.lt     #0x28130e8
0x02813048: ldp      w10, w12, [x21, #0x20]
0x0281304C: ldr      w9, [sp, #0x460]
0x02813050: ldr      w13, [sp, #0x464]
0x02813054: ldr      w14, [x21, #0x28]
0x02813058: ldr      w15, [sp, #0x468]
0x0281305C: sub      w9, w9, w10
0x02813060: ldr      w11, [x19, #0x4d0]
0x02813064: sub      w13, w13, w12
0x02813068: sub      w15, w15, w14
0x0281306C: mul      w9, w9, w11
0x02813070: mul      w13, w13, w11
0x02813074: mul      w11, w15, w11
0x02813078: sdiv     w9, w9, w8
0x0281307C: sub      w9, w10, w9
0x02813080: sdiv     w13, w13, w8
0x02813084: str      w9, [x19, #0x4e4]
0x02813088: sub      w10, w12, w13
0x0281308C: sdiv     w8, w11, w8
0x02813090: str      w10, [x19, #0x4e8]
0x02813094: sub      w8, w14, w8
0x02813098: str      w8, [x19, #0x4ec]
0x0281309C: b        #0x2813118
0x028130A0: ldr      w8, [x19, #0x4d8]
0x028130A4: cmp      w8, #1
0x028130A8: b.lt     #0x28130b4
0x028130AC: ldr      w8, [x20]
0x028130B0: str      w8, [x19, #0x4dc]
0x028130B4: adrp     x8, #0x509c000
0x028130B8: ldr      w9, [x20]
0x028130BC: str      wzr, [x19, #0x4d8]
0x028130C0: ldr      x8, [x8, #0x70]
0x028130C4: str      w9, [x19, #0x4f0]
0x028130C8: blr      x8
0x028130CC: ldr      w3, [x20]
0x028130D0: adrp     x1, #0x1201000
0x028130D4: adrp     x2, #0x11ad000
0x028130D8: add      x1, x1, #0x89b
0x028130DC: add      x2, x2, #0x9cd
0x028130E0: bl       #0x2185854
0x028130E4: b        #0x2812f30
0x028130E8: adrp     x8, #0x509d000
0x028130EC: ldr      x8, [x8, #0x540]
0x028130F0: add      x3, sp, #0x38
0x028130F4: mov      x0, x19
0x028130F8: mov      x1, x20
0x028130FC: mov      w2, w22
0x02813100: blr      x8
0x02813104: add      x8, x19, #0x4e4
0x02813108: ldr      x9, [sp, #0x38]
0x0281310C: ldr      w10, [sp, #0x40]
0x02813110: str      x9, [x8]
0x02813114: str      w10, [x8, #8]
0x02813118: adrp     x8, #0x509c000
0x0281311C: ldr      x8, [x8, #0x70]
0x02813120: blr      x8
0x02813124: ldp      w9, w10, [x21, #0x20]
0x02813128: ldr      w3, [x20]
~~~

### Function start 0x2827bec
Hits: [{"pc": "0x2827c74", "adrp": "0x2827c68", "target": "0x11872a5", "label": "Ignore, yAction:%d not kMoveDir", "keywords": ["MoveDir"], "fde_start": "0x2827bec", "fde_end": "0x2827d70", "kind": "add", "reg": "x2"}]
~~~asm
0x02827BEC: str      x30, [sp, #-0x40]!
0x02827BF0: stp      x24, x23, [sp, #0x10]
0x02827BF4: stp      x22, x21, [sp, #0x20]
0x02827BF8: stp      x20, x19, [sp, #0x30]
0x02827BFC: ldr      w8, [x2, #0x150]
0x02827C00: mov      x19, x2
0x02827C04: cmp      w8, #0xf
0x02827C08: b.ne     #0x2827c58
0x02827C0C: ldrsw    x22, [x1, #0x10]
0x02827C10: mov      w8, #0x3f0
0x02827C14: ldr      x23, [x1, #0x68]
0x02827C18: mov      x20, x1
0x02827C1C: ldr      w9, [x0, #0x5f8]
0x02827C20: mov      x21, x0
0x02827C24: madd     x24, x22, x8, x23
0x02827C28: ldr      w8, [x24, #0x50]!
0x02827C2C: cmp      w8, w9
0x02827C30: b.le     #0x2827c94
0x02827C34: adrp     x8, #0x509c000
0x02827C38: ldr      x8, [x8, #0x70]
0x02827C3C: blr      x8
0x02827C40: ldr      w3, [x24]
0x02827C44: adrp     x1, #0x11a7000
0x02827C48: adrp     x2, #0x11fb000
0x02827C4C: add      x1, x1, #0x9ee
0x02827C50: add      x2, x2, #0x697
0x02827C54: b        #0x2827c78
0x02827C58: adrp     x8, #0x509c000
0x02827C5C: ldr      x8, [x8, #0x70]
0x02827C60: blr      x8
0x02827C64: adrp     x1, #0x11a7000
0x02827C68: adrp     x2, #0x1187000
0x02827C6C: ldr      w3, [x19, #0x150]
0x02827C70: add      x1, x1, #0x9ee
0x02827C74: add      x2, x2, #0x2a5
0x02827C78: bl       #0x2185854
0x02827C7C: mov      w0, wzr
0x02827C80: ldp      x20, x19, [sp, #0x30]
0x02827C84: ldp      x22, x21, [sp, #0x20]
0x02827C88: ldp      x24, x23, [sp, #0x10]
0x02827C8C: ldr      x30, [sp], #0x40
0x02827C90: ret      
0x02827C94: ldr      w8, [x21, #0x4c4]
0x02827C98: cbz      w8, #0x2827d2c
0x02827C9C: adrp     x8, #0x5089000
0x02827CA0: add      x1, x21, #0x4c4
0x02827CA4: add      x0, x21, #0x4a8
0x02827CA8: ldr      x8, [x8, #0x210]
0x02827CAC: blr      x8
0x02827CB0: add      x8, x21, #0x4b0
0x02827CB4: cmp      x8, x0
0x02827CB8: b.eq     #0x2827d4c
0x02827CBC: ldr      w8, [x21, #0x60c]
0x02827CC0: cmp      w8, #1
0x02827CC4: b.lt     #0x2827d24
0x02827CC8: mov      w8, #0x3f0
0x02827CCC: ldr      w9, [x21, #0x578]
0x02827CD0: nop      
0x02827CD4: madd     x8, x22, x8, x23
0x02827CD8: ldr      w8, [x8, #0x54]
0x02827CDC: cmp      w9, w8
0x02827CE0: b.ge     #0x2827d24
0x02827CE4: adrp     x8, #0x509d000
0x02827CE8: ldr      w3, [x21, #0x4c4]
0x02827CEC: mov      x0, x21
0x02827CF0: mov      x1, x20
0x02827CF4: mov      x2, x19
0x02827CF8: ldr      x8, [x8, #0xc60]
0x02827CFC: blr      x8
0x02827D00: tbz      w0, #0, #0x2827d24
0x02827D04: adrp     x8, #0x509c000
0x02827D08: ldr      x8, [x8, #0x70]
0x02827D0C: blr      x8
0x02827D10: adrp     x1, #0x11a7000
0x02827D14: adrp     x2, #0x11b4000
0x02827D18: add      x1, x1, #0x9ee
0x02827D1C: add      x2, x2, #0x299
0x02827D20: bl       #0x2185854
0x02827D24: mov      w0, #1
0x02827D28: b        #0x2827c80
0x02827D2C: adrp     x8, #0x509c000
0x02827D30: ldr      x8, [x8, #0x70]
0x02827D34: blr      x8
0x02827D38: adrp     x1, #0x11a7000
0x02827D3C: adrp     x2, #0x1199000
0x02827D40: add      x1, x1, #0x9ee
0x02827D44: add      x2, x2, #0xa98
0x02827D48: b        #0x2827d68
0x02827D4C: adrp     x8, #0x509c000
0x02827D50: ldr      x8, [x8, #0x70]
0x02827D54: blr      x8
0x02827D58: adrp     x1, #0x11a7000
0x02827D5C: adrp     x2, #0x1173000
0x02827D60: add      x1, x1, #0x9ee
0x02827D64: add      x2, x2, #0xc13
0x02827D68: bl       #0x2185854
0x02827D6C: b        #0x2827c7c
~~~

### Function start 0x282cf0c
Hits: [{"pc": "0x282cf8c", "adrp": "0x282cf84", "target": "0x12084ba", "label": "OptimizeMoveDir", "keywords": ["MoveDir"], "fde_start": "0x282cf0c", "fde_end": "0x282d018", "kind": "add", "reg": "x2"}]
~~~asm
0x0282CF0C: str      x30, [sp, #-0x30]!
0x0282CF10: stp      x22, x21, [sp, #0x10]
0x0282CF14: stp      x20, x19, [sp, #0x20]
0x0282CF18: adrp     x22, #0x509c000
0x0282CF1C: mov      x19, x2
0x0282CF20: mov      x20, x1
0x0282CF24: mov      x21, x0
0x0282CF28: ldr      x8, [x22, #0x70]
0x0282CF2C: blr      x8
0x0282CF30: adrp     x1, #0x1187000
0x0282CF34: adrp     x2, #0x1207000
0x0282CF38: ldr      w3, [x19, #0x150]
0x0282CF3C: add      x1, x1, #0x2fe
0x0282CF40: add      x2, x2, #0xe38
0x0282CF44: bl       #0x2185854
0x0282CF48: ldrsw    x8, [x20, #0x10]
0x0282CF4C: mov      w10, #0x3f0
0x0282CF50: ldr      x9, [x20, #0x68]
0x0282CF54: adrp     x11, #0x509d000
0x0282CF58: mov      x0, x21
0x0282CF5C: mov      x1, x20
0x0282CF60: mov      x2, x19
0x0282CF64: madd     x8, x8, x10, x9
0x0282CF68: ldr      x9, [x11, #0xee0]
0x0282CF6C: str      x8, [x21, #0x4a8]
0x0282CF70: blr      x9
0x0282CF74: tbz      w0, #0, #0x282cf94
0x0282CF78: ldr      x8, [x22, #0x70]
0x0282CF7C: blr      x8
0x0282CF80: adrp     x1, #0x1187000
0x0282CF84: adrp     x2, #0x1208000
0x0282CF88: add      x1, x1, #0x2fe
0x0282CF8C: add      x2, x2, #0x4ba
0x0282CF90: bl       #0x2185854
0x0282CF94: adrp     x8, #0x509d000
0x0282CF98: mov      x0, x21
0x0282CF9C: mov      x1, x20
0x0282CFA0: mov      x2, x19
0x0282CFA4: ldr      x8, [x8, #0xef0]
0x0282CFA8: blr      x8
0x0282CFAC: tbz      w0, #0, #0x282cfcc
0x0282CFB0: ldr      x8, [x22, #0x70]
0x0282CFB4: blr      x8
0x0282CFB8: adrp     x1, #0x1187000
0x0282CFBC: adrp     x2, #0x11c6000
0x0282CFC0: add      x1, x1, #0x2fe
0x0282CFC4: add      x2, x2, #0xb56
0x0282CFC8: bl       #0x2185854
0x0282CFCC: adrp     x8, #0x509d000
0x0282CFD0: mov      x0, x21
0x0282CFD4: mov      x1, x20
0x0282CFD8: mov      x2, x19
0x0282CFDC: ldr      x8, [x8, #0xf00]
0x0282CFE0: blr      x8
0x0282CFE4: tbz      w0, #0, #0x282d004
0x0282CFE8: ldr      x8, [x22, #0x70]
0x0282CFEC: blr      x8
0x0282CFF0: adrp     x1, #0x1187000
0x0282CFF4: adrp     x2, #0x11da000
0x0282CFF8: add      x1, x1, #0x2fe
0x0282CFFC: add      x2, x2, #0x4fb
0x0282D000: bl       #0x2185854
0x0282D004: ldp      x20, x19, [sp, #0x20]
0x0282D008: mov      w0, #1
0x0282D00C: ldp      x22, x21, [sp, #0x10]
0x0282D010: ldr      x30, [sp], #0x30
0x0282D014: ret      
~~~

### Function start 0x282d06c
Hits: [{"pc": "0x282d1c0", "adrp": "0x282d1b8", "target": "0x114672f", "label": "GuanyuActionOpt::OptimizeMoveDir", "keywords": ["MoveDir"], "fde_start": "0x282d06c", "fde_end": "0x282d360", "kind": "add", "reg": "x1"}, {"pc": "0x282d27c", "adrp": "0x282d274", "target": "0x114672f", "label": "GuanyuActionOpt::OptimizeMoveDir", "keywords": ["MoveDir"], "fde_start": "0x282d06c", "fde_end": "0x282d360", "kind": "add", "reg": "x1"}, {"pc": "0x282d2dc", "adrp": "0x282d2d4", "target": "0x114672f", "label": "GuanyuActionOpt::OptimizeMoveDir", "keywords": ["MoveDir"], "fde_start": "0x282d06c", "fde_end": "0x282d360", "kind": "add", "reg": "x1"}, {"pc": "0x282d304", "adrp": "0x282d2fc", "target": "0x114672f", "label": "GuanyuActionOpt::OptimizeMoveDir", "keywords": ["MoveDir"], "fde_start": "0x282d06c", "fde_end": "0x282d360", "kind": "add", "reg": "x1"}]
~~~asm
0x0282D06C: sub      sp, sp, #0x130
0x0282D070: stp      x29, x30, [sp, #0xd0]
0x0282D074: stp      x28, x27, [sp, #0xe0]
0x0282D078: stp      x26, x25, [sp, #0xf0]
0x0282D07C: stp      x24, x23, [sp, #0x100]
0x0282D080: stp      x22, x21, [sp, #0x110]
0x0282D084: stp      x20, x19, [sp, #0x120]
0x0282D088: mov      x20, x0
0x0282D08C: add      x0, sp, #0x20
0x0282D090: str      x2, [sp, #0x10]
0x0282D094: mov      x22, x1
0x0282D098: add      x29, sp, #0x20
0x0282D09C: bl       #0x4a49794
0x0282D0A0: ldp      x19, x8, [x22, #0x80]
0x0282D0A4: add      x21, x20, #0x4b0
0x0282D0A8: cmp      x19, x8
0x0282D0AC: b.eq     #0x282d1a0
0x0282D0B0: mov      w28, wzr
0x0282D0B4: add      x8, x29, #0x40
0x0282D0B8: add      x24, x29, #0x58
0x0282D0BC: add      x25, x29, #0x78
0x0282D0C0: add      x26, x29, #0x90
0x0282D0C4: adrp     x23, #0x517f000
0x0282D0C8: str      x8, [sp, #0x18]
0x0282D0CC: b        #0x282d0ec
0x0282D0D0: ldr      w8, [x19, #0xa8]
0x0282D0D4: mov      w28, w27
0x0282D0D8: str      w8, [sp, #0xc8]
0x0282D0DC: ldr      x8, [x22, #0x88]
0x0282D0E0: add      x19, x19, #0xb0
0x0282D0E4: cmp      x19, x8
0x0282D0E8: b.eq     #0x282d1a4
0x0282D0EC: ldr      w8, [x19, #0x1c]
0x0282D0F0: cmp      w8, #1
0x0282D0F4: b.lt     #0x282d0dc
0x0282D0F8: ldr      x8, [x20, #0x4a8]
0x0282D0FC: ldr      w9, [x19, #0xc]
0x0282D100: ldr      w10, [x8, #0x18]
0x0282D104: cmp      w9, w10
0x0282D108: b.eq     #0x282d0dc
0x0282D10C: add      x1, x19, #0x10
0x0282D110: add      x2, x8, #0x20
0x0282D114: ldr      x8, [x23, #0x388]
0x0282D118: mov      x0, x21
0x0282D11C: mov      w3, #1
0x0282D120: blr      x8
0x0282D124: mov      w27, w0
0x0282D128: cbz      w28, #0x282d134
0x0282D12C: cmp      w27, w28
0x0282D130: b.ge     #0x282d0dc
0x0282D134: ldp      q1, q0, [x19, #0x20]
0x0282D138: cmp      x19, x29
0x0282D13C: ldp      q3, q2, [x19]
0x0282D140: stp      q1, q0, [sp, #0x40]
0x0282D144: stp      q3, q2, [sp, #0x20]
0x0282D148: b.eq     #0x282d0d0
0x0282D14C: adrp     x8, #0x5252000
0x0282D150: ldp      x1, x2, [x19, #0x40]
0x0282D154: ldr      x8, [x8, #0xbe8]
0x0282D158: ldr      x0, [sp, #0x18]
0x0282D15C: blr      x8
0x0282D160: add      x1, x19, #0x58
0x0282D164: mov      x0, x24
0x0282D168: bl       #0x225fbd8
0x0282D16C: ldr      w8, [x19, #0x70]
0x0282D170: str      w8, [sp, #0x90]
0x0282D174: adrp     x8, #0x5253000
0x0282D178: ldp      x1, x2, [x19, #0x78]
0x0282D17C: ldr      x8, [x8, #0x38]
0x0282D180: mov      x0, x25
0x0282D184: blr      x8
0x0282D188: adrp     x8, #0x5253000
0x0282D18C: ldp      x1, x2, [x19, #0x90]
0x0282D190: ldr      x8, [x8, #0xc8]
0x0282D194: mov      x0, x26
0x0282D198: blr      x8
0x0282D19C: b        #0x282d0d0
0x0282D1A0: mov      w28, wzr
0x0282D1A4: adrp     x23, #0x509c000
0x0282D1A8: ldr      x8, [x23, #0x70]
0x0282D1AC: blr      x8
0x0282D1B0: ldr      x8, [x20, #0x4a8]
0x0282D1B4: ldr      w3, [x8, #0x160]
0x0282D1B8: adrp     x1, #0x1146000
0x0282D1BC: adrp     x2, #0x1208000
0x0282D1C0: add      x1, x1, #0x72f
0x0282D1C4: add      x2, x2, #0x4ca
0x0282D1C8: bl       #0x2185854
0x0282D1CC: adrp     x8, #0x517f000
0x0282D1D0: ldr      x8, [x8, #0x2d8]
0x0282D1D4: mov      x0, x21
0x0282D1D8: mov      x1, x22
0x0282D1DC: mov      w2, #1
0x0282D1E0: mov      w3, #2
0x0282D1E4: mov      w4, #0x64
0x0282D1E8: mov      w5, #1
0x0282D1EC: blr      x8
0x0282D1F0: lsr      x8, x0, #0x20
0x0282D1F4: add      x9, x20, #0x4c4
0x0282D1F8: ldrb     w10, [x20, #0x4cc]
0x0282D1FC: str      w0, [x20, #0x4bc]
0x0282D200: ldr      x19, [sp, #0x10]
0x0282D204: str      w8, [x20, #0x4c0]
0x0282D208: str      x1, [x9]
0x0282D20C: cbz      w10, #0x282d2ec
0x0282D210: ldr      w8, [x19, #0x150]
0x0282D214: cmp      w8, #0xf
0x0282D218: b.ne     #0x282d2ec
0x0282D21C: ldr      x8, [x20, #0x4a8]
0x0282D220: ldp      x9, x10, [x8, #0x1c0]
0x0282D224: cmp      x10, x9
0x0282D228: b.eq     #0x282d2ec
0x0282D22C: ldrb     w9, [x9, #8]
0x0282D230: cbz      w9, #0x282d2ec
0x0282D234: ldp      w10, w9, [x8, #0x7c]
0x0282D238: cmp      w9, w10
0x0282D23C: b.ne     #0x282d2ec
0x0282D240: cbz      w28, #0x282d258
0x0282D244: adrp     x9, #0x542b000
0x0282D248: sub      w10, w28, #0x14
0x0282D24C: ldr      w9, [x9, #0x404]
0x0282D250: cmp      w10, w9
0x0282D254: b.gt     #0x282d268
0x0282D258: ldr      w9, [sp, #0x54]
0x0282D25C: ldr      w8, [x8, #8]
0x0282D260: cmp      w9, w8
0x0282D264: b.ne     #0x282d2ec
0x0282D268: ldr      x8, [x23, #0x70]
0x0282D26C: blr      x8
0x0282D270: ldr      w3, [x19, #0x150]
0x0282D274: adrp     x1, #0x1146000
0x0282D278: adrp     x2, #0x11ba000
0x0282D27C: add      x1, x1, #0x72f
0x0282D280: add      x2, x2, #0x287
0x0282D284: bl       #0x2185854
0x0282D288: ldr      w8, [x20, #0x4bc]
0x0282D28C: cbz      w8, #0x282d310
0x0282D290: mov      w8, #0xf
0x0282D294: adrp     x9, #0x517f000
0x0282D298: add      x2, x20, #0x4c0
0x0282D29C: str      w8, [x19, #0x150]
0x0282D2A0: ldr      x8, [x20, #0x4a8]
0x0282D2A4: add      x1, x8, #0x20
0x0282D2A8: ldr      x8, [x9, #0x308]
0x0282D2AC: mov      x0, x21
0x0282D2B0: blr      x8
0x0282D2B4: ldr      x8, [x23, #0x70]
0x0282D2B8: str      x0, [x19, #0x158]
0x0282D2BC: str      w1, [x19, #0x160]
0x0282D2C0: blr      x8
0x0282D2C4: ldr      w3, [x20, #0x4bc]
0x0282D2C8: ldr      w4, [x19, #0x158]
0x0282D2CC: ldr      w5, [x19, #0x15c]
0x0282D2D0: ldr      w6, [x19, #0x160]
0x0282D2D4: adrp     x1, #0x1146000
0x0282D2D8: adrp     x2, #0x1187000
0x0282D2DC: add      x1, x1, #0x72f
0x0282D2E0: add      x2, x2, #0x317
0x0282D2E4: bl       #0x2185854
0x0282D2E8: b        #0x282d310
0x0282D2EC: ldr      x8, [x23, #0x70]
0x0282D2F0: blr      x8
0x0282D2F4: ldrb     w3, [x20, #0x4cc]
0x0282D2F8: ldr      w4, [x19, #0x150]
0x0282D2FC: adrp     x1, #0x1146000
0x0282D300: adrp     x2, #0x11cc000
0x0282D304: add      x1, x1, #0x72f
0x0282D308: add      x2, x2, #0xf13
0x0282D30C: bl       #0x2185854
0x0282D310: add      x0, sp, #0x20
0x0282D314: bl       #0x4a49878
0x0282D318: ldp      x20, x19, [sp, #0x120]
0x0282D31C: mov      w0, #1
0x0282D320: ldp      x22, x21, [sp, #0x110]
0x0282D324: ldp      x24, x23, [sp, #0x100]
0x0282D328: ldp      x26, x25, [sp, #0xf0]
0x0282D32C: ldp      x28, x27, [sp, #0xe0]
0x0282D330: ldp      x29, x30, [sp, #0xd0]
0x0282D334: add      sp, sp, #0x130
0x0282D338: ret      
0x0282D33C: b        #0x282d34c
0x0282D340: b        #0x282d34c
0x0282D344: b        #0x282d34c
0x0282D348: b        #0x282d34c
0x0282D34C: mov      x19, x0
0x0282D350: add      x0, sp, #0x20
0x0282D354: bl       #0x4a49878
0x0282D358: mov      x0, x19
0x0282D35C: bl       #0x2231bf0
~~~

### Function start 0x2832508
Hits: [{"pc": "0x2832c34", "adrp": "0x2832c2c", "target": "0x117417f", "label": "no_shoot_invisible_frame_gap", "keywords": ["invisible"], "fde_start": "0x2832508", "fde_end": "0x2832f68", "kind": "add", "reg": "x1"}]
~~~asm
0x02832508: sub      sp, sp, #0x70
0x0283250C: str      x30, [sp, #0x40]
0x02832510: stp      x22, x21, [sp, #0x50]
0x02832514: stp      x20, x19, [sp, #0x60]
0x02832518: adrp     x8, #0x509c000
0x0283251C: mov      x19, x0
0x02832520: add      x0, x0, #0x88
0x02832524: mov      x20, x1
0x02832528: ldr      x8, [x8, #0x380]
0x0283252C: blr      x8
0x02832530: tbz      w0, #0, #0x2832e8c
0x02832534: adrp     x8, #0x508c000
0x02832538: ldr      x8, [x8, #0x6c8]
0x0283253C: blr      x8
0x02832540: mov      x21, x0
0x02832544: mov      w0, #0x40
0x02832548: bl       #0x4b40050
0x0283254C: adrp     x9, #0x1180000
0x02832550: adrp     x8, #0x113c000
0x02832554: add      x9, x9, #0x31e
0x02832558: adrp     x10, #0x508c000
0x0283255C: str      x0, [sp, #0x30]
0x02832560: ldr      q2, [x8, #0xfd0]
0x02832564: mov      w8, #0x742e
0x02832568: ldp      q0, q1, [x9]
0x0283256C: movk     w8, #0x7478, lsl #16
0x02832570: strb     wzr, [x0, #0x33]
0x02832574: str      q2, [sp, #0x20]
0x02832578: stur     w8, [x0, #0x2f]
0x0283257C: stp      q0, q1, [x0]
0x02832580: ldr      q0, [x9, #0x20]
0x02832584: ldr      x8, [x10, #0x6d0]
0x02832588: str      q0, [x0, #0x20]
0x0283258C: add      x1, sp, #0x20
0x02832590: mov      x0, x21
0x02832594: blr      x8
0x02832598: mov      w21, w0
0x0283259C: ldrb     w8, [sp, #0x20]
0x028325A0: tbz      w8, #0, #0x28325ac
0x028325A4: ldr      x0, [sp, #0x30]
0x028325A8: bl       #0x4b3fb60
0x028325AC: tbz      w21, #0, #0x2832ec0
0x028325B0: adrp     x8, #0x509d000
0x028325B4: mov      x0, x19
0x028325B8: mov      x1, x20
0x028325BC: ldr      x8, [x8, #0x70]
0x028325C0: blr      x8
0x028325C4: tbz      w0, #0, #0x2832ef8
0x028325C8: adrp     x9, #0x5179000
0x028325CC: add      x8, sp, #0x20
0x028325D0: add      x21, x8, #8
0x028325D4: mov      w8, #0x3d02
0x028325D8: add      x0, x19, #0x78
0x028325DC: stp      xzr, xzr, [sp, #0x28]
0x028325E0: ldr      x9, [x9, #0xb20]
0x028325E4: strb     wzr, [sp, #0xa]
0x028325E8: str      x21, [sp, #0x20]
0x028325EC: strh     w8, [sp, #8]
0x028325F0: add      x2, sp, #8
0x028325F4: add      x3, sp, #0x20
0x028325F8: mov      x1, x20
0x028325FC: blr      x9
0x02832600: ldrb     w8, [sp, #8]
0x02832604: tbz      w8, #0, #0x2832610
0x02832608: ldr      x0, [sp, #0x18]
0x0283260C: bl       #0x4b3fb60
0x02832610: adrp     x10, #0x11ed000
0x02832614: mov      w9, #0x6e61
0x02832618: add      x10, x10, #0xf93
0x0283261C: mov      w8, #0x26
0x02832620: movk     w9, #0x6567, lsl #16
0x02832624: add      x0, sp, #0x20
0x02832628: add      x1, sp, #8
0x0283262C: strb     wzr, [sp, #0x1c]
0x02832630: ldr      q0, [x10]
0x02832634: strb     w8, [sp, #8]
0x02832638: str      w9, [sp, #0x18]
0x0283263C: stur     q0, [sp, #9]
0x02832640: bl       #0x227e510
0x02832644: cmp      x21, x0
0x02832648: b.eq     #0x2832668
0x0283264C: ldrb     w8, [x0, #0x38]
0x02832650: add      x10, x0, #0x39
0x02832654: ldr      x9, [x0, #0x48]
0x02832658: tst      w8, #1
0x0283265C: csel     x0, x10, x9, eq
0x02832660: bl       #0x4b400f0
0x02832664: str      w0, [x19, #8]
0x02832668: adrp     x10, #0x11ad000
0x0283266C: mov      w8, #0x22
0x02832670: add      x10, x10, #0x9ed
0x02832674: mov      w9, #0x65
0x02832678: add      x0, sp, #0x20
0x0283267C: add      x1, sp, #8
0x02832680: strb     w8, [sp, #8]
0x02832684: ldr      q0, [x10]
0x02832688: sturh    w9, [sp, #0x19]
0x0283268C: stur     q0, [sp, #9]
0x02832690: bl       #0x227e510
0x02832694: cmp      x21, x0
0x02832698: b.eq     #0x28326b8
0x0283269C: ldrb     w8, [x0, #0x38]
0x028326A0: add      x10, x0, #0x39
0x028326A4: ldr      x9, [x0, #0x48]
0x028326A8: tst      w8, #1
0x028326AC: csel     x0, x10, x9, eq
0x028326B0: bl       #0x4b400f0
0x028326B4: str      w0, [x19, #0xc]
0x028326B8: adrp     x9, #0x1146000
0x028326BC: mov      w8, #0x1a
0x028326C0: add      x9, x9, #0x545
0x028326C4: add      x0, sp, #0x20
0x028326C8: add      x1, sp, #8
0x028326CC: strb     wzr, [sp, #0x16]
0x028326D0: strb     w8, [sp, #8]
0x028326D4: ldr      x10, [x9]
0x028326D8: ldur     x9, [x9, #5]
0x028326DC: stur     x10, [sp, #9]
0x028326E0: stur     x9, [sp, #0xe]
0x028326E4: bl       #0x227e510
0x028326E8: cmp      x21, x0
0x028326EC: b.eq     #0x283270c
0x028326F0: ldrb     w8, [x0, #0x38]
0x028326F4: add      x10, x0, #0x39
0x028326F8: ldr      x9, [x0, #0x48]
0x028326FC: tst      w8, #1
0x02832700: csel     x0, x10, x9, eq
0x02832704: bl       #0x4b400f0
0x02832708: str      w0, [x19, #0x10]
0x0283270C: adrp     x9, #0x1160000
0x02832710: mov      w8, #0x1e
0x02832714: add      x9, x9, #0xce2
0x02832718: add      x0, sp, #0x20
0x0283271C: add      x1, sp, #8
0x02832720: strb     wzr, [sp, #0x18]
0x02832724: strb     w8, [sp, #8]
0x02832728: ldr      x10, [x9]
0x0283272C: ldur     x9, [x9, #7]
0x02832730: stur     x10, [sp, #9]
0x02832734: str      x9, [sp, #0x10]
0x02832738: bl       #0x227e510
0x0283273C: cmp      x21, x0
0x02832740: b.eq     #0x2832760
0x02832744: ldrb     w8, [x0, #0x38]
0x02832748: add      x10, x0, #0x39
0x0283274C: ldr      x9, [x0, #0x48]
0x02832750: tst      w8, #1
0x02832754: csel     x0, x10, x9, eq
0x02832758: bl       #0x4b400f0
0x0283275C: str      w0, [x19, #0x14]
0x02832760: adrp     x11, #0x1208000
0x02832764: mov      w8, #-1
0x02832768: add      x11, x11, #0x4e1
0x0283276C: adrp     x20, #0x522d000
0x02832770: mov      w9, #0x24
0x02832774: mov      w10, #0x7473
0x02832778: str      w8, [x19, #0x4b0]
0x0283277C: add      x5, x19, #0x4c0
0x02832780: ldr      q0, [x11]
0x02832784: strb     wzr, [sp, #0x1b]
0x02832788: ldr      x8, [x20, #0xac0]
0x0283278C: strb     w9, [sp, #8]
0x02832790: sturh    w10, [sp, #0x19]
0x02832794: stur     q0, [sp, #9]
0x02832798: adrp     x0, #0x114d000
0x0283279C: add      x1, sp, #0x20
0x028327A0: add      x0, x0, #0x803
0x028327A4: add      x2, sp, #8
0x028327A8: mov      w3, #0x32
0x028327AC: mov      w4, wzr
0x028327B0: blr      x8
0x028327B4: adrp     x1, #0x11ba000
0x028327B8: add      x0, sp, #8
0x028327BC: add      x1, x1, #0x313
0x028327C0: mov      w2, #0x15
0x028327C4: bl       #0x2282f58
0x028327C8: ldr      x8, [x20, #0xac0]
0x028327CC: add      x5, x19, #0x4cc
0x028327D0: adrp     x0, #0x114d000
0x028327D4: add      x1, sp, #0x20
0x028327D8: add      x0, x0, #0x803
0x028327DC: add      x2, sp, #8
0x028327E0: mov      w3, #0xc8
0x028327E4: mov      w4, wzr
0x028327E8: blr      x8
0x028327EC: adrp     x1, #0x11ee000
0x028327F0: add      x0, sp, #8
0x028327F4: add      x1, x1, #0x26a
0x028327F8: mov      w2, #0x18
0x028327FC: bl       #0x2282f58
0x02832800: ldr      x8, [x20, #0xac0]
0x02832804: add      x5, x19, #0x4d0
0x02832808: adrp     x0, #0x114d000
0x0283280C: add      x1, sp, #0x20
0x02832810: add      x0, x0, #0x803
0x02832814: add      x2, sp, #8
0x02832818: mov      w3, #0x5a
0x0283281C: mov      w4, wzr
0x02832820: blr      x8
0x02832824: adrp     x1, #0x11b4000
0x02832828: add      x0, sp, #8
0x0283282C: add      x1, x1, #0x346
0x02832830: mov      w2, #0x18
0x02832834: bl       #0x2282f58
0x02832838: ldr      x8, [x20, #0xac0]
0x0283283C: add      x5, x19, #0x4d4
0x02832840: adrp     x0, #0x114d000
0x02832844: add      x1, sp, #0x20
0x02832848: add      x0, x0, #0x803
0x0283284C: add      x2, sp, #8
0x02832850: mov      w3, #0x5a
0x02832854: mov      w4, wzr
0x02832858: blr      x8
0x0283285C: adrp     x1, #0x11a0000
0x02832860: add      x0, sp, #8
0x02832864: add      x1, x1, #0x568
0x02832868: mov      w2, #0x13
0x0283286C: bl       #0x2282f58
0x02832870: ldr      x8, [x20, #0xac0]
0x02832874: add      x5, x19, #0x5f4
0x02832878: adrp     x0, #0x114d000
0x0283287C: add      x1, sp, #0x20
0x02832880: add      x0, x0, #0x803
0x02832884: add      x2, sp, #8
0x02832888: mov      w3, #0x32
0x0283288C: mov      w4, wzr
0x02832890: blr      x8
0x02832894: adrp     x1, #0x1174000
0x02832898: add      x0, sp, #8
0x0283289C: add      x1, x1, #0x13f
0x028328A0: mov      w2, #0x1c
0x028328A4: bl       #0x2282f58
0x028328A8: ldr      x8, [x20, #0xac0]
0x028328AC: add      x5, x19, #0x5f8
0x028328B0: adrp     x0, #0x114d000
0x028328B4: add      x1, sp, #0x20
0x028328B8: add      x0, x0, #0x803
0x028328BC: add      x2, sp, #8
0x028328C0: mov      w3, #0x14
0x028328C4: mov      w4, wzr
~~~

### Function start 0x2835a7c
Hits: [{"pc": "0x2835d38", "adrp": "0x2835d2c", "target": "0x114d8b7", "label": "frame=%d,monster_rid=%d,invisible,move_to_it", "keywords": ["invisible"], "fde_start": "0x2835a7c", "fde_end": "0x2835e20", "kind": "add", "reg": "x2"}]
~~~asm
0x02835A7C: sub      sp, sp, #0x50
0x02835A80: str      d8, [sp, #0x10]
0x02835A84: str      x30, [sp, #0x18]
0x02835A88: stp      x24, x23, [sp, #0x20]
0x02835A8C: stp      x22, x21, [sp, #0x30]
0x02835A90: stp      x20, x19, [sp, #0x40]
0x02835A94: ldr      w8, [x2, #0x150]
0x02835A98: orr      w8, w8, #2
0x02835A9C: cmp      w8, #0xf
0x02835AA0: b.ne     #0x2835bd4
0x02835AA4: ldr      w8, [x0, #0x604]
0x02835AA8: mov      x19, x0
0x02835AAC: cmp      w8, #0x6d
0x02835AB0: b.gt     #0x2835ae0
0x02835AB4: adrp     x8, #0x509c000
0x02835AB8: ldr      x8, [x8, #0x70]
0x02835ABC: blr      x8
0x02835AC0: adrp     x1, #0x1153000
0x02835AC4: adrp     x2, #0x1193000
0x02835AC8: ldr      w3, [x19, #0x4c8]
0x02835ACC: add      x1, x1, #0xd0f
0x02835AD0: ldr      w4, [x19, #0x604]
0x02835AD4: add      x2, x2, #0xfe3
0x02835AD8: bl       #0x2185854
0x02835ADC: b        #0x2835bd4
0x02835AE0: adrp     x24, #0x508a000
0x02835AE4: mov      x20, x2
0x02835AE8: mov      x21, x1
0x02835AEC: ldr      x8, [x24, #0xe10]
0x02835AF0: blr      x8
0x02835AF4: ldr      w9, [x19, #0x5b0]
0x02835AF8: mov      w10, #0x64
0x02835AFC: ldr      x8, [x19, #0x4a8]
0x02835B00: adrp     x11, #0x508a000
0x02835B04: add      x3, sp, #0xc
0x02835B08: mov      x4, sp
0x02835B0C: mul      w2, w9, w10
0x02835B10: add      x1, x8, #0x20
0x02835B14: ldr      x8, [x11, #0xe78]
0x02835B18: blr      x8
0x02835B1C: adrp     x23, #0x509c000
0x02835B20: ldr      s8, [sp, #0xc]
0x02835B24: mov      w22, w0
0x02835B28: ldr      x8, [x23, #0x70]
0x02835B2C: blr      x8
0x02835B30: ldr      s0, [sp, #0xc]
0x02835B34: cmp      w22, #1
0x02835B38: ldr      w3, [x19, #0x4c8]
0x02835B3C: fcvt     d0, s0
0x02835B40: b.lt     #0x2835bbc
0x02835B44: fmov     s1, #1.00000000
0x02835B48: fcmp     s8, s1
0x02835B4C: b.ge     #0x2835bbc
0x02835B50: adrp     x1, #0x1153000
0x02835B54: adrp     x2, #0x118e000
0x02835B58: add      x1, x1, #0xd0f
0x02835B5C: add      x2, x2, #0xf7
0x02835B60: mov      w4, w22
0x02835B64: bl       #0x2185854
0x02835B68: ldr      x8, [x24, #0xe10]
0x02835B6C: blr      x8
0x02835B70: ldr      x8, [x19, #0x4a8]
0x02835B74: adrp     x9, #0x508a000
0x02835B78: mov      w3, #0x2a94
0x02835B7C: ldr      w1, [x8, #0x18]
0x02835B80: add      x2, x8, #0x20
0x02835B84: ldr      x8, [x9, #0xe28]
0x02835B88: blr      x8
0x02835B8C: cmp      w0, #2
0x02835B90: b.lt     #0x2835bf4
0x02835B94: ldr      x8, [x23, #0x70]
0x02835B98: mov      w22, w0
0x02835B9C: blr      x8
0x02835BA0: adrp     x1, #0x1153000
0x02835BA4: adrp     x2, #0x11c6000
0x02835BA8: ldr      w3, [x19, #0x4c8]
0x02835BAC: sub      w4, w22, #1
0x02835BB0: add      x1, x1, #0xd0f
0x02835BB4: add      x2, x2, #0xbcc
0x02835BB8: b        #0x2835ad8
0x02835BBC: adrp     x1, #0x1153000
0x02835BC0: adrp     x2, #0x1208000
0x02835BC4: add      x1, x1, #0xd0f
0x02835BC8: add      x2, x2, #0x545
0x02835BCC: mov      w4, w22
0x02835BD0: bl       #0x2185854
0x02835BD4: mov      w0, wzr
0x02835BD8: ldp      x20, x19, [sp, #0x40]
0x02835BDC: ldp      x22, x21, [sp, #0x30]
0x02835BE0: ldp      x24, x23, [sp, #0x20]
0x02835BE4: ldr      x30, [sp, #0x18]
0x02835BE8: ldr      d8, [sp, #0x10]
0x02835BEC: add      sp, sp, #0x50
0x02835BF0: ret      
0x02835BF4: ldr      x9, [x19, #0x4a8]
0x02835BF8: ldr      s0, [x9, #0x58]
0x02835BFC: ldr      s1, [x9, #0x60]
0x02835C00: scvtf    s0, s0
0x02835C04: scvtf    s1, s1
0x02835C08: fdiv     s8, s0, s1
0x02835C0C: ldr      s0, [x19, #0x648]
0x02835C10: fcmp     s8, s0
0x02835C14: b.gt     #0x2835c40
0x02835C18: ldr      x8, [x23, #0x70]
0x02835C1C: blr      x8
0x02835C20: fcvt     d0, s8
0x02835C24: adrp     x1, #0x1153000
0x02835C28: adrp     x2, #0x11e7000
0x02835C2C: ldr      w3, [x19, #0x4c8]
0x02835C30: add      x1, x1, #0xd0f
0x02835C34: add      x2, x2, #0x3fa
0x02835C38: bl       #0x2185854
0x02835C3C: b        #0x2835bd4
0x02835C40: ldr      x8, [sp]
0x02835C44: cbz      x8, #0x2835bd4
0x02835C48: ldr      w10, [x9, #0x18]
0x02835C4C: subs     w9, w10, #1
0x02835C50: b.lt     #0x2835bd4
0x02835C54: ldr      x11, [x8, #0x68]
0x02835C58: cmp      x11, x10
0x02835C5C: b.lo     #0x2835bd4
0x02835C60: ldr      w10, [x8]
0x02835C64: cmp      w10, #0x29
0x02835C68: b.ne     #0x2835c90
0x02835C6C: ldr      x8, [x23, #0x70]
0x02835C70: blr      x8
0x02835C74: adrp     x1, #0x1153000
0x02835C78: adrp     x2, #0x1180000
0x02835C7C: ldr      w3, [x19, #0x4c8]
0x02835C80: add      x1, x1, #0xd0f
0x02835C84: add      x2, x2, #0xb25
0x02835C88: bl       #0x2185854
0x02835C8C: b        #0x2835bd4
0x02835C90: lsr      x10, x9, #3
0x02835C94: ldr      x11, [x8, #0x60]
0x02835C98: and      x10, x10, #0x1ffffff8
0x02835C9C: ldr      x10, [x11, x10]
0x02835CA0: lsr      x9, x10, x9
0x02835CA4: tbz      w9, #0, #0x2835ce8
0x02835CA8: adrp     x9, #0x509e000
0x02835CAC: ldr      w4, [x8, #4]
0x02835CB0: mov      x0, x19
0x02835CB4: mov      x1, x21
0x02835CB8: mov      x2, x20
0x02835CBC: mov      w3, #0xe
0x02835CC0: ldr      x8, [x9, #0xf0]
0x02835CC4: mov      w21, #0xe
0x02835CC8: blr      x8
0x02835CCC: tbz      w0, #0, #0x2835d48
0x02835CD0: ldr      x8, [sp]
0x02835CD4: str      w21, [x20, #0x150]
0x02835CD8: mov      w0, #1
0x02835CDC: ldr      w8, [x8, #4]
0x02835CE0: str      w8, [x20, #0x154]
0x02835CE4: b        #0x2835bd8
0x02835CE8: adrp     x9, #0x1212000
0x02835CEC: ldr      d0, [x9, #0xc68]
0x02835CF0: adrp     x9, #0x542b000
0x02835CF4: add      x9, x9, #0x410
0x02835CF8: str      d0, [x20, #0x150]
0x02835CFC: ldr      x10, [x9]
0x02835D00: ldr      w11, [x8, #0x1c]
0x02835D04: ldur     x8, [x8, #0x14]
0x02835D08: ldr      w9, [x9, #8]
0x02835D0C: str      x10, [x20, #0x158]
0x02835D10: ldr      x10, [x23, #0x70]
0x02835D14: str      w11, [x20, #0x178]
0x02835D18: str      x8, [x20, #0x170]
0x02835D1C: str      w9, [x20, #0x160]
0x02835D20: blr      x10
0x02835D24: ldr      x8, [sp]
0x02835D28: adrp     x1, #0x1153000
0x02835D2C: adrp     x2, #0x114d000
0x02835D30: ldr      w3, [x19, #0x4c8]
0x02835D34: add      x1, x1, #0xd0f
0x02835D38: add      x2, x2, #0x8b7
0x02835D3C: ldr      w4, [x8, #4]
0x02835D40: bl       #0x2185854
0x02835D44: b        #0x2835e18
0x02835D48: ldr      w8, [x19, #0x610]
0x02835D4C: cmp      w8, #0x27
0x02835D50: b.gt     #0x2835db4
0x02835D54: adrp     x8, #0x542b000
0x02835D58: adrp     x9, #0x1212000
0x02835D5C: add      x8, x8, #0x410
0x02835D60: ldr      d0, [x9, #0x9f8]
0x02835D64: ldr      x10, [x8]
0x02835D68: ldr      w8, [x8, #8]
0x02835D6C: ldr      x9, [x23, #0x70]
0x02835D70: str      d0, [x20, #0x150]
0x02835D74: str      x10, [x20, #0x170]
0x02835D78: str      w8, [x20, #0x178]
0x02835D7C: str      x10, [x20, #0x158]
0x02835D80: str      w8, [x20, #0x160]
0x02835D84: blr      x9
0x02835D88: ldr      x8, [sp]
0x02835D8C: adrp     x1, #0x1153000
0x02835D90: adrp     x2, #0x11c0000
0x02835D94: ldr      w3, [x19, #0x4c8]
0x02835D98: ldr      w5, [x19, #0x5c8]
0x02835D9C: add      x1, x1, #0xd0f
0x02835DA0: ldr      w4, [x8, #4]
0x02835DA4: add      x2, x2, #0x74d
0x02835DA8: ldr      w6, [x19, #0x610]
0x02835DAC: bl       #0x2185854
0x02835DB0: b        #0x2835e18
0x02835DB4: adrp     x8, #0x1212000
0x02835DB8: adrp     x9, #0x542b000
0x02835DBC: add      x9, x9, #0x410
0x02835DC0: ldr      d0, [x8, #0xc68]
0x02835DC4: ldr      x8, [sp]
0x02835DC8: ldr      x10, [x9]
0x02835DCC: str      d0, [x20, #0x150]
0x02835DD0: ldr      w9, [x9, #8]
0x02835DD4: ldur     x11, [x8, #0x14]
0x02835DD8: ldr      w8, [x8, #0x1c]
0x02835DDC: str      x10, [x20, #0x158]
0x02835DE0: ldr      x10, [x23, #0x70]
0x02835DE4: str      w9, [x20, #0x160]
0x02835DE8: str      x11, [x20, #0x170]
0x02835DEC: str      w8, [x20, #0x178]
0x02835DF0: blr      x10
0x02835DF4: ldr      x8, [sp]
0x02835DF8: adrp     x1, #0x1153000
0x02835DFC: adrp     x2, #0x1153000
0x02835E00: ldr      w3, [x19, #0x4c8]
0x02835E04: ldr      w5, [x19, #0x5c8]
0x02835E08: add      x1, x1, #0xd0f
0x02835E0C: ldr      w4, [x8, #4]
0x02835E10: add      x2, x2, #0xd38
0x02835E14: bl       #0x2185854
0x02835E18: mov      w0, #1
0x02835E1C: b        #0x2835bd8
~~~

### Function start 0x2837144
Hits: [{"pc": "0x28374f4", "adrp": "0x28374f0", "target": "0x114d91d", "label": "frame=%d,emy_hero=%d,cid=%d,hp=%d,dis_from_main=%d,invisible", "keywords": ["invisible"], "fde_start": "0x2837144", "fde_end": "0x2837710", "kind": "add", "reg": "x23"}]
~~~asm
0x02837144: sub      sp, sp, #0x90
0x02837148: stp      x29, x30, [sp, #0x30]
0x0283714C: stp      x28, x27, [sp, #0x40]
0x02837150: stp      x26, x25, [sp, #0x50]
0x02837154: stp      x24, x23, [sp, #0x60]
0x02837158: stp      x22, x21, [sp, #0x70]
0x0283715C: stp      x20, x19, [sp, #0x80]
0x02837160: mov      x20, x0
0x02837164: adrp     x8, #0x542a000
0x02837168: mov      x19, x1
0x0283716C: add      x0, x0, #0x4f0
0x02837170: add      x21, x20, #0x4f8
0x02837174: ldr      w22, [x8, #0xf00]
0x02837178: ldr      x1, [x20, #0x4f8]
0x0283717C: str      x0, [sp, #0x10]
0x02837180: str      w22, [x20, #0x604]
0x02837184: bl       #0x223f584
0x02837188: adrp     x8, #0x5089000
0x0283718C: add      x0, x20, #0x580
0x02837190: movi     v0.2d, #0000000000000000
0x02837194: str      x21, [x20, #0x4f0]
0x02837198: ldr      x8, [x8, #0x4b0]
0x0283719C: str      x0, [sp, #0x28]
0x028371A0: str      q0, [x21]
0x028371A4: blr      x8
0x028371A8: movi     v0.2d, #0000000000000000
0x028371AC: add      x8, x20, #0x638
0x028371B0: add      x0, x20, #0x6b8
0x028371B4: ldr      x1, [x20, #0x6c0]
0x028371B8: strb     wzr, [x20, #0x65f]
0x028371BC: add      x23, x20, #0x6c0
0x028371C0: strb     wzr, [x20, #0x680]
0x028371C4: str      q0, [x8]
0x028371C8: bl       #0x223f584
0x028371CC: add      x0, x20, #0x720
0x028371D0: ldr      x1, [x20, #0x728]
0x028371D4: str      x23, [x20, #0x6b8]
0x028371D8: add      x23, x20, #0x728
0x028371DC: str      xzr, [x20, #0x6c8]
0x028371E0: str      xzr, [x20, #0x6c0]
0x028371E4: str      x0, [sp, #8]
0x028371E8: bl       #0x223f584
0x028371EC: str      x23, [x20, #0x720]
0x028371F0: str      xzr, [x20, #0x730]
0x028371F4: str      xzr, [x20, #0x728]
0x028371F8: str      w22, [x20, #0x738]
0x028371FC: ldp      x24, x8, [x19, #0x68]
0x02837200: str      x23, [sp, #0x18]
0x02837204: cmp      x24, x8
0x02837208: b.eq     #0x28376ec
0x0283720C: adrp     x25, #0x11fb000
0x02837210: add      x8, x20, #0x7c
0x02837214: add      x26, x20, #0x6d8
0x02837218: add      x25, x25, #0x7f6
0x0283721C: str      x8, [sp, #0x20]
0x02837220: b        #0x2837234
0x02837224: ldr      x8, [x19, #0x70]
0x02837228: add      x24, x24, #0x3f0
0x0283722C: cmp      x24, x8
0x02837230: b.eq     #0x28376ec
0x02837234: ldr      x8, [x20, #0x4a8]
0x02837238: ldr      w9, [x24, #0x18]
0x0283723C: ldr      w10, [x8, #0x18]
0x02837240: cmp      w9, w10
0x02837244: b.eq     #0x2837224
0x02837248: ldr      w9, [x24, #0x58]
0x0283724C: cmp      w9, #1
0x02837250: b.lt     #0x2837224
0x02837254: ldr      w9, [x24, #0xd0]
0x02837258: ldr      w10, [x8, #8]
0x0283725C: cmp      w9, w10
0x02837260: b.ne     #0x283726c
0x02837264: mov      w9, #1
0x02837268: strb     w9, [x20, #0x65f]
0x0283726C: add      x1, x8, #0x20
0x02837270: adrp     x8, #0x517f000
0x02837274: add      x2, x24, #0x20
0x02837278: ldr      x0, [sp, #0x20]
0x0283727C: mov      w3, #1
0x02837280: ldr      x8, [x8, #0x388]
0x02837284: blr      x8
0x02837288: mov      w27, w0
0x0283728C: ldr      x22, [x21]
0x02837290: add      x28, x24, #8
0x02837294: cbz      x22, #0x28372dc
0x02837298: ldr      w8, [x28]
0x0283729C: mov      x23, x21
0x028372A0: ldr      w9, [x22, #0x1c]
0x028372A4: cmp      w8, w9
0x028372A8: b.ge     #0x28372c0
0x028372AC: ldr      x9, [x22]
0x028372B0: cbz      x9, #0x2837328
0x028372B4: mov      x23, x22
0x028372B8: mov      x22, x9
0x028372BC: b        #0x28372a0
0x028372C0: cmp      w9, w8
0x028372C4: b.ge     #0x28372e4
0x028372C8: mov      x23, x22
0x028372CC: ldr      x9, [x23, #8]!
0x028372D0: cbz      x9, #0x28372e4
0x028372D4: mov      x22, x9
0x028372D8: b        #0x28372a0
0x028372DC: mov      x22, x21
0x028372E0: mov      x23, x21
0x028372E4: ldr      x29, [x23]
0x028372E8: cbnz     x29, #0x2837350
0x028372EC: mov      w0, #0x28
0x028372F0: bl       #0x4b40050
0x028372F4: ldr      w8, [x28]
0x028372F8: stp      xzr, xzr, [x0]
0x028372FC: ldr      x9, [sp, #0x10]
0x02837300: str      x22, [x0, #0x10]
0x02837304: mov      x29, x0
0x02837308: stp      w8, wzr, [x0, #0x1c]
0x0283730C: str      x0, [x23]
0x02837310: ldr      x8, [x9]
0x02837314: ldr      x8, [x8]
0x02837318: cbz      x8, #0x2837338
0x0283731C: str      x8, [x9]
0x02837320: ldr      x1, [x23]
0x02837324: b        #0x283733c
0x02837328: mov      x23, x22
0x0283732C: ldr      x29, [x23]
0x02837330: cbnz     x29, #0x2837350
0x02837334: b        #0x28372ec
0x02837338: mov      x1, x29
0x0283733C: ldr      x0, [x20, #0x4f8]
0x02837340: bl       #0x2260c4c
0x02837344: ldr      x8, [x20, #0x500]
0x02837348: add      x8, x8, #1
0x0283734C: str      x8, [x20, #0x500]
0x02837350: adrp     x8, #0x5089000
0x02837354: ldr      x0, [sp, #0x28]
0x02837358: mov      x1, x28
0x0283735C: str      w27, [x29, #0x20]
0x02837360: ldr      x8, [x8, #0x5d0]
0x02837364: blr      x8
0x02837368: adrp     x8, #0x509e000
0x0283736C: str      x24, [x0]
0x02837370: ldr      w1, [x24, #8]
0x02837374: mov      x0, x20
0x02837378: mov      w2, w27
0x0283737C: ldr      x8, [x8, #0x360]
0x02837380: blr      x8
0x02837384: ldr      w8, [x20, #0x604]
0x02837388: cmp      w8, w27
0x0283738C: b.le     #0x2837398
0x02837390: str      w27, [x20, #0x604]
0x02837394: str      x24, [x20, #0x638]
0x02837398: ldrsw    x8, [x24, #0x54]
0x0283739C: mov      w9, #0x851f
0x028373A0: movk     w9, #0x51eb, lsl #16
0x028373A4: mul      x8, x8, x9
0x028373A8: lsr      x9, x8, #0x3f
0x028373AC: asr      x8, x8, #0x25
0x028373B0: add      w8, w8, w9
0x028373B4: cmp      w27, w8
0x028373B8: b.ge     #0x28373c4
0x028373BC: mov      w8, #1
0x028373C0: strb     w8, [x20, #0x680]
0x028373C4: ldr      w8, [x20, #0x5b0]
0x028373C8: cmp      w27, w8
0x028373CC: b.ge     #0x28373d4
0x028373D0: str      x24, [x20, #0x640]
0x028373D4: ldr      x22, [x26]
0x028373D8: cbz      x22, #0x283745c
0x028373DC: ldr      w8, [x28]
0x028373E0: mov      x9, x26
0x028373E4: mov      x10, x22
0x028373E8: ldr      w11, [x10, #0x1c]
0x028373EC: cmp      w11, w8
0x028373F0: cset     w11, lt
0x028373F4: csel     x9, x9, x10, lt
0x028373F8: ldr      x10, [x10, w11, uxtw #3]
0x028373FC: cbnz     x10, #0x28373e8
0x02837400: cmp      x9, x26
0x02837404: b.eq     #0x2837414
0x02837408: ldr      w9, [x9, #0x1c]
0x0283740C: cmp      w8, w9
0x02837410: b.ge     #0x28374cc
0x02837414: ldr      w23, [x19]
0x02837418: cbz      x22, #0x2837460
0x0283741C: mov      x25, x26
0x02837420: ldr      w9, [x22, #0x1c]
0x02837424: cmp      w8, w9
0x02837428: b.ge     #0x2837440
0x0283742C: ldr      x9, [x22]
0x02837430: cbz      x9, #0x283759c
0x02837434: mov      x25, x22
0x02837438: mov      x22, x9
0x0283743C: b        #0x2837420
0x02837440: cmp      w9, w8
0x02837444: b.ge     #0x2837468
0x02837448: mov      x25, x22
0x0283744C: ldr      x9, [x25, #8]!
0x02837450: cbz      x9, #0x2837468
0x02837454: mov      x22, x9
0x02837458: b        #0x2837420
0x0283745C: ldr      w23, [x19]
0x02837460: mov      x22, x26
0x02837464: mov      x25, x26
0x02837468: ldr      x29, [x25]
0x0283746C: cbnz     x29, #0x28374c0
0x02837470: mov      w0, #0x28
0x02837474: bl       #0x4b40050
0x02837478: ldr      w8, [x28]
0x0283747C: stp      xzr, xzr, [x0]
0x02837480: str      x22, [x0, #0x10]
0x02837484: mov      x29, x0
0x02837488: stp      w8, wzr, [x0, #0x1c]
0x0283748C: str      x0, [x25]
0x02837490: ldr      x8, [x20, #0x6d0]
0x02837494: ldr      x8, [x8]
0x02837498: cbz      x8, #0x28374a8
0x0283749C: str      x8, [x20, #0x6d0]
0x028374A0: ldr      x1, [x25]
0x028374A4: b        #0x28374ac
0x028374A8: mov      x1, x29
0x028374AC: ldr      x0, [x20, #0x6d8]
0x028374B0: bl       #0x2260c4c
0x028374B4: ldr      x8, [x20, #0x6e0]
0x028374B8: add      x8, x8, #1
0x028374BC: str      x8, [x20, #0x6e0]
0x028374C0: adrp     x25, #0x11fb000
0x028374C4: str      w23, [x29, #0x20]
0x028374C8: add      x25, x25, #0x7f6
0x028374CC: ldr      x8, [x20, #0x4a8]
0x028374D0: mov      x0, x25
0x028374D4: ldr      w3, [x19]
0x028374D8: mov      x1, x24
0x028374DC: mov      w4, wzr
0x028374E0: ldr      w2, [x8, #0x18]
0x028374E4: adrp     x8, #0x522d000
0x028374E8: ldr      x8, [x8, #0xb70]
0x028374EC: blr      x8
0x028374F0: adrp     x23, #0x114d000
0x028374F4: add      x23, x23, #0x91d
0x028374F8: tbz      w0, #0, #0x28375d8
0x028374FC: ldr      x22, [x26]
0x02837500: cbz      x22, #0x2837548
~~~

### Function start 0x285ac94
Hits: [{"pc": "0x285ea70", "adrp": "0x285ea68", "target": "0x11d8792", "label": "invisible_range", "keywords": ["invisible"], "fde_start": "0x285ac94", "fde_end": "0x2860024", "kind": "add", "reg": "x1"}, {"pc": "0x285eaa8", "adrp": "0x285eaa0", "target": "0x11d8792", "label": "invisible_range", "keywords": ["invisible"], "fde_start": "0x285ac94", "fde_end": "0x2860024", "kind": "add", "reg": "x1"}]
~~~asm
0x0285AC94: stp      x29, x30, [sp, #-0x60]!
0x0285AC98: stp      x28, x27, [sp, #0x10]
0x0285AC9C: stp      x26, x25, [sp, #0x20]
0x0285ACA0: stp      x24, x23, [sp, #0x30]
0x0285ACA4: stp      x22, x21, [sp, #0x40]
0x0285ACA8: stp      x20, x19, [sp, #0x50]
0x0285ACAC: sub      sp, sp, #0x1f0
0x0285ACB0: ldr      w8, [sp, #0x298]
0x0285ACB4: stp      x2, x7, [sp, #0xe0]
0x0285ACB8: ldr      w19, [sp, #0x288]
0x0285ACBC: stp      w6, w1, [sp, #0xbc]
0x0285ACC0: ldr      w29, [sp, #0x258]
0x0285ACC4: str      w5, [sp, #0xdc]
0x0285ACC8: str      w8, [sp, #0xb8]
0x0285ACCC: ldrb     w8, [sp, #0x268]
0x0285ACD0: ldr      w21, [sp, #0x250]
0x0285ACD4: mov      w26, w4
0x0285ACD8: ldr      w20, [sp, #0x290]
0x0285ACDC: mov      w28, w3
0x0285ACE0: str      w8, [sp, #0xf0]
0x0285ACE4: adrp     x8, #0x509c000
0x0285ACE8: ldr      w22, [sp, #0x260]
0x0285ACEC: mov      x25, x0
0x0285ACF0: ldr      w23, [sp, #0x278]
0x0285ACF4: ldr      x8, [x8, #0x70]
0x0285ACF8: ldr      w27, [sp, #0x280]
0x0285ACFC: ldr      w24, [sp, #0x270]
0x0285AD00: blr      x8
0x0285AD04: adrp     x1, #0x11d3000
0x0285AD08: adrp     x2, #0x1159000
0x0285AD0C: add      x1, x1, #0xc5d
0x0285AD10: add      x2, x2, #0x444
0x0285AD14: mov      w3, w28
0x0285AD18: mov      w4, w21
0x0285AD1C: mov      w5, w29
0x0285AD20: mov      w6, w26
0x0285AD24: mov      w7, w22
0x0285AD28: str      w24, [sp, #0x18]
0x0285AD2C: str      w26, [sp, #0xb4]
0x0285AD30: str      w19, [sp, #0x10]
0x0285AD34: str      w27, [sp, #8]
0x0285AD38: str      w23, [sp]
0x0285AD3C: bl       #0x2185854
0x0285AD40: ldr      w8, [sp, #0xf0]
0x0285AD44: cmp      w20, #0x1a
0x0285AD48: str      w22, [x25, #0xddc]
0x0285AD4C: ldr      w9, [x25, #0xdec]
0x0285AD50: mov      x22, x25
0x0285AD54: str      w24, [x25, #0x3934]
0x0285AD58: strb     w8, [x25, #0xde8]
0x0285AD5C: cset     w8, lt
0x0285AD60: str      w19, [sp, #0xa4]
0x0285AD64: str      w19, [x25, #0x3808]
0x0285AD68: str      w23, [x25, #0x34a0]
0x0285AD6C: str      w27, [x25, #0x34a4]
0x0285AD70: str      w20, [x25, #0xcc8]
0x0285AD74: str      w8, [x25, #0xccc]
0x0285AD78: cbnz     w9, #0x285adac
0x0285AD7C: ldr      w0, [sp, #0xc0]
0x0285AD80: bl       #0x4b40380
0x0285AD84: bl       #0x4b40370
0x0285AD88: mov      w8, #0x851f
0x0285AD8C: movk     w8, #0x51eb, lsl #16
0x0285AD90: smull    x8, w0, w8
0x0285AD94: lsr      x9, x8, #0x3f
0x0285AD98: asr      x8, x8, #0x25
0x0285AD9C: add      w8, w8, w9
0x0285ADA0: mov      w9, #0x64
0x0285ADA4: msub     w8, w8, w9, w0
0x0285ADA8: str      w8, [x22, #0xdec]
0x0285ADAC: mov      w8, #0x3268
0x0285ADB0: add      w25, w29, w21
0x0285ADB4: add      x19, x22, x8
0x0285ADB8: ands     w20, w28, #0xfffffffd
0x0285ADBC: mov      w23, w28
0x0285ADC0: b.eq     #0x285add8
0x0285ADC4: mov      x26, x22
0x0285ADC8: adrp     x27, #0x509c000
0x0285ADCC: cmp      w23, #1
0x0285ADD0: b.ls     #0x285ae70
0x0285ADD4: b        #0x285f2bc
0x0285ADD8: mov      w8, #0x34b8
0x0285ADDC: ldr      x1, [sp, #0xe8]
0x0285ADE0: add      x26, x22, x8
0x0285ADE4: mov      x24, x19
0x0285ADE8: mov      x0, x26
0x0285ADEC: ldr      w28, [sp, #0x2a0]
0x0285ADF0: ldr      w19, [sp, #0x2a8]
0x0285ADF4: bl       #0x2282510
0x0285ADF8: adrp     x27, #0x509c000
0x0285ADFC: str      w21, [x22, #0x34d0]
0x0285AE00: str      w29, [x22, #0x34d4]
0x0285AE04: ldr      x8, [x27, #0x70]
0x0285AE08: blr      x8
0x0285AE0C: adrp     x8, #0x509c000
0x0285AE10: ldr      w2, [x22, #0x34d0]
0x0285AE14: ldr      w3, [x22, #0x34d4]
0x0285AE18: mov      x1, x26
0x0285AE1C: mov      w4, wzr
0x0285AE20: ldr      x8, [x8, #0x40]
0x0285AE24: blr      x8
0x0285AE28: ldr      x8, [x27, #0x70]
0x0285AE2C: blr      x8
0x0285AE30: adrp     x8, #0x509c000
0x0285AE34: mov      w1, w28
0x0285AE38: ldr      x8, [x8, #0x50]
0x0285AE3C: blr      x8
0x0285AE40: mov      x26, x22
0x0285AE44: ldr      w8, [sp, #0xdc]
0x0285AE48: str      w19, [x22, #0xee4]
0x0285AE4C: tbz      w8, #0, #0x285ae58
0x0285AE50: mov      w8, #1
0x0285AE54: str      w8, [x26, #0xedc]
0x0285AE58: movi     v0.2s, #1
0x0285AE5C: mov      x19, x24
0x0285AE60: add      x8, x24, #0x274
0x0285AE64: cmp      w23, #2
0x0285AE68: str      d0, [x8]
0x0285AE6C: b.hs     #0x285f124
0x0285AE70: adrp     x8, #0x5179000
0x0285AE74: mov      w10, #0x1688
0x0285AE78: stp      w23, w25, [sp, #0x88]
0x0285AE7C: mov      x25, x26
0x0285AE80: add      x26, x26, x10
0x0285AE84: mov      w10, #0x2010
0x0285AE88: add      x23, sp, #0x180
0x0285AE8C: mov      w9, #0x3d02
0x0285AE90: add      x0, x25, x10
0x0285AE94: ldr      x8, [x8, #0xb20]
0x0285AE98: strb     wzr, [sp, #0x182]
0x0285AE9C: strh     w9, [sp, #0x180]
0x0285AEA0: add      x2, sp, #0x180
0x0285AEA4: ldr      x1, [sp, #0xe0]
0x0285AEA8: mov      x3, x26
0x0285AEAC: str      x0, [sp, #0xe8]
0x0285AEB0: blr      x8
0x0285AEB4: mov      w22, w0
0x0285AEB8: ldrb     w8, [sp, #0x180]
0x0285AEBC: tbz      w8, #0, #0x285aec8
0x0285AEC0: ldr      x0, [x23, #0x10]
0x0285AEC4: bl       #0x4b3fb60
0x0285AEC8: tbz      w22, #0, #0x285f2f0
0x0285AECC: mov      w8, #0x15d1
0x0285AED0: movi     v0.2s, #1
0x0285AED4: add      x8, x25, x8
0x0285AED8: ldr      x9, [x27, #0x70]
0x0285AEDC: str      w20, [sp, #0x5c]
0x0285AEE0: str      x19, [sp, #0x70]
0x0285AEE4: strb     wzr, [x19, #0x284]
0x0285AEE8: str      wzr, [x25, #0x15d4]
0x0285AEEC: strb     wzr, [x8]
0x0285AEF0: strb     wzr, [x8, #7]
0x0285AEF4: str      d0, [x25, #0x3280]
0x0285AEF8: blr      x9
0x0285AEFC: adrp     x20, #0x509c000
0x0285AF00: mov      w1, #0xa
0x0285AF04: ldr      x8, [x20, #0x20]
0x0285AF08: blr      x8
0x0285AF0C: adrp     x8, #0x11a6000
0x0285AF10: mov      w19, #0x12
0x0285AF14: add      x8, x8, #0x942
0x0285AF18: mov      w22, #0x6c
0x0285AF1C: add      x1, sp, #0x180
0x0285AF20: mov      x0, x26
0x0285AF24: strb     w19, [sp, #0x180]
0x0285AF28: ldr      x21, [x8]
0x0285AF2C: add      x8, sp, #0x82
0x0285AF30: sturh    w22, [x23, #9]
0x0285AF34: stur     x21, [x8, #0xff]
0x0285AF38: bl       #0x227e510
0x0285AF3C: mov      w8, #0x1690
0x0285AF40: add      x28, x25, x8
0x0285AF44: cmp      x28, x0
0x0285AF48: b.eq     #0x285afc8
0x0285AF4C: add      x8, sp, #0x82
0x0285AF50: add      x1, sp, #0x1d8
0x0285AF54: add      x2, sp, #0x180
0x0285AF58: mov      x0, x26
0x0285AF5C: strb     w19, [sp, #0x180]
0x0285AF60: sturh    w22, [x23, #9]
0x0285AF64: stur     x21, [x8, #0xff]
0x0285AF68: bl       #0x227e070
0x0285AF6C: ldr      x24, [x0]
0x0285AF70: cbnz     x24, #0x285afe8
0x0285AF74: mov      x22, x0
0x0285AF78: mov      w0, #0x50
0x0285AF7C: bl       #0x4b40050
0x0285AF80: ldr      x8, [x23, #0x10]
0x0285AF84: stp      xzr, xzr, [x0, #0x40]
0x0285AF88: ldr      q0, [sp, #0x180]
0x0285AF8C: str      xzr, [sp, #0x180]
0x0285AF90: stp      xzr, xzr, [x23, #8]
0x0285AF94: mov      x24, x0
0x0285AF98: stp      x8, xzr, [x0, #0x30]
0x0285AF9C: ldr      x8, [x23, #0x58]
0x0285AFA0: str      q0, [x0, #0x20]
0x0285AFA4: stp      xzr, xzr, [x0]
0x0285AFA8: str      x8, [x0, #0x10]
0x0285AFAC: str      x0, [x22]
0x0285AFB0: ldr      x8, [x26]
0x0285AFB4: ldr      x8, [x8]
0x0285AFB8: cbz      x8, #0x285afd0
0x0285AFBC: str      x8, [x26]
0x0285AFC0: ldr      x1, [x22]
0x0285AFC4: b        #0x285afd4
0x0285AFC8: mov      w22, wzr
0x0285AFCC: b        #0x285b004
0x0285AFD0: mov      x1, x24
0x0285AFD4: ldr      x0, [x25, #0x1690]
0x0285AFD8: bl       #0x2260c4c
0x0285AFDC: ldr      x8, [x25, #0x1698]
0x0285AFE0: add      x8, x8, #1
0x0285AFE4: str      x8, [x25, #0x1698]
0x0285AFE8: ldrb     w8, [x24, #0x38]
0x0285AFEC: add      x10, x24, #0x39
0x0285AFF0: ldr      x9, [x24, #0x48]
0x0285AFF4: tst      w8, #1
0x0285AFF8: csel     x0, x10, x9, eq
0x0285AFFC: bl       #0x4b400f0
0x0285B000: mov      w22, w0
0x0285B004: ldr      x8, [x27, #0x70]
0x0285B008: blr      x8
0x0285B00C: ldr      x8, [x20, #0x20]
0x0285B010: mov      w1, w22
0x0285B014: blr      x8
0x0285B018: mov      w20, #0x7067
0x0285B01C: mov      w19, #0xc
0x0285B020: movk     w20, #0x5f75, lsl #16
0x0285B024: mov      w21, #0x6469
0x0285B028: add      x8, sp, #0x82
0x0285B02C: add      x1, sp, #0x180
0x0285B030: mov      x0, x26
0x0285B034: str      wzr, [x25, #0xd7c]
0x0285B038: strb     w19, [sp, #0x180]
0x0285B03C: stur     w20, [x8, #0xff]
0x0285B040: sturh    w21, [x23, #5]
0x0285B044: strb     wzr, [sp, #0x187]
0x0285B048: bl       #0x227e510
0x0285B04C: cmp      x28, x0
0x0285B050: b.eq     #0x285b128
~~~

### Function start 0x28c9b6c
Hits: [{"pc": "0x28c9ba0", "adrp": "0x28c9b98", "target": "0x11e76f3", "label": "CreateMoveDirectionState", "keywords": ["MoveDir"], "fde_start": "0x28c9b6c", "fde_end": "0x28c9c08", "kind": "add", "reg": "x1"}]
~~~asm
0x028C9B6C: str      x30, [sp, #-0x20]!
0x028C9B70: stp      x20, x19, [sp, #0x10]
0x028C9B74: adrp     x20, #0x53dc000
0x028C9B78: ldr      x0, [x20, #0x840]
0x028C9B7C: cbnz     x0, #0x28c9bfc
0x028C9B80: mov      w0, #0x168
0x028C9B84: bl       #0x4b40050
0x028C9B88: adrp     x8, #0x5040000
0x028C9B8C: mov      x19, x0
0x028C9B90: ldr      x8, [x8, #0x20]
0x028C9B94: cbz      x8, #0x28c9bb4
0x028C9B98: adrp     x1, #0x11e7000
0x028C9B9C: mov      x0, x19
0x028C9BA0: add      x1, x1, #0x6f3
0x028C9BA4: mov      x2, xzr
0x028C9BA8: mov      x3, xzr
0x028C9BAC: mov      w4, #0x18
0x028C9BB0: blr      x8
0x028C9BB4: adrp     x8, #0x4ffc000
0x028C9BB8: adrp     x9, #0x50a3000
0x028C9BBC: str      x19, [x20, #0x840]
0x028C9BC0: ldr      x8, [x8, #0xdc8]
0x028C9BC4: ldr      x9, [x9, #0x838]
0x028C9BC8: str      x8, [x19, #0x160]
0x028C9BCC: blr      x9
0x028C9BD0: ldr      x8, [x19]
0x028C9BD4: mov      x1, x0
0x028C9BD8: mov      x0, x19
0x028C9BDC: mov      w2, wzr
0x028C9BE0: ldr      x8, [x8, #0x10]
0x028C9BE4: blr      x8
0x028C9BE8: ldr      x8, [x19]
0x028C9BEC: mov      x0, x19
0x028C9BF0: ldr      x8, [x8, #0x18]
0x028C9BF4: blr      x8
0x028C9BF8: ldr      x0, [x20, #0x840]
0x028C9BFC: ldp      x20, x19, [sp, #0x10]
0x028C9C00: ldr      x30, [sp], #0x20
0x028C9C04: ret      
~~~

### Function start 0x28d1600
Hits: [{"pc": "0x28d1634", "adrp": "0x28d162c", "target": "0x114079c", "label": "SyncPositionMoveCmd", "keywords": ["SyncPosition"], "fde_start": "0x28d1600", "fde_end": "0x28d1690", "kind": "add", "reg": "x1"}]
~~~asm
0x028D1600: str      x30, [sp, #-0x20]!
0x028D1604: stp      x20, x19, [sp, #0x10]
0x028D1608: adrp     x20, #0x53dc000
0x028D160C: ldr      x0, [x20, #0x728]
0x028D1610: cbnz     x0, #0x28d1684
0x028D1614: mov      w0, #0x160
0x028D1618: bl       #0x4b40050
0x028D161C: adrp     x8, #0x503f000
0x028D1620: mov      x19, x0
0x028D1624: ldr      x8, [x8, #0xeb0]
0x028D1628: cbz      x8, #0x28d1648
0x028D162C: adrp     x1, #0x1140000
0x028D1630: mov      x0, x19
0x028D1634: add      x1, x1, #0x79c
0x028D1638: mov      x2, xzr
0x028D163C: mov      x3, xzr
0x028D1640: mov      w4, #0x40
0x028D1644: blr      x8
0x028D1648: adrp     x8, #0x50a3000
0x028D164C: str      x19, [x20, #0x728]
0x028D1650: ldr      x8, [x8, #0x838]
0x028D1654: blr      x8
0x028D1658: ldr      x8, [x19]
0x028D165C: mov      x1, x0
0x028D1660: mov      x0, x19
0x028D1664: mov      w2, wzr
0x028D1668: ldr      x8, [x8, #0x10]
0x028D166C: blr      x8
0x028D1670: ldr      x8, [x19]
0x028D1674: mov      x0, x19
0x028D1678: ldr      x8, [x8, #0x18]
0x028D167C: blr      x8
0x028D1680: ldr      x0, [x20, #0x728]
0x028D1684: ldp      x20, x19, [sp, #0x10]
0x028D1688: ldr      x30, [sp], #0x20
0x028D168C: ret      
~~~

### Function start 0x292768c
Hits: [{"pc": "0x29276c0", "adrp": "0x29276b8", "target": "0x1208aa0", "label": "MoveDirectionCmd", "keywords": ["MoveDir"], "fde_start": "0x292768c", "fde_end": "0x2927728", "kind": "add", "reg": "x1"}]
~~~asm
0x0292768C: str      x30, [sp, #-0x20]!
0x02927690: stp      x20, x19, [sp, #0x10]
0x02927694: adrp     x20, #0x5273000
0x02927698: ldr      x0, [x20, #0x608]
0x0292769C: cbnz     x0, #0x292771c
0x029276A0: mov      w0, #0x168
0x029276A4: bl       #0x4b40050
0x029276A8: adrp     x8, #0x5040000
0x029276AC: mov      x19, x0
0x029276B0: ldr      x8, [x8, #0x20]
0x029276B4: cbz      x8, #0x29276d4
0x029276B8: adrp     x1, #0x1208000
0x029276BC: mov      x0, x19
0x029276C0: add      x1, x1, #0xaa0
0x029276C4: mov      x2, xzr
0x029276C8: mov      x3, xzr
0x029276CC: mov      w4, #0x20
0x029276D0: blr      x8
0x029276D4: adrp     x8, #0x4ffc000
0x029276D8: adrp     x9, #0x50a5000
0x029276DC: str      x19, [x20, #0x608]
0x029276E0: ldr      x8, [x8, #0x550]
0x029276E4: ldr      x9, [x9, #0xc78]
0x029276E8: str      x8, [x19, #0x160]
0x029276EC: blr      x9
0x029276F0: ldr      x8, [x19]
0x029276F4: mov      x1, x0
0x029276F8: mov      x0, x19
0x029276FC: mov      w2, wzr
0x02927700: ldr      x8, [x8, #0x10]
0x02927704: blr      x8
0x02927708: ldr      x8, [x19]
0x0292770C: mov      x0, x19
0x02927710: ldr      x8, [x8, #0x18]
0x02927714: blr      x8
0x02927718: ldr      x0, [x20, #0x608]
0x0292771C: ldp      x20, x19, [sp, #0x10]
0x02927720: ldr      x30, [sp], #0x20
0x02927724: ret      
~~~

### Function start 0x2932664
Hits: [{"pc": "0x2932698", "adrp": "0x2932690", "target": "0x11f554b", "label": "Physics::MoveDirectionState", "keywords": ["MoveDir"], "fde_start": "0x2932664", "fde_end": "0x2932700", "kind": "add", "reg": "x1"}]
~~~asm
0x02932664: str      x30, [sp, #-0x20]!
0x02932668: stp      x20, x19, [sp, #0x10]
0x0293266C: adrp     x20, #0x5272000
0x02932670: ldr      x0, [x20, #0x160]
0x02932674: cbnz     x0, #0x29326f4
0x02932678: mov      w0, #0x168
0x0293267C: bl       #0x4b40050
0x02932680: adrp     x8, #0x5040000
0x02932684: mov      x19, x0
0x02932688: ldr      x8, [x8, #0x20]
0x0293268C: cbz      x8, #0x29326ac
0x02932690: adrp     x1, #0x11f5000
0x02932694: mov      x0, x19
0x02932698: add      x1, x1, #0x54b
0x0293269C: mov      x2, xzr
0x029326A0: mov      x3, xzr
0x029326A4: mov      w4, #0x58
0x029326A8: blr      x8
0x029326AC: adrp     x8, #0x4ffc000
0x029326B0: adrp     x9, #0x509f000
0x029326B4: str      x19, [x20, #0x160]
0x029326B8: ldr      x8, [x8, #0x328]
0x029326BC: ldr      x9, [x9, #0x920]
0x029326C0: str      x8, [x19, #0x160]
0x029326C4: blr      x9
0x029326C8: ldr      x8, [x19]
0x029326CC: mov      x1, x0
0x029326D0: mov      x0, x19
0x029326D4: mov      w2, wzr
0x029326D8: ldr      x8, [x8, #0x10]
0x029326DC: blr      x8
0x029326E0: ldr      x8, [x19]
0x029326E4: mov      x0, x19
0x029326E8: ldr      x8, [x8, #0x18]
0x029326EC: blr      x8
0x029326F0: ldr      x0, [x20, #0x160]
0x029326F4: ldp      x20, x19, [sp, #0x10]
0x029326F8: ldr      x30, [sp], #0x20
0x029326FC: ret      
~~~

### Function start 0x29e9e0c
Hits: [{"pc": "0x29e9e2c", "adrp": "0x29e9e28", "target": "0x1154147", "label": "AGE::SimpleMoveDirType", "keywords": ["MoveDir"], "fde_start": "0x29e9e0c", "fde_end": "0x29e9ef0", "kind": "add", "reg": "x1"}]
~~~asm
0x029E9E0C: sub      sp, sp, #0x30
0x029E9E10: str      x30, [sp, #0x10]
0x029E9E14: stp      x20, x19, [sp, #0x20]
0x029E9E18: adrp     x20, #0x53e1000
0x029E9E1C: ldr      x19, [x20, #0x2a8]
0x029E9E20: cbnz     x19, #0x29e9eac
0x029E9E24: adrp     x8, #0x50b8000
0x029E9E28: adrp     x1, #0x1154000
0x029E9E2C: add      x1, x1, #0x147
0x029E9E30: mov      x0, sp
0x029E9E34: stp      xzr, xzr, [sp]
0x029E9E38: ldr      x8, [x8, #0x3f8]
0x029E9E3C: blr      x8
0x029E9E40: adrp     x8, #0x5206000
0x029E9E44: ldr      x8, [x8, #0x9e8]
0x029E9E48: mov      x0, sp
0x029E9E4C: blr      x8
0x029E9E50: mov      x19, x0
0x029E9E54: str      x0, [x20, #0x2a8]
0x029E9E58: cbz      x0, #0x29e9e68
0x029E9E5C: ldrb     w8, [sp, #4]
0x029E9E60: tbz      w8, #0, #0x29e9e9c
0x029E9E64: b        #0x29e9eac
0x029E9E68: mov      w0, #0x180
0x029E9E6C: bl       #0x4b40050
0x029E9E70: adrp     x8, #0x503f000
0x029E9E74: mov      x19, x0
0x029E9E78: ldr      x8, [x8, #0xf60]
0x029E9E7C: cbz      x8, #0x29e9e90
0x029E9E80: mov      x1, sp
0x029E9E84: mov      x0, x19
0x029E9E88: mov      w2, #4
0x029E9E8C: blr      x8
0x029E9E90: str      x19, [x20, #0x2a8]
0x029E9E94: ldrb     w8, [sp, #4]
0x029E9E98: tbnz     w8, #0, #0x29e9eac
0x029E9E9C: adrp     x8, #0x50b8000
0x029E9EA0: ldr      x8, [x8, #0x1d0]
0x029E9EA4: mov      x0, sp
0x029E9EA8: blr      x8
0x029E9EAC: mov      x0, x19
0x029E9EB0: ldr      x30, [sp, #0x10]
0x029E9EB4: ldp      x20, x19, [sp, #0x20]
0x029E9EB8: add      sp, sp, #0x30
0x029E9EBC: ret      
0x029E9EC0: bl       #0x2236550
0x029E9EC4: b        #0x29e9ec8
0x029E9EC8: mov      x19, x0
0x029E9ECC: ldrb     w8, [sp, #4]
0x029E9ED0: tbnz     w8, #0, #0x29e9ee4
0x029E9ED4: adrp     x8, #0x50b8000
0x029E9ED8: ldr      x8, [x8, #0x1d0]
0x029E9EDC: mov      x0, sp
0x029E9EE0: blr      x8
0x029E9EE4: mov      x0, x19
0x029E9EE8: bl       #0x2231bf0
0x029E9EEC: bl       #0x2236550
~~~

### Function start 0x2a0df48
Hits: [{"pc": "0x2a0e360", "adrp": "0x2a0e35c", "target": "0x119a5c3", "label": "CheckActorPositionCrossWall", "keywords": ["ActorPos"], "fde_start": "0x2a0df48", "fde_end": "0x2a0e478", "kind": "add", "reg": "x1"}]
~~~asm
0x02A0DF48: stp      x30, x21, [sp, #-0x20]!
0x02A0DF4C: stp      x20, x19, [sp, #0x10]
0x02A0DF50: adrp     x8, #0x50b6000
0x02A0DF54: adrp     x20, #0x50b3000
0x02A0DF58: adrp     x1, #0x11c0000
0x02A0DF5C: add      x1, x1, #0xef1
0x02A0DF60: ldr      x0, [x8, #0xdd8]
0x02A0DF64: ldr      x8, [x20, #0x780]
0x02A0DF68: str      xzr, [x0, #8]
0x02A0DF6C: blr      x8
0x02A0DF70: adrp     x8, #0x50b6000
0x02A0DF74: adrp     x1, #0x1161000
0x02A0DF78: add      x1, x1, #0x61a
0x02A0DF7C: ldr      x0, [x8, #0xfc8]
0x02A0DF80: ldr      x8, [x20, #0x780]
0x02A0DF84: str      xzr, [x0, #8]
0x02A0DF88: blr      x8
0x02A0DF8C: adrp     x8, #0x50b6000
0x02A0DF90: adrp     x1, #0x117a000
0x02A0DF94: add      x1, x1, #0xf9a
0x02A0DF98: ldr      x0, [x8, #0xdc0]
0x02A0DF9C: ldr      x8, [x20, #0x780]
0x02A0DFA0: str      xzr, [x0, #8]
0x02A0DFA4: blr      x8
0x02A0DFA8: adrp     x19, #0x53dd000
0x02A0DFAC: adrp     x1, #0x117a000
0x02A0DFB0: add      x19, x19, #0xb8
0x02A0DFB4: ldr      x8, [x20, #0x780]
0x02A0DFB8: add      x1, x1, #0xfa4
0x02A0DFBC: mov      x0, x19
0x02A0DFC0: str      xzr, [x19, #8]
0x02A0DFC4: blr      x8
0x02A0DFC8: adrp     x8, #0x50b6000
0x02A0DFCC: adrp     x1, #0x11e1000
0x02A0DFD0: add      x1, x1, #0x32c
0x02A0DFD4: ldr      x0, [x8, #0xf50]
0x02A0DFD8: ldr      x8, [x20, #0x780]
0x02A0DFDC: str      xzr, [x0, #8]
0x02A0DFE0: blr      x8
0x02A0DFE4: adrp     x8, #0x50b6000
0x02A0DFE8: adrp     x1, #0x114e000
0x02A0DFEC: add      x1, x1, #0xa3
0x02A0DFF0: ldr      x0, [x8, #0xf30]
0x02A0DFF4: ldr      x8, [x20, #0x780]
0x02A0DFF8: str      xzr, [x0, #8]
0x02A0DFFC: blr      x8
0x02A0E000: adrp     x8, #0x50b6000
0x02A0E004: adrp     x1, #0x11fb000
0x02A0E008: add      x1, x1, #0xdbd
0x02A0E00C: ldr      x0, [x8, #0xf38]
0x02A0E010: ldr      x8, [x20, #0x780]
0x02A0E014: str      xzr, [x0, #8]
0x02A0E018: blr      x8
0x02A0E01C: adrp     x8, #0x50b6000
0x02A0E020: adrp     x1, #0x11e7000
0x02A0E024: add      x1, x1, #0x9e3
0x02A0E028: ldr      x0, [x8, #0xe28]
0x02A0E02C: ldr      x8, [x20, #0x780]
0x02A0E030: str      xzr, [x0, #8]
0x02A0E034: blr      x8
0x02A0E038: adrp     x8, #0x50b6000
0x02A0E03C: adrp     x1, #0x1154000
0x02A0E040: add      x1, x1, #0xb1
0x02A0E044: ldr      x0, [x8, #0xf48]
0x02A0E048: ldr      x8, [x20, #0x780]
0x02A0E04C: str      xzr, [x0, #8]
0x02A0E050: blr      x8
0x02A0E054: adrp     x8, #0x50b6000
0x02A0E058: adrp     x1, #0x1146000
0x02A0E05C: add      x1, x1, #0xfb4
0x02A0E060: ldr      x0, [x8, #0xf40]
0x02A0E064: ldr      x8, [x20, #0x780]
0x02A0E068: str      xzr, [x0, #8]
0x02A0E06C: blr      x8
0x02A0E070: adrp     x1, #0x1194000
0x02A0E074: ldr      x8, [x20, #0x780]
0x02A0E078: add      x0, x19, #0x70
0x02A0E07C: add      x1, x1, #0x857
0x02A0E080: str      xzr, [x19, #0x78]
0x02A0E084: blr      x8
0x02A0E088: adrp     x8, #0x50b7000
0x02A0E08C: adrp     x1, #0x1187000
0x02A0E090: add      x1, x1, #0xc7b
0x02A0E094: ldr      x0, [x8, #0x30]
0x02A0E098: ldr      x8, [x20, #0x780]
0x02A0E09C: str      xzr, [x0, #8]
0x02A0E0A0: blr      x8
0x02A0E0A4: adrp     x8, #0x50b6000
0x02A0E0A8: adrp     x1, #0x11d4000
0x02A0E0AC: add      x1, x1, #0xc9
0x02A0E0B0: ldr      x0, [x8, #0xe40]
0x02A0E0B4: ldr      x8, [x20, #0x780]
0x02A0E0B8: str      xzr, [x0, #8]
0x02A0E0BC: blr      x8
0x02A0E0C0: adrp     x8, #0x50b7000
0x02A0E0C4: adrp     x1, #0x11da000
0x02A0E0C8: add      x1, x1, #0xd02
0x02A0E0CC: ldr      x0, [x8, #0x40]
0x02A0E0D0: ldr      x8, [x20, #0x780]
0x02A0E0D4: str      xzr, [x0, #8]
0x02A0E0D8: blr      x8
0x02A0E0DC: adrp     x8, #0x50b6000
0x02A0E0E0: adrp     x1, #0x1161000
0x02A0E0E4: add      x1, x1, #0x625
0x02A0E0E8: ldr      x0, [x8, #0xe18]
0x02A0E0EC: ldr      x8, [x20, #0x780]
0x02A0E0F0: str      xzr, [x0, #8]
0x02A0E0F4: blr      x8
0x02A0E0F8: adrp     x21, #0x50b6000
0x02A0E0FC: adrp     x1, #0x11fb000
0x02A0E100: ldr      x8, [x20, #0x780]
0x02A0E104: add      x1, x1, #0xdc8
0x02A0E108: ldr      x0, [x21, #0xe30]
0x02A0E10C: str      xzr, [x0, #8]
0x02A0E110: blr      x8
0x02A0E114: adrp     x8, #0x50b6000
0x02A0E118: adrp     x1, #0x1146000
0x02A0E11C: add      x1, x1, #0xfc1
0x02A0E120: ldr      x0, [x8, #0xfd8]
0x02A0E124: ldr      x8, [x20, #0x780]
0x02A0E128: str      xzr, [x0, #8]
0x02A0E12C: blr      x8
0x02A0E130: adrp     x8, #0x50b6000
0x02A0E134: adrp     x1, #0x1208000
0x02A0E138: add      x1, x1, #0xcf9
0x02A0E13C: ldr      x0, [x8, #0xff0]
0x02A0E140: ldr      x8, [x20, #0x780]
0x02A0E144: str      xzr, [x0, #8]
0x02A0E148: blr      x8
0x02A0E14C: adrp     x8, #0x50b6000
0x02A0E150: adrp     x1, #0x1194000
0x02A0E154: add      x1, x1, #0x824
0x02A0E158: ldr      x0, [x8, #0xf28]
0x02A0E15C: ldr      x8, [x20, #0x780]
0x02A0E160: str      xzr, [x0, #8]
0x02A0E164: blr      x8
0x02A0E168: adrp     x8, #0x50b6000
0x02A0E16C: adrp     x1, #0x11b4000
0x02A0E170: add      x1, x1, #0xaa1
0x02A0E174: ldr      x0, [x8, #0xfe8]
0x02A0E178: ldr      x8, [x20, #0x780]
0x02A0E17C: str      xzr, [x0, #8]
0x02A0E180: blr      x8
0x02A0E184: adrp     x8, #0x50b7000
0x02A0E188: adrp     x1, #0x1154000
0x02A0E18C: add      x1, x1, #0x2f2
0x02A0E190: ldr      x0, [x8, #8]
0x02A0E194: ldr      x8, [x20, #0x780]
0x02A0E198: str      xzr, [x0, #8]
0x02A0E19C: blr      x8
0x02A0E1A0: adrp     x8, #0x50b6000
0x02A0E1A4: adrp     x1, #0x11fb000
0x02A0E1A8: add      x1, x1, #0xdde
0x02A0E1AC: ldr      x0, [x8, #0xd08]
0x02A0E1B0: ldr      x8, [x20, #0x780]
0x02A0E1B4: str      xzr, [x0, #8]
0x02A0E1B8: blr      x8
0x02A0E1BC: adrp     x8, #0x50b6000
0x02A0E1C0: adrp     x1, #0x117a000
0x02A0E1C4: add      x1, x1, #0xfae
0x02A0E1C8: ldr      x0, [x8, #0xf60]
0x02A0E1CC: ldr      x8, [x20, #0x780]
0x02A0E1D0: str      xzr, [x0, #8]
0x02A0E1D4: blr      x8
0x02A0E1D8: adrp     x1, #0x11cd000
0x02A0E1DC: ldr      x0, [x21, #0xe30]
0x02A0E1E0: ldr      x8, [x20, #0x780]
0x02A0E1E4: add      x1, x1, #0x6e8
0x02A0E1E8: str      xzr, [x0, #8]
0x02A0E1EC: blr      x8
0x02A0E1F0: adrp     x8, #0x50b6000
0x02A0E1F4: adrp     x1, #0x11e7000
0x02A0E1F8: add      x1, x1, #0x9f1
0x02A0E1FC: ldr      x0, [x8, #0xfd0]
0x02A0E200: ldr      x8, [x20, #0x780]
0x02A0E204: str      xzr, [x0, #8]
0x02A0E208: blr      x8
0x02A0E20C: adrp     x8, #0x50b6000
0x02A0E210: adrp     x1, #0x1140000
0x02A0E214: add      x1, x1, #0xb91
0x02A0E218: ldr      x0, [x8, #0xd00]
0x02A0E21C: ldr      x8, [x20, #0x780]
0x02A0E220: str      xzr, [x0, #8]
0x02A0E224: blr      x8
0x02A0E228: adrp     x8, #0x50b6000
0x02A0E22C: adrp     x1, #0x11e1000
0x02A0E230: add      x1, x1, #0x337
0x02A0E234: ldr      x0, [x8, #0xe00]
0x02A0E238: ldr      x8, [x20, #0x780]
0x02A0E23C: str      xzr, [x0, #8]
0x02A0E240: blr      x8
0x02A0E244: adrp     x8, #0x50b6000
0x02A0E248: adrp     x1, #0x116d000
0x02A0E24C: add      x1, x1, #0xd94
0x02A0E250: ldr      x0, [x8, #0xf58]
0x02A0E254: ldr      x8, [x20, #0x780]
0x02A0E258: str      xzr, [x0, #8]
0x02A0E25C: blr      x8
0x02A0E260: adrp     x8, #0x50b6000
0x02A0E264: adrp     x1, #0x1174000
0x02A0E268: add      x1, x1, #0x95c
0x02A0E26C: ldr      x0, [x8, #0xcf8]
0x02A0E270: ldr      x8, [x20, #0x780]
0x02A0E274: str      xzr, [x0, #8]
0x02A0E278: blr      x8
0x02A0E27C: adrp     x1, #0x1167000
0x02A0E280: ldr      x8, [x20, #0x780]
0x02A0E284: add      x0, x19, #0x190
0x02A0E288: add      x1, x1, #0x956
0x02A0E28C: str      xzr, [x19, #0x198]
0x02A0E290: blr      x8
0x02A0E294: adrp     x8, #0x50b6000
0x02A0E298: adrp     x1, #0x119a000
0x02A0E29C: add      x1, x1, #0x5ae
0x02A0E2A0: ldr      x0, [x8, #0xf98]
0x02A0E2A4: ldr      x8, [x20, #0x780]
0x02A0E2A8: str      xzr, [x0, #8]
0x02A0E2AC: blr      x8
0x02A0E2B0: adrp     x8, #0x50b6000
0x02A0E2B4: adrp     x1, #0x11da000
0x02A0E2B8: add      x1, x1, #0xd13
0x02A0E2BC: ldr      x0, [x8, #0xdf0]
0x02A0E2C0: ldr      x8, [x20, #0x780]
0x02A0E2C4: str      xzr, [x0, #8]
0x02A0E2C8: blr      x8
0x02A0E2CC: adrp     x8, #0x50b6000
0x02A0E2D0: adrp     x1, #0x1194000
0x02A0E2D4: add      x1, x1, #0x868
0x02A0E2D8: ldr      x0, [x8, #0xdf8]
0x02A0E2DC: ldr      x8, [x20, #0x780]
0x02A0E2E0: str      xzr, [x0, #8]
0x02A0E2E4: blr      x8
0x02A0E2E8: adrp     x8, #0x50b7000
0x02A0E2EC: adrp     x1, #0x11d4000
0x02A0E2F0: add      x1, x1, #0xd8
0x02A0E2F4: ldr      x0, [x8, #0x38]
0x02A0E2F8: ldr      x8, [x20, #0x780]
0x02A0E2FC: str      xzr, [x0, #8]
0x02A0E300: blr      x8
0x02A0E304: adrp     x8, #0x50b7000
~~~

### Function start 0x2a2c668
Hits: [{"pc": "0x2a2cb78", "adrp": "0x2a2cb70", "target": "0x11c0f57", "label": "invisible_range: ", "keywords": ["invisible"], "fde_start": "0x2a2c668", "fde_end": "0x2a2cbe8", "kind": "add", "reg": "x1"}]
~~~asm
0x02A2C668: str      x30, [sp, #-0x40]!
0x02A2C66C: stp      x24, x23, [sp, #0x10]
0x02A2C670: stp      x22, x21, [sp, #0x20]
0x02A2C674: stp      x20, x19, [sp, #0x30]
0x02A2C678: adrp     x22, #0x50b8000
0x02A2C67C: mov      x20, x1
0x02A2C680: adrp     x1, #0x11a8000
0x02A2C684: mov      x19, x0
0x02A2C688: add      x1, x1, #0x3d4
0x02A2C68C: ldr      x8, [x22, #0x1f0]
0x02A2C690: blr      x8
0x02A2C694: adrp     x21, #0x11cb000
0x02A2C698: ldr      x8, [x22, #0x1f0]
0x02A2C69C: add      x21, x21, #0x88d
0x02A2C6A0: mov      x0, x19
0x02A2C6A4: mov      x1, x21
0x02A2C6A8: blr      x8
0x02A2C6AC: adrp     x1, #0x1161000
0x02A2C6B0: ldr      x8, [x22, #0x1f0]
0x02A2C6B4: add      x1, x1, #0x690
0x02A2C6B8: mov      x0, x19
0x02A2C6BC: blr      x8
0x02A2C6C0: adrp     x23, #0x50b8000
0x02A2C6C4: add      x1, x20, #4
0x02A2C6C8: mov      x0, x19
0x02A2C6CC: ldr      x8, [x23, #0x4f8]
0x02A2C6D0: blr      x8
0x02A2C6D4: ldr      x8, [x22, #0x1f0]
0x02A2C6D8: mov      x0, x19
0x02A2C6DC: mov      x1, x21
0x02A2C6E0: blr      x8
0x02A2C6E4: adrp     x1, #0x114e000
0x02A2C6E8: ldr      x8, [x22, #0x1f0]
0x02A2C6EC: add      x1, x1, #0xf4
0x02A2C6F0: mov      x0, x19
0x02A2C6F4: blr      x8
0x02A2C6F8: add      x1, x20, #8
0x02A2C6FC: ldr      x8, [x23, #0x4f8]
0x02A2C700: mov      x0, x19
0x02A2C704: blr      x8
0x02A2C708: ldr      x8, [x22, #0x1f0]
0x02A2C70C: mov      x0, x19
0x02A2C710: mov      x1, x21
0x02A2C714: blr      x8
0x02A2C718: adrp     x1, #0x118e000
0x02A2C71C: ldr      x8, [x22, #0x1f0]
0x02A2C720: add      x1, x1, #0x93f
0x02A2C724: mov      x0, x19
0x02A2C728: blr      x8
0x02A2C72C: add      x1, x20, #0xc
0x02A2C730: ldr      x8, [x23, #0x4f8]
0x02A2C734: mov      x0, x19
0x02A2C738: blr      x8
0x02A2C73C: ldr      x8, [x22, #0x1f0]
0x02A2C740: mov      x0, x19
0x02A2C744: mov      x1, x21
0x02A2C748: blr      x8
0x02A2C74C: adrp     x1, #0x11fb000
0x02A2C750: ldr      x8, [x22, #0x1f0]
0x02A2C754: add      x1, x1, #0xe17
0x02A2C758: mov      x0, x19
0x02A2C75C: blr      x8
0x02A2C760: adrp     x24, #0x50b8000
0x02A2C764: add      x1, x20, #0x10
0x02A2C768: mov      x0, x19
0x02A2C76C: ldr      x8, [x24, #0x538]
0x02A2C770: blr      x8
0x02A2C774: ldr      x8, [x22, #0x1f0]
0x02A2C778: mov      x0, x19
0x02A2C77C: mov      x1, x21
0x02A2C780: blr      x8
0x02A2C784: adrp     x1, #0x1140000
0x02A2C788: ldr      x8, [x22, #0x1f0]
0x02A2C78C: add      x1, x1, #0xbc6
0x02A2C790: mov      x0, x19
0x02A2C794: blr      x8
0x02A2C798: add      x1, x20, #0x14
0x02A2C79C: ldr      x8, [x23, #0x4f8]
0x02A2C7A0: mov      x0, x19
0x02A2C7A4: blr      x8
0x02A2C7A8: ldr      x8, [x22, #0x1f0]
0x02A2C7AC: mov      x0, x19
0x02A2C7B0: mov      x1, x21
0x02A2C7B4: blr      x8
0x02A2C7B8: adrp     x1, #0x117b000
0x02A2C7BC: ldr      x8, [x22, #0x1f0]
0x02A2C7C0: add      x1, x1, #0x25
0x02A2C7C4: mov      x0, x19
0x02A2C7C8: blr      x8
0x02A2C7CC: add      x1, x20, #0x18
0x02A2C7D0: ldr      x8, [x23, #0x4f8]
0x02A2C7D4: mov      x0, x19
0x02A2C7D8: blr      x8
0x02A2C7DC: ldr      x8, [x22, #0x1f0]
0x02A2C7E0: mov      x0, x19
0x02A2C7E4: mov      x1, x21
0x02A2C7E8: blr      x8
0x02A2C7EC: adrp     x1, #0x11a8000
0x02A2C7F0: ldr      x8, [x22, #0x1f0]
0x02A2C7F4: add      x1, x1, #0x3e9
0x02A2C7F8: mov      x0, x19
0x02A2C7FC: blr      x8
0x02A2C800: add      x1, x20, #0x1c
0x02A2C804: ldr      x8, [x24, #0x538]
0x02A2C808: mov      x0, x19
0x02A2C80C: blr      x8
0x02A2C810: ldr      x8, [x22, #0x1f0]
0x02A2C814: mov      x0, x19
0x02A2C818: mov      x1, x21
0x02A2C81C: blr      x8
0x02A2C820: adrp     x1, #0x114e000
0x02A2C824: ldr      x8, [x22, #0x1f0]
0x02A2C828: add      x1, x1, #0x103
0x02A2C82C: mov      x0, x19
0x02A2C830: blr      x8
0x02A2C834: add      x1, x20, #0x20
0x02A2C838: ldr      x8, [x24, #0x538]
0x02A2C83C: mov      x0, x19
0x02A2C840: blr      x8
0x02A2C844: ldr      x8, [x22, #0x1f0]
0x02A2C848: mov      x0, x19
0x02A2C84C: mov      x1, x21
0x02A2C850: blr      x8
0x02A2C854: adrp     x1, #0x1187000
0x02A2C858: ldr      x8, [x22, #0x1f0]
0x02A2C85C: add      x1, x1, #0xcc4
0x02A2C860: mov      x0, x19
0x02A2C864: blr      x8
0x02A2C868: add      x1, x20, #0x24
0x02A2C86C: ldr      x8, [x24, #0x538]
0x02A2C870: mov      x0, x19
0x02A2C874: blr      x8
0x02A2C878: ldr      x8, [x22, #0x1f0]
0x02A2C87C: mov      x0, x19
0x02A2C880: mov      x1, x21
0x02A2C884: blr      x8
0x02A2C888: adrp     x1, #0x1181000
0x02A2C88C: ldr      x8, [x22, #0x1f0]
0x02A2C890: add      x1, x1, #0x24f
0x02A2C894: mov      x0, x19
0x02A2C898: blr      x8
0x02A2C89C: add      x1, x20, #0x28
0x02A2C8A0: ldr      x8, [x24, #0x538]
0x02A2C8A4: mov      x0, x19
0x02A2C8A8: blr      x8
0x02A2C8AC: ldr      x8, [x22, #0x1f0]
0x02A2C8B0: mov      x0, x19
0x02A2C8B4: mov      x1, x21
0x02A2C8B8: blr      x8
0x02A2C8BC: adrp     x1, #0x11ba000
0x02A2C8C0: ldr      x8, [x22, #0x1f0]
0x02A2C8C4: add      x1, x1, #0xad9
0x02A2C8C8: mov      x0, x19
0x02A2C8CC: blr      x8
0x02A2C8D0: add      x1, x20, #0x2c
0x02A2C8D4: ldr      x8, [x23, #0x4f8]
0x02A2C8D8: mov      x0, x19
0x02A2C8DC: blr      x8
0x02A2C8E0: ldr      x8, [x22, #0x1f0]
0x02A2C8E4: mov      x0, x19
0x02A2C8E8: mov      x1, x21
0x02A2C8EC: blr      x8
0x02A2C8F0: adrp     x1, #0x1194000
0x02A2C8F4: ldr      x8, [x22, #0x1f0]
0x02A2C8F8: add      x1, x1, #0x916
0x02A2C8FC: mov      x0, x19
0x02A2C900: blr      x8
0x02A2C904: add      x1, x20, #0x30
0x02A2C908: ldr      x8, [x24, #0x538]
0x02A2C90C: mov      x0, x19
0x02A2C910: blr      x8
0x02A2C914: ldr      x8, [x22, #0x1f0]
0x02A2C918: mov      x0, x19
0x02A2C91C: mov      x1, x21
0x02A2C920: blr      x8
0x02A2C924: adrp     x1, #0x114e000
0x02A2C928: ldr      x8, [x22, #0x1f0]
0x02A2C92C: add      x1, x1, #0x11d
0x02A2C930: mov      x0, x19
0x02A2C934: blr      x8
0x02A2C938: add      x1, x20, #0x34
0x02A2C93C: ldr      x8, [x23, #0x4f8]
0x02A2C940: mov      x0, x19
0x02A2C944: blr      x8
0x02A2C948: ldr      x8, [x22, #0x1f0]
0x02A2C94C: mov      x0, x19
0x02A2C950: mov      x1, x21
0x02A2C954: blr      x8
0x02A2C958: adrp     x1, #0x11e7000
0x02A2C95C: ldr      x8, [x22, #0x1f0]
0x02A2C960: add      x1, x1, #0xa65
0x02A2C964: mov      x0, x19
0x02A2C968: blr      x8
0x02A2C96C: add      x1, x20, #0x38
0x02A2C970: ldr      x8, [x23, #0x4f8]
0x02A2C974: mov      x0, x19
0x02A2C978: blr      x8
0x02A2C97C: ldr      x8, [x22, #0x1f0]
0x02A2C980: mov      x0, x19
0x02A2C984: mov      x1, x21
0x02A2C988: blr      x8
0x02A2C98C: adrp     x1, #0x11b4000
0x02A2C990: ldr      x8, [x22, #0x1f0]
0x02A2C994: add      x1, x1, #0xad9
0x02A2C998: mov      x0, x19
0x02A2C99C: blr      x8
0x02A2C9A0: add      x1, x20, #0x3c
0x02A2C9A4: ldr      x8, [x23, #0x4f8]
0x02A2C9A8: mov      x0, x19
0x02A2C9AC: blr      x8
0x02A2C9B0: ldr      x8, [x22, #0x1f0]
0x02A2C9B4: mov      x0, x19
0x02A2C9B8: mov      x1, x21
0x02A2C9BC: blr      x8
0x02A2C9C0: adrp     x1, #0x11c7000
0x02A2C9C4: ldr      x8, [x22, #0x1f0]
0x02A2C9C8: add      x1, x1, #0x1f5
0x02A2C9CC: mov      x0, x19
0x02A2C9D0: blr      x8
0x02A2C9D4: add      x1, x20, #0x40
0x02A2C9D8: ldr      x8, [x23, #0x4f8]
0x02A2C9DC: mov      x0, x19
0x02A2C9E0: blr      x8
0x02A2C9E4: ldr      x8, [x22, #0x1f0]
0x02A2C9E8: mov      x0, x19
0x02A2C9EC: mov      x1, x21
0x02A2C9F0: blr      x8
0x02A2C9F4: adrp     x1, #0x11a0000
0x02A2C9F8: ldr      x8, [x22, #0x1f0]
0x02A2C9FC: add      x1, x1, #0xfe5
0x02A2CA00: mov      x0, x19
0x02A2CA04: blr      x8
0x02A2CA08: ldrb     w8, [x20, #0x48]
0x02A2CA0C: add      x10, x20, #0x49
0x02A2CA10: ldr      x9, [x20, #0x58]
0x02A2CA14: mov      x0, x19
0x02A2CA18: tst      w8, #1
0x02A2CA1C: ldr      x8, [x22, #0x1f0]
0x02A2CA20: csel     x1, x10, x9, eq
0x02A2CA24: blr      x8
~~~

### Function start 0x2c46f8c
Hits: [{"pc": "0x2c46fc0", "adrp": "0x2c46fb8", "target": "0x11dadbe", "label": "USGActorRoot", "keywords": ["ActorRoot"], "fde_start": "0x2c46f8c", "fde_end": "0x2c47028", "kind": "add", "reg": "x1"}]
~~~asm
0x02C46F8C: str      x30, [sp, #-0x20]!
0x02C46F90: stp      x20, x19, [sp, #0x10]
0x02C46F94: adrp     x20, #0x53ec000
0x02C46F98: ldr      x0, [x20, #0x478]
0x02C46F9C: cbnz     x0, #0x2c4701c
0x02C46FA0: mov      w0, #0x168
0x02C46FA4: bl       #0x4b40050
0x02C46FA8: adrp     x8, #0x5040000
0x02C46FAC: mov      x19, x0
0x02C46FB0: ldr      x8, [x8, #0x20]
0x02C46FB4: cbz      x8, #0x2c46fd4
0x02C46FB8: adrp     x1, #0x11da000
0x02C46FBC: mov      x0, x19
0x02C46FC0: add      x1, x1, #0xdbe
0x02C46FC4: mov      x2, xzr
0x02C46FC8: mov      x3, xzr
0x02C46FCC: mov      w4, #0x100
0x02C46FD0: blr      x8
0x02C46FD4: adrp     x8, #0x5002000
0x02C46FD8: adrp     x9, #0x50ce000
0x02C46FDC: str      x19, [x20, #0x478]
0x02C46FE0: ldr      x8, [x8, #0x850]
0x02C46FE4: ldr      x9, [x9]
0x02C46FE8: str      x8, [x19, #0x160]
0x02C46FEC: blr      x9
0x02C46FF0: ldr      x8, [x19]
0x02C46FF4: mov      x1, x0
0x02C46FF8: mov      x0, x19
0x02C46FFC: mov      w2, wzr
0x02C47000: ldr      x8, [x8, #0x10]
0x02C47004: blr      x8
0x02C47008: ldr      x8, [x19]
0x02C4700C: mov      x0, x19
0x02C47010: ldr      x8, [x8, #0x18]
0x02C47014: blr      x8
0x02C47018: ldr      x0, [x20, #0x478]
0x02C4701C: ldp      x20, x19, [sp, #0x10]
0x02C47020: ldr      x30, [sp], #0x20
0x02C47024: ret      
~~~

### Function start 0x2cf4f00
Hits: [{"pc": "0x2cf5100", "adrp": "0x2cf50fc", "target": "0x11a11c8", "label": "TraverseVInt3Array", "keywords": ["VInt3"], "fde_start": "0x2cf4f00", "fde_end": "0x2cf5e10", "kind": "add", "reg": "x1"}, {"pc": "0x2cf5550", "adrp": "0x2cf5548", "target": "0x11a5472", "label": "VInt3", "keywords": ["VInt3"], "fde_start": "0x2cf4f00", "fde_end": "0x2cf5e10", "kind": "add", "reg": "x1"}, {"pc": "0x2cf55b4", "adrp": "0x2cf55ac", "target": "0x1187de3", "label": "VInt3Array", "keywords": ["VInt3"], "fde_start": "0x2cf4f00", "fde_end": "0x2cf5e10", "kind": "add", "reg": "x1"}]
~~~asm
0x02CF4F00: sub      sp, sp, #0x140
0x02CF4F04: stp      x29, x30, [sp, #0x100]
0x02CF4F08: stp      x24, x23, [sp, #0x110]
0x02CF4F0C: stp      x22, x21, [sp, #0x120]
0x02CF4F10: stp      x20, x19, [sp, #0x130]
0x02CF4F14: adrp     x20, #0x5219000
0x02CF4F18: mov      x19, x0
0x02CF4F1C: ldr      x0, [x0, #0x10]
0x02CF4F20: add      x8, sp, #0x10
0x02CF4F24: ldr      x9, [x20, #0xb60]
0x02CF4F28: blr      x9
0x02CF4F2C: adrp     x21, #0x5219000
0x02CF4F30: ldr      x9, [x21, #0xb68]
0x02CF4F34: adrp     x1, #0x119a000
0x02CF4F38: add      x8, sp, #0x20
0x02CF4F3C: add      x1, x1, #0x759
0x02CF4F40: add      x0, sp, #0x10
0x02CF4F44: blr      x9
0x02CF4F48: adrp     x8, #0x5015000
0x02CF4F4C: adrp     x9, #0x521a000
0x02CF4F50: ldr      x2, [x8, #0x2c0]
0x02CF4F54: ldr      x8, [x9, #0x258]
0x02CF4F58: adrp     x1, #0x11d4000
0x02CF4F5C: add      x0, sp, #0x20
0x02CF4F60: add      x1, x1, #0x2ce
0x02CF4F64: blr      x8
0x02CF4F68: adrp     x8, #0x5015000
0x02CF4F6C: adrp     x9, #0x521a000
0x02CF4F70: ldr      x2, [x8, #0x2c8]
0x02CF4F74: ldr      x8, [x9, #0x268]
0x02CF4F78: adrp     x1, #0x1140000
0x02CF4F7C: add      x1, x1, #0xd38
0x02CF4F80: blr      x8
0x02CF4F84: adrp     x8, #0x5015000
0x02CF4F88: adrp     x9, #0x521a000
0x02CF4F8C: ldr      x2, [x8, #0x2d8]
0x02CF4F90: ldr      x8, [x9, #0x278]
0x02CF4F94: adrp     x1, #0x11a1000
0x02CF4F98: add      x1, x1, #0x1bd
0x02CF4F9C: blr      x8
0x02CF4FA0: adrp     x8, #0x5015000
0x02CF4FA4: adrp     x9, #0x521a000
0x02CF4FA8: ldr      x2, [x8, #0x2d0]
0x02CF4FAC: ldr      x8, [x9, #0x288]
0x02CF4FB0: adrp     x1, #0x11f5000
0x02CF4FB4: add      x1, x1, #0x802
0x02CF4FB8: blr      x8
0x02CF4FBC: adrp     x8, #0x5015000
0x02CF4FC0: adrp     x9, #0x521a000
0x02CF4FC4: ldr      x2, [x8, #0x2b0]
0x02CF4FC8: ldr      x8, [x9, #0x298]
0x02CF4FCC: adrp     x1, #0x1161000
0x02CF4FD0: add      x1, x1, #0x714
0x02CF4FD4: blr      x8
0x02CF4FD8: adrp     x8, #0x5015000
0x02CF4FDC: adrp     x9, #0x5219000
0x02CF4FE0: ldr      x2, [x8, #0x2b8]
0x02CF4FE4: ldr      x8, [x9, #0xcb8]
0x02CF4FE8: adrp     x1, #0x119a000
0x02CF4FEC: add      x1, x1, #0x75c
0x02CF4FF0: blr      x8
0x02CF4FF4: adrp     x8, #0x5015000
0x02CF4FF8: adrp     x22, #0x521a000
0x02CF4FFC: ldr      x2, [x8, #0x3e8]
0x02CF5000: b        #0x4b3f67c
0x02CF5004: adrp     x1, #0x118e000
0x02CF5008: add      x1, x1, #0xa3d
0x02CF500C: blr      x8
0x02CF5010: adrp     x8, #0x5015000
0x02CF5014: adrp     x9, #0x521a000
0x02CF5018: ldr      x2, [x8, #0x2e0]
0x02CF501C: ldr      x8, [x9, #0x2b8]
0x02CF5020: adrp     x1, #0x1187000
0x02CF5024: add      x1, x1, #0xdd2
0x02CF5028: blr      x8
0x02CF502C: adrp     x8, #0x5015000
0x02CF5030: adrp     x23, #0x521a000
0x02CF5034: ldr      x2, [x8, #0x2e8]
0x02CF5038: ldr      x8, [x23, #0x2c8]
0x02CF503C: adrp     x1, #0x1181000
0x02CF5040: add      x1, x1, #0x30a
0x02CF5044: blr      x8
0x02CF5048: adrp     x8, #0x5015000
0x02CF504C: ldr      x2, [x8, #0x2f0]
0x02CF5050: ldr      x8, [x23, #0x2c8]
0x02CF5054: adrp     x1, #0x114e000
0x02CF5058: add      x1, x1, #0x24a
0x02CF505C: blr      x8
0x02CF5060: adrp     x8, #0x5015000
0x02CF5064: adrp     x9, #0x521a000
0x02CF5068: ldr      x2, [x8, #0x2f8]
0x02CF506C: ldr      x8, [x9, #0x2d8]
0x02CF5070: adrp     x1, #0x1167000
0x02CF5074: add      x1, x1, #0xb3b
0x02CF5078: blr      x8
0x02CF507C: adrp     x8, #0x5015000
0x02CF5080: adrp     x9, #0x521a000
0x02CF5084: ldr      x2, [x8, #0x370]
0x02CF5088: ldr      x8, [x9, #0x2e8]
0x02CF508C: adrp     x1, #0x11e1000
0x02CF5090: add      x1, x1, #0x514
0x02CF5094: blr      x8
0x02CF5098: adrp     x8, #0x5015000
0x02CF509C: adrp     x9, #0x521a000
0x02CF50A0: ldr      x2, [x8, #0x378]
0x02CF50A4: ldr      x8, [x9, #0x2f8]
0x02CF50A8: adrp     x1, #0x11ee000
0x02CF50AC: add      x1, x1, #0xd3e
0x02CF50B0: blr      x8
0x02CF50B4: adrp     x8, #0x5015000
0x02CF50B8: adrp     x9, #0x521a000
0x02CF50BC: ldr      x2, [x8, #0x380]
0x02CF50C0: ldr      x8, [x9, #0x308]
0x02CF50C4: adrp     x1, #0x11c7000
0x02CF50C8: add      x1, x1, #0x295
0x02CF50CC: blr      x8
0x02CF50D0: adrp     x8, #0x5015000
0x02CF50D4: adrp     x9, #0x521a000
0x02CF50D8: ldr      x2, [x8, #0x388]
0x02CF50DC: ldr      x8, [x9, #0x318]
0x02CF50E0: adrp     x1, #0x11f5000
0x02CF50E4: add      x1, x1, #0x810
0x02CF50E8: blr      x8
0x02CF50EC: adrp     x8, #0x5015000
0x02CF50F0: adrp     x9, #0x521a000
0x02CF50F4: ldr      x2, [x8, #0x390]
0x02CF50F8: ldr      x8, [x9, #0x328]
0x02CF50FC: adrp     x1, #0x11a1000
0x02CF5100: add      x1, x1, #0x1c8
0x02CF5104: blr      x8
0x02CF5108: adrp     x8, #0x5015000
0x02CF510C: adrp     x9, #0x521a000
0x02CF5110: ldr      x2, [x8, #0x360]
0x02CF5114: ldr      x8, [x9, #0x338]
0x02CF5118: adrp     x1, #0x11ee000
0x02CF511C: add      x1, x1, #0xd56
0x02CF5120: blr      x8
0x02CF5124: adrp     x8, #0x5015000
0x02CF5128: adrp     x9, #0x521a000
0x02CF512C: ldr      x2, [x8, #0x368]
0x02CF5130: ldr      x8, [x9, #0x348]
0x02CF5134: adrp     x1, #0x11c7000
0x02CF5138: add      x1, x1, #0x2a9
0x02CF513C: blr      x8
0x02CF5140: adrp     x8, #0x5015000
0x02CF5144: adrp     x9, #0x521a000
0x02CF5148: ldr      x2, [x8, #0x300]
0x02CF514C: ldr      x8, [x9, #0x358]
0x02CF5150: adrp     x1, #0x11fb000
0x02CF5154: add      x1, x1, #0xf42
0x02CF5158: blr      x8
0x02CF515C: adrp     x8, #0x5015000
0x02CF5160: adrp     x9, #0x521a000
0x02CF5164: ldr      x2, [x8, #0x308]
0x02CF5168: ldr      x8, [x9, #0x368]
0x02CF516C: adrp     x1, #0x11e1000
0x02CF5170: add      x1, x1, #0x527
0x02CF5174: blr      x8
0x02CF5178: adrp     x8, #0x5015000
0x02CF517C: adrp     x9, #0x521a000
0x02CF5180: ldr      x2, [x8, #0x358]
0x02CF5184: ldr      x8, [x9, #0x378]
0x02CF5188: adrp     x1, #0x1194000
0x02CF518C: add      x1, x1, #0xaa1
0x02CF5190: blr      x8
0x02CF5194: adrp     x8, #0x5015000
0x02CF5198: adrp     x9, #0x521a000
0x02CF519C: ldr      x2, [x8, #0x310]
0x02CF51A0: ldr      x8, [x9, #0x388]
0x02CF51A4: adrp     x1, #0x11b4000
0x02CF51A8: add      x1, x1, #0xc2e
0x02CF51AC: blr      x8
0x02CF51B0: adrp     x8, #0x5015000
0x02CF51B4: adrp     x9, #0x521a000
0x02CF51B8: ldr      x2, [x8, #0x318]
0x02CF51BC: ldr      x8, [x9, #0x398]
0x02CF51C0: adrp     x1, #0x1194000
0x02CF51C4: add      x1, x1, #0xab0
0x02CF51C8: blr      x8
0x02CF51CC: adrp     x8, #0x5015000
0x02CF51D0: adrp     x9, #0x521a000
0x02CF51D4: ldr      x2, [x8, #0x320]
0x02CF51D8: ldr      x8, [x9, #0x3a8]
0x02CF51DC: adrp     x1, #0x117b000
0x02CF51E0: add      x1, x1, #0x194
0x02CF51E4: blr      x8
0x02CF51E8: adrp     x8, #0x5015000
0x02CF51EC: adrp     x9, #0x521a000
0x02CF51F0: ldr      x2, [x8, #0x328]
0x02CF51F4: ldr      x8, [x9, #0x3b8]
0x02CF51F8: adrp     x1, #0x11e7000
0x02CF51FC: add      x1, x1, #0xb75
0x02CF5200: blr      x8
0x02CF5204: adrp     x8, #0x5015000
0x02CF5208: adrp     x9, #0x521a000
0x02CF520C: ldr      x2, [x8, #0x330]
0x02CF5210: ldr      x8, [x9, #0x3c8]
0x02CF5214: adrp     x1, #0x1154000
0x02CF5218: add      x1, x1, #0x457
0x02CF521C: blr      x8
0x02CF5220: adrp     x8, #0x5015000
0x02CF5224: adrp     x9, #0x521a000
0x02CF5228: ldr      x2, [x8, #0x338]
0x02CF522C: ldr      x8, [x9, #0x3d8]
0x02CF5230: adrp     x1, #0x11e1000
0x02CF5234: add      x1, x1, #0x54b
0x02CF5238: blr      x8
0x02CF523C: adrp     x8, #0x5015000
0x02CF5240: adrp     x9, #0x521a000
0x02CF5244: ldr      x2, [x8, #0x340]
0x02CF5248: ldr      x8, [x9, #0x3e8]
0x02CF524C: adrp     x1, #0x11c1000
0x02CF5250: add      x1, x1, #0x2d
0x02CF5254: blr      x8
0x02CF5258: adrp     x8, #0x5015000
0x02CF525C: adrp     x9, #0x521a000
0x02CF5260: ldr      x2, [x8, #0x348]
0x02CF5264: ldr      x8, [x9, #0x3f8]
0x02CF5268: adrp     x1, #0x11c1000
0x02CF526C: add      x1, x1, #0x44
0x02CF5270: blr      x8
0x02CF5274: adrp     x8, #0x5015000
0x02CF5278: adrp     x9, #0x521a000
0x02CF527C: ldr      x2, [x8, #0x350]
0x02CF5280: ldr      x8, [x9, #0x408]
0x02CF5284: adrp     x1, #0x1194000
0x02CF5288: add      x1, x1, #0xad3
0x02CF528C: blr      x8
0x02CF5290: ldr      x9, [x21, #0xb68]
0x02CF5294: adrp     x1, #0x115a000
0x02CF5298: add      x8, sp, #0x30
0x02CF529C: add      x1, x1, #0xc6e
0x02CF52A0: blr      x9
0x02CF52A4: adrp     x23, #0x521a000
0x02CF52A8: ldr      x8, [x23, #0x418]
0x02CF52AC: adrp     x1, #0x11c7000
0x02CF52B0: add      x0, sp, #0x30
0x02CF52B4: add      x1, x1, #0x2b2
0x02CF52B8: mov      w2, #0x98
0x02CF52BC: blr      x8
~~~

### Function start 0x2e71c1c
Hits: [{"pc": "0x2e71c50", "adrp": "0x2e71c48", "target": "0x11ae660", "label": "ActorPositionChangeEventNodeRuntime", "keywords": ["ActorPos"], "fde_start": "0x2e71c1c", "fde_end": "0x2e71cb8", "kind": "add", "reg": "x1"}]
~~~asm
0x02E71C1C: str      x30, [sp, #-0x20]!
0x02E71C20: stp      x20, x19, [sp, #0x10]
0x02E71C24: adrp     x20, #0x53e8000
0x02E71C28: ldr      x0, [x20, #0x358]
0x02E71C2C: cbnz     x0, #0x2e71cac
0x02E71C30: mov      w0, #0x168
0x02E71C34: bl       #0x4b40050
0x02E71C38: adrp     x8, #0x5040000
0x02E71C3C: mov      x19, x0
0x02E71C40: ldr      x8, [x8, #0x20]
0x02E71C44: cbz      x8, #0x2e71c64
0x02E71C48: adrp     x1, #0x11ae000
0x02E71C4C: mov      x0, x19
0x02E71C50: add      x1, x1, #0x660
0x02E71C54: mov      x2, xzr
0x02E71C58: mov      x3, xzr
0x02E71C5C: mov      w4, #0x38
0x02E71C60: blr      x8
0x02E71C64: adrp     x8, #0x5000000
0x02E71C68: adrp     x9, #0x50eb000
0x02E71C6C: str      x19, [x20, #0x358]
0x02E71C70: ldr      x8, [x8, #0x960]
0x02E71C74: ldr      x9, [x9, #0x350]
0x02E71C78: str      x8, [x19, #0x160]
0x02E71C7C: blr      x9
0x02E71C80: ldr      x8, [x19]
0x02E71C84: mov      x1, x0
0x02E71C88: mov      x0, x19
0x02E71C8C: mov      w2, wzr
0x02E71C90: ldr      x8, [x8, #0x10]
0x02E71C94: blr      x8
0x02E71C98: ldr      x8, [x19]
0x02E71C9C: mov      x0, x19
0x02E71CA0: ldr      x8, [x8, #0x18]
0x02E71CA4: blr      x8
0x02E71CA8: ldr      x0, [x20, #0x358]
0x02E71CAC: ldp      x20, x19, [sp, #0x10]
0x02E71CB0: ldr      x30, [sp], #0x20
0x02E71CB4: ret      
~~~

### Function start 0x2e83b6c
Hits: [{"pc": "0x2e83ba0", "adrp": "0x2e83b98", "target": "0x119a990", "label": "ActorPositionChangeListenerNodeRuntime", "keywords": ["ActorPos"], "fde_start": "0x2e83b6c", "fde_end": "0x2e83c08", "kind": "add", "reg": "x1"}]
~~~asm
0x02E83B6C: str      x30, [sp, #-0x20]!
0x02E83B70: stp      x20, x19, [sp, #0x10]
0x02E83B74: adrp     x20, #0x53e8000
0x02E83B78: ldr      x0, [x20, #0x188]
0x02E83B7C: cbnz     x0, #0x2e83bfc
0x02E83B80: mov      w0, #0x168
0x02E83B84: bl       #0x4b40050
0x02E83B88: adrp     x8, #0x5040000
0x02E83B8C: mov      x19, x0
0x02E83B90: ldr      x8, [x8, #0x20]
0x02E83B94: cbz      x8, #0x2e83bb4
0x02E83B98: adrp     x1, #0x119a000
0x02E83B9C: mov      x0, x19
0x02E83BA0: add      x1, x1, #0x990
0x02E83BA4: mov      x2, xzr
0x02E83BA8: mov      x3, xzr
0x02E83BAC: mov      w4, #0x38
0x02E83BB0: blr      x8
0x02E83BB4: adrp     x8, #0x5000000
0x02E83BB8: adrp     x9, #0x50eb000
0x02E83BBC: str      x19, [x20, #0x188]
0x02E83BC0: ldr      x8, [x8, #0x790]
0x02E83BC4: ldr      x9, [x9, #0x350]
0x02E83BC8: str      x8, [x19, #0x160]
0x02E83BCC: blr      x9
0x02E83BD0: ldr      x8, [x19]
0x02E83BD4: mov      x1, x0
0x02E83BD8: mov      x0, x19
0x02E83BDC: mov      w2, wzr
0x02E83BE0: ldr      x8, [x8, #0x10]
0x02E83BE4: blr      x8
0x02E83BE8: ldr      x8, [x19]
0x02E83BEC: mov      x0, x19
0x02E83BF0: ldr      x8, [x8, #0x18]
0x02E83BF4: blr      x8
0x02E83BF8: ldr      x0, [x20, #0x188]
0x02E83BFC: ldp      x20, x19, [sp, #0x10]
0x02E83C00: ldr      x30, [sp], #0x20
0x02E83C04: ret      
~~~

### Function start 0x2f39c14
Hits: [{"pc": "0x2f39c48", "adrp": "0x2f39c40", "target": "0x11d4497", "label": "GlobalVariableActorRootNodeRuntime", "keywords": ["ActorRoot"], "fde_start": "0x2f39c14", "fde_end": "0x2f39cb0", "kind": "add", "reg": "x1"}]
~~~asm
0x02F39C14: str      x30, [sp, #-0x20]!
0x02F39C18: stp      x20, x19, [sp, #0x10]
0x02F39C1C: adrp     x20, #0x53e7000
0x02F39C20: ldr      x0, [x20, #0xe28]
0x02F39C24: cbnz     x0, #0x2f39ca4
0x02F39C28: mov      w0, #0x168
0x02F39C2C: bl       #0x4b40050
0x02F39C30: adrp     x8, #0x5040000
0x02F39C34: mov      x19, x0
0x02F39C38: ldr      x8, [x8, #0x20]
0x02F39C3C: cbz      x8, #0x2f39c5c
0x02F39C40: adrp     x1, #0x11d4000
0x02F39C44: mov      x0, x19
0x02F39C48: add      x1, x1, #0x497
0x02F39C4C: mov      x2, xzr
0x02F39C50: mov      x3, xzr
0x02F39C54: mov      w4, #0x38
0x02F39C58: blr      x8
0x02F39C5C: adrp     x8, #0x5000000
0x02F39C60: adrp     x9, #0x50eb000
0x02F39C64: str      x19, [x20, #0xe28]
0x02F39C68: ldr      x8, [x8, #0x430]
0x02F39C6C: ldr      x9, [x9, #0x350]
0x02F39C70: str      x8, [x19, #0x160]
0x02F39C74: blr      x9
0x02F39C78: ldr      x8, [x19]
0x02F39C7C: mov      x1, x0
0x02F39C80: mov      x0, x19
0x02F39C84: mov      w2, wzr
0x02F39C88: ldr      x8, [x8, #0x10]
0x02F39C8C: blr      x8
0x02F39C90: ldr      x8, [x19]
0x02F39C94: mov      x0, x19
0x02F39C98: ldr      x8, [x8, #0x18]
0x02F39C9C: blr      x8
0x02F39CA0: ldr      x0, [x20, #0xe28]
0x02F39CA4: ldp      x20, x19, [sp, #0x10]
0x02F39CA8: ldr      x30, [sp], #0x20
0x02F39CAC: ret      
~~~

### Function start 0x2f3a950
Hits: [{"pc": "0x2f3a984", "adrp": "0x2f3a97c", "target": "0x12028c3", "label": "VInt3ConstantMapNodeRuntime", "keywords": ["VInt3"], "fde_start": "0x2f3a950", "fde_end": "0x2f3a9ec", "kind": "add", "reg": "x1"}]
~~~asm
0x02F3A950: str      x30, [sp, #-0x20]!
0x02F3A954: stp      x20, x19, [sp, #0x10]
0x02F3A958: adrp     x20, #0x53e7000
0x02F3A95C: ldr      x0, [x20, #0xdf8]
0x02F3A960: cbnz     x0, #0x2f3a9e0
0x02F3A964: mov      w0, #0x168
0x02F3A968: bl       #0x4b40050
0x02F3A96C: adrp     x8, #0x5040000
0x02F3A970: mov      x19, x0
0x02F3A974: ldr      x8, [x8, #0x20]
0x02F3A978: cbz      x8, #0x2f3a998
0x02F3A97C: adrp     x1, #0x1202000
0x02F3A980: mov      x0, x19
0x02F3A984: add      x1, x1, #0x8c3
0x02F3A988: mov      x2, xzr
0x02F3A98C: mov      x3, xzr
0x02F3A990: mov      w4, #0x58
0x02F3A994: blr      x8
0x02F3A998: adrp     x8, #0x5000000
0x02F3A99C: adrp     x9, #0x50eb000
0x02F3A9A0: str      x19, [x20, #0xdf8]
0x02F3A9A4: ldr      x8, [x8, #0x400]
0x02F3A9A8: ldr      x9, [x9, #0x350]
0x02F3A9AC: str      x8, [x19, #0x160]
0x02F3A9B0: blr      x9
0x02F3A9B4: ldr      x8, [x19]
0x02F3A9B8: mov      x1, x0
0x02F3A9BC: mov      x0, x19
0x02F3A9C0: mov      w2, wzr
0x02F3A9C4: ldr      x8, [x8, #0x10]
0x02F3A9C8: blr      x8
0x02F3A9CC: ldr      x8, [x19]
0x02F3A9D0: mov      x0, x19
0x02F3A9D4: ldr      x8, [x8, #0x18]
0x02F3A9D8: blr      x8
0x02F3A9DC: ldr      x0, [x20, #0xdf8]
0x02F3A9E0: ldp      x20, x19, [sp, #0x10]
0x02F3A9E4: ldr      x30, [sp], #0x20
0x02F3A9E8: ret      
~~~

### Function start 0x2f3ad98
Hits: [{"pc": "0x2f3adcc", "adrp": "0x2f3adc4", "target": "0x1161a0e", "label": "VInt3MapForeachLoopNodeRuntime", "keywords": ["VInt3"], "fde_start": "0x2f3ad98", "fde_end": "0x2f3ae34", "kind": "add", "reg": "x1"}]
~~~asm
0x02F3AD98: str      x30, [sp, #-0x20]!
0x02F3AD9C: stp      x20, x19, [sp, #0x10]
0x02F3ADA0: adrp     x20, #0x53e7000
0x02F3ADA4: ldr      x0, [x20, #0xdf0]
0x02F3ADA8: cbnz     x0, #0x2f3ae28
0x02F3ADAC: mov      w0, #0x168
0x02F3ADB0: bl       #0x4b40050
0x02F3ADB4: adrp     x8, #0x5040000
0x02F3ADB8: mov      x19, x0
0x02F3ADBC: ldr      x8, [x8, #0x20]
0x02F3ADC0: cbz      x8, #0x2f3ade0
0x02F3ADC4: adrp     x1, #0x1161000
0x02F3ADC8: mov      x0, x19
0x02F3ADCC: add      x1, x1, #0xa0e
0x02F3ADD0: mov      x2, xzr
0x02F3ADD4: mov      x3, xzr
0x02F3ADD8: mov      w4, #0x38
0x02F3ADDC: blr      x8
0x02F3ADE0: adrp     x8, #0x5000000
0x02F3ADE4: adrp     x9, #0x50eb000
0x02F3ADE8: str      x19, [x20, #0xdf0]
0x02F3ADEC: ldr      x8, [x8, #0x3f8]
0x02F3ADF0: ldr      x9, [x9, #0x350]
0x02F3ADF4: str      x8, [x19, #0x160]
0x02F3ADF8: blr      x9
0x02F3ADFC: ldr      x8, [x19]
0x02F3AE00: mov      x1, x0
0x02F3AE04: mov      x0, x19
0x02F3AE08: mov      w2, wzr
0x02F3AE0C: ldr      x8, [x8, #0x10]
0x02F3AE10: blr      x8
0x02F3AE14: ldr      x8, [x19]
0x02F3AE18: mov      x0, x19
0x02F3AE1C: ldr      x8, [x8, #0x18]
0x02F3AE20: blr      x8
0x02F3AE24: ldr      x0, [x20, #0xdf0]
0x02F3AE28: ldp      x20, x19, [sp, #0x10]
0x02F3AE2C: ldr      x30, [sp], #0x20
0x02F3AE30: ret      
~~~

### Function start 0x2f3b008
Hits: [{"pc": "0x2f3b03c", "adrp": "0x2f3b034", "target": "0x11815db", "label": "GlobalVariableVInt3MapNodeRuntime", "keywords": ["VInt3"], "fde_start": "0x2f3b008", "fde_end": "0x2f3b0a4", "kind": "add", "reg": "x1"}]
~~~asm
0x02F3B008: str      x30, [sp, #-0x20]!
0x02F3B00C: stp      x20, x19, [sp, #0x10]
0x02F3B010: adrp     x20, #0x53e7000
0x02F3B014: ldr      x0, [x20, #0xde8]
0x02F3B018: cbnz     x0, #0x2f3b098
0x02F3B01C: mov      w0, #0x168
0x02F3B020: bl       #0x4b40050
0x02F3B024: adrp     x8, #0x5040000
0x02F3B028: mov      x19, x0
0x02F3B02C: ldr      x8, [x8, #0x20]
0x02F3B030: cbz      x8, #0x2f3b050
0x02F3B034: adrp     x1, #0x1181000
0x02F3B038: mov      x0, x19
0x02F3B03C: add      x1, x1, #0x5db
0x02F3B040: mov      x2, xzr
0x02F3B044: mov      x3, xzr
0x02F3B048: mov      w4, #0x38
0x02F3B04C: blr      x8
0x02F3B050: adrp     x8, #0x5000000
0x02F3B054: adrp     x9, #0x50eb000
0x02F3B058: str      x19, [x20, #0xde8]
0x02F3B05C: ldr      x8, [x8, #0x3f0]
0x02F3B060: ldr      x9, [x9, #0x350]
0x02F3B064: str      x8, [x19, #0x160]
0x02F3B068: blr      x9
0x02F3B06C: ldr      x8, [x19]
0x02F3B070: mov      x1, x0
0x02F3B074: mov      x0, x19
0x02F3B078: mov      w2, wzr
0x02F3B07C: ldr      x8, [x8, #0x10]
0x02F3B080: blr      x8
0x02F3B084: ldr      x8, [x19]
0x02F3B088: mov      x0, x19
0x02F3B08C: ldr      x8, [x8, #0x18]
0x02F3B090: blr      x8
0x02F3B094: ldr      x0, [x20, #0xde8]
0x02F3B098: ldp      x20, x19, [sp, #0x10]
0x02F3B09C: ldr      x30, [sp], #0x20
0x02F3B0A0: ret      
~~~

### Function start 0x2f3b574
Hits: [{"pc": "0x2f3b5a8", "adrp": "0x2f3b5a0", "target": "0x11ae791", "label": "VInt3MapNodeRuntime", "keywords": ["VInt3"], "fde_start": "0x2f3b574", "fde_end": "0x2f3b610", "kind": "add", "reg": "x1"}]
~~~asm
0x02F3B574: str      x30, [sp, #-0x20]!
0x02F3B578: stp      x20, x19, [sp, #0x10]
0x02F3B57C: adrp     x20, #0x53e7000
0x02F3B580: ldr      x0, [x20, #0xde0]
0x02F3B584: cbnz     x0, #0x2f3b604
0x02F3B588: mov      w0, #0x168
0x02F3B58C: bl       #0x4b40050
0x02F3B590: adrp     x8, #0x5040000
0x02F3B594: mov      x19, x0
0x02F3B598: ldr      x8, [x8, #0x20]
0x02F3B59C: cbz      x8, #0x2f3b5bc
0x02F3B5A0: adrp     x1, #0x11ae000
0x02F3B5A4: mov      x0, x19
0x02F3B5A8: add      x1, x1, #0x791
0x02F3B5AC: mov      x2, xzr
0x02F3B5B0: mov      x3, xzr
0x02F3B5B4: mov      w4, #0x58
0x02F3B5B8: blr      x8
0x02F3B5BC: adrp     x8, #0x5000000
0x02F3B5C0: adrp     x9, #0x50eb000
0x02F3B5C4: str      x19, [x20, #0xde0]
0x02F3B5C8: ldr      x8, [x8, #0x3e8]
0x02F3B5CC: ldr      x9, [x9, #0x350]
0x02F3B5D0: str      x8, [x19, #0x160]
0x02F3B5D4: blr      x9
0x02F3B5D8: ldr      x8, [x19]
0x02F3B5DC: mov      x1, x0
0x02F3B5E0: mov      x0, x19
0x02F3B5E4: mov      w2, wzr
0x02F3B5E8: ldr      x8, [x8, #0x10]
0x02F3B5EC: blr      x8
0x02F3B5F0: ldr      x8, [x19]
0x02F3B5F4: mov      x0, x19
0x02F3B5F8: ldr      x8, [x8, #0x18]
0x02F3B5FC: blr      x8
0x02F3B600: ldr      x0, [x20, #0xde0]
0x02F3B604: ldp      x20, x19, [sp, #0x10]
0x02F3B608: ldr      x30, [sp], #0x20
0x02F3B60C: ret      
~~~

### Function start 0x2f3c950
Hits: [{"pc": "0x2f3c984", "adrp": "0x2f3c97c", "target": "0x11c74f3", "label": "ActorRootConstantMapNodeRuntime", "keywords": ["ActorRoot"], "fde_start": "0x2f3c950", "fde_end": "0x2f3c9ec", "kind": "add", "reg": "x1"}]
~~~asm
0x02F3C950: str      x30, [sp, #-0x20]!
0x02F3C954: stp      x20, x19, [sp, #0x10]
0x02F3C958: adrp     x20, #0x53e7000
0x02F3C95C: ldr      x0, [x20, #0xdb8]
0x02F3C960: cbnz     x0, #0x2f3c9e0
0x02F3C964: mov      w0, #0x168
0x02F3C968: bl       #0x4b40050
0x02F3C96C: adrp     x8, #0x5040000
0x02F3C970: mov      x19, x0
0x02F3C974: ldr      x8, [x8, #0x20]
0x02F3C978: cbz      x8, #0x2f3c998
0x02F3C97C: adrp     x1, #0x11c7000
0x02F3C980: mov      x0, x19
0x02F3C984: add      x1, x1, #0x4f3
0x02F3C988: mov      x2, xzr
0x02F3C98C: mov      x3, xzr
0x02F3C990: mov      w4, #0x58
0x02F3C994: blr      x8
0x02F3C998: adrp     x8, #0x5000000
0x02F3C99C: adrp     x9, #0x50eb000
0x02F3C9A0: str      x19, [x20, #0xdb8]
0x02F3C9A4: ldr      x8, [x8, #0x3c0]
0x02F3C9A8: ldr      x9, [x9, #0x350]
0x02F3C9AC: str      x8, [x19, #0x160]
0x02F3C9B0: blr      x9
0x02F3C9B4: ldr      x8, [x19]
0x02F3C9B8: mov      x1, x0
0x02F3C9BC: mov      x0, x19
0x02F3C9C0: mov      w2, wzr
0x02F3C9C4: ldr      x8, [x8, #0x10]
0x02F3C9C8: blr      x8
0x02F3C9CC: ldr      x8, [x19]
0x02F3C9D0: mov      x0, x19
0x02F3C9D4: ldr      x8, [x8, #0x18]
0x02F3C9D8: blr      x8
0x02F3C9DC: ldr      x0, [x20, #0xdb8]
0x02F3C9E0: ldp      x20, x19, [sp, #0x10]
0x02F3C9E4: ldr      x30, [sp], #0x20
0x02F3C9E8: ret      
~~~

### Function start 0x2f3ccd8
Hits: [{"pc": "0x2f3cd0c", "adrp": "0x2f3cd04", "target": "0x11c7513", "label": "ActorRootMapForeachLoopNodeRuntime", "keywords": ["ActorRoot"], "fde_start": "0x2f3ccd8", "fde_end": "0x2f3cd74", "kind": "add", "reg": "x1"}]
~~~asm
0x02F3CCD8: str      x30, [sp, #-0x20]!
0x02F3CCDC: stp      x20, x19, [sp, #0x10]
0x02F3CCE0: adrp     x20, #0x53e7000
0x02F3CCE4: ldr      x0, [x20, #0xdb0]
0x02F3CCE8: cbnz     x0, #0x2f3cd68
0x02F3CCEC: mov      w0, #0x168
0x02F3CCF0: bl       #0x4b40050
0x02F3CCF4: adrp     x8, #0x5040000
0x02F3CCF8: mov      x19, x0
0x02F3CCFC: ldr      x8, [x8, #0x20]
0x02F3CD00: cbz      x8, #0x2f3cd20
0x02F3CD04: adrp     x1, #0x11c7000
0x02F3CD08: mov      x0, x19
0x02F3CD0C: add      x1, x1, #0x513
0x02F3CD10: mov      x2, xzr
0x02F3CD14: mov      x3, xzr
0x02F3CD18: mov      w4, #0x38
0x02F3CD1C: blr      x8
0x02F3CD20: adrp     x8, #0x5000000
0x02F3CD24: adrp     x9, #0x50eb000
0x02F3CD28: str      x19, [x20, #0xdb0]
0x02F3CD2C: ldr      x8, [x8, #0x3b8]
0x02F3CD30: ldr      x9, [x9, #0x350]
0x02F3CD34: str      x8, [x19, #0x160]
0x02F3CD38: blr      x9
0x02F3CD3C: ldr      x8, [x19]
0x02F3CD40: mov      x1, x0
0x02F3CD44: mov      x0, x19
0x02F3CD48: mov      w2, wzr
0x02F3CD4C: ldr      x8, [x8, #0x10]
0x02F3CD50: blr      x8
0x02F3CD54: ldr      x8, [x19]
0x02F3CD58: mov      x0, x19
0x02F3CD5C: ldr      x8, [x8, #0x18]
0x02F3CD60: blr      x8
0x02F3CD64: ldr      x0, [x20, #0xdb0]
0x02F3CD68: ldp      x20, x19, [sp, #0x10]
0x02F3CD6C: ldr      x30, [sp], #0x20
0x02F3CD70: ret      
~~~

### Function start 0x2f3cf48
Hits: [{"pc": "0x2f3cf7c", "adrp": "0x2f3cf74", "target": "0x11fc1b3", "label": "GlobalVariableActorRootMapNodeRuntime", "keywords": ["ActorRoot"], "fde_start": "0x2f3cf48", "fde_end": "0x2f3cfe4", "kind": "add", "reg": "x1"}]
~~~asm
0x02F3CF48: str      x30, [sp, #-0x20]!
0x02F3CF4C: stp      x20, x19, [sp, #0x10]
0x02F3CF50: adrp     x20, #0x53e7000
0x02F3CF54: ldr      x0, [x20, #0xda8]
0x02F3CF58: cbnz     x0, #0x2f3cfd8
0x02F3CF5C: mov      w0, #0x168
0x02F3CF60: bl       #0x4b40050
0x02F3CF64: adrp     x8, #0x5040000
0x02F3CF68: mov      x19, x0
0x02F3CF6C: ldr      x8, [x8, #0x20]
0x02F3CF70: cbz      x8, #0x2f3cf90
0x02F3CF74: adrp     x1, #0x11fc000
0x02F3CF78: mov      x0, x19
0x02F3CF7C: add      x1, x1, #0x1b3
0x02F3CF80: mov      x2, xzr
0x02F3CF84: mov      x3, xzr
0x02F3CF88: mov      w4, #0x38
0x02F3CF8C: blr      x8
0x02F3CF90: adrp     x8, #0x5000000
0x02F3CF94: adrp     x9, #0x50eb000
0x02F3CF98: str      x19, [x20, #0xda8]
0x02F3CF9C: ldr      x8, [x8, #0x3b0]
0x02F3CFA0: ldr      x9, [x9, #0x350]
0x02F3CFA4: str      x8, [x19, #0x160]
0x02F3CFA8: blr      x9
0x02F3CFAC: ldr      x8, [x19]
0x02F3CFB0: mov      x1, x0
0x02F3CFB4: mov      x0, x19
0x02F3CFB8: mov      w2, wzr
0x02F3CFBC: ldr      x8, [x8, #0x10]
0x02F3CFC0: blr      x8
0x02F3CFC4: ldr      x8, [x19]
0x02F3CFC8: mov      x0, x19
0x02F3CFCC: ldr      x8, [x8, #0x18]
0x02F3CFD0: blr      x8
0x02F3CFD4: ldr      x0, [x20, #0xda8]
0x02F3CFD8: ldp      x20, x19, [sp, #0x10]
0x02F3CFDC: ldr      x30, [sp], #0x20
0x02F3CFE0: ret      
~~~

### Function start 0x2f3d4b4
Hits: [{"pc": "0x2f3d4e8", "adrp": "0x2f3d4e0", "target": "0x1187fca", "label": "ActorRootMapNodeRuntime", "keywords": ["ActorRoot"], "fde_start": "0x2f3d4b4", "fde_end": "0x2f3d550", "kind": "add", "reg": "x1"}]
~~~asm
0x02F3D4B4: str      x30, [sp, #-0x20]!
0x02F3D4B8: stp      x20, x19, [sp, #0x10]
0x02F3D4BC: adrp     x20, #0x53e7000
0x02F3D4C0: ldr      x0, [x20, #0xda0]
0x02F3D4C4: cbnz     x0, #0x2f3d544
0x02F3D4C8: mov      w0, #0x168
0x02F3D4CC: bl       #0x4b40050
0x02F3D4D0: adrp     x8, #0x5040000
0x02F3D4D4: mov      x19, x0
0x02F3D4D8: ldr      x8, [x8, #0x20]
0x02F3D4DC: cbz      x8, #0x2f3d4fc
0x02F3D4E0: adrp     x1, #0x1187000
0x02F3D4E4: mov      x0, x19
0x02F3D4E8: add      x1, x1, #0xfca
0x02F3D4EC: mov      x2, xzr
0x02F3D4F0: mov      x3, xzr
0x02F3D4F4: mov      w4, #0x58
0x02F3D4F8: blr      x8
0x02F3D4FC: adrp     x8, #0x5000000
0x02F3D500: adrp     x9, #0x50eb000
0x02F3D504: str      x19, [x20, #0xda0]
0x02F3D508: ldr      x8, [x8, #0x3a8]
0x02F3D50C: ldr      x9, [x9, #0x350]
0x02F3D510: str      x8, [x19, #0x160]
0x02F3D514: blr      x9
0x02F3D518: ldr      x8, [x19]
0x02F3D51C: mov      x1, x0
0x02F3D520: mov      x0, x19
0x02F3D524: mov      w2, wzr
0x02F3D528: ldr      x8, [x8, #0x10]
0x02F3D52C: blr      x8
0x02F3D530: ldr      x8, [x19]
0x02F3D534: mov      x0, x19
0x02F3D538: ldr      x8, [x8, #0x18]
0x02F3D53C: blr      x8
0x02F3D540: ldr      x0, [x20, #0xda0]
0x02F3D544: ldp      x20, x19, [sp, #0x10]
0x02F3D548: ldr      x30, [sp], #0x20
0x02F3D54C: ret      
~~~

### Function start 0x2f3d874
Hits: [{"pc": "0x2f3d8a8", "adrp": "0x2f3d8a0", "target": "0x1140f41", "label": "ConstantVInt3NodeRuntime", "keywords": ["VInt3"], "fde_start": "0x2f3d874", "fde_end": "0x2f3d910", "kind": "add", "reg": "x1"}]
~~~asm
0x02F3D874: str      x30, [sp, #-0x20]!
0x02F3D878: stp      x20, x19, [sp, #0x10]
0x02F3D87C: adrp     x20, #0x53e7000
0x02F3D880: ldr      x0, [x20, #0xd98]
0x02F3D884: cbnz     x0, #0x2f3d904
0x02F3D888: mov      w0, #0x168
0x02F3D88C: bl       #0x4b40050
0x02F3D890: adrp     x8, #0x5040000
0x02F3D894: mov      x19, x0
0x02F3D898: ldr      x8, [x8, #0x20]
0x02F3D89C: cbz      x8, #0x2f3d8bc
0x02F3D8A0: adrp     x1, #0x1140000
0x02F3D8A4: mov      x0, x19
0x02F3D8A8: add      x1, x1, #0xf41
0x02F3D8AC: mov      x2, xzr
0x02F3D8B0: mov      x3, xzr
0x02F3D8B4: mov      w4, #0x40
0x02F3D8B8: blr      x8
0x02F3D8BC: adrp     x8, #0x5000000
0x02F3D8C0: adrp     x9, #0x50eb000
0x02F3D8C4: str      x19, [x20, #0xd98]
0x02F3D8C8: ldr      x8, [x8, #0x3a0]
0x02F3D8CC: ldr      x9, [x9, #0x350]
0x02F3D8D0: str      x8, [x19, #0x160]
0x02F3D8D4: blr      x9
0x02F3D8D8: ldr      x8, [x19]
0x02F3D8DC: mov      x1, x0
0x02F3D8E0: mov      x0, x19
0x02F3D8E4: mov      w2, wzr
0x02F3D8E8: ldr      x8, [x8, #0x10]
0x02F3D8EC: blr      x8
0x02F3D8F0: ldr      x8, [x19]
0x02F3D8F4: mov      x0, x19
0x02F3D8F8: ldr      x8, [x8, #0x18]
0x02F3D8FC: blr      x8
0x02F3D900: ldr      x0, [x20, #0xd98]
0x02F3D904: ldp      x20, x19, [sp, #0x10]
0x02F3D908: ldr      x30, [sp], #0x20
0x02F3D90C: ret      
~~~

### Function start 0x2f3db74
Hits: [{"pc": "0x2f3dba8", "adrp": "0x2f3dba0", "target": "0x12028df", "label": "GlobalVariableVInt3NodeRuntime", "keywords": ["VInt3"], "fde_start": "0x2f3db74", "fde_end": "0x2f3dc10", "kind": "add", "reg": "x1"}]
~~~asm
0x02F3DB74: str      x30, [sp, #-0x20]!
0x02F3DB78: stp      x20, x19, [sp, #0x10]
0x02F3DB7C: adrp     x20, #0x53e7000
0x02F3DB80: ldr      x0, [x20, #0xd90]
0x02F3DB84: cbnz     x0, #0x2f3dc04
0x02F3DB88: mov      w0, #0x168
0x02F3DB8C: bl       #0x4b40050
0x02F3DB90: adrp     x8, #0x5040000
0x02F3DB94: mov      x19, x0
0x02F3DB98: ldr      x8, [x8, #0x20]
0x02F3DB9C: cbz      x8, #0x2f3dbbc
0x02F3DBA0: adrp     x1, #0x1202000
0x02F3DBA4: mov      x0, x19
0x02F3DBA8: add      x1, x1, #0x8df
0x02F3DBAC: mov      x2, xzr
0x02F3DBB0: mov      x3, xzr
0x02F3DBB4: mov      w4, #0x38
0x02F3DBB8: blr      x8
0x02F3DBBC: adrp     x8, #0x5000000
0x02F3DBC0: adrp     x9, #0x50eb000
0x02F3DBC4: str      x19, [x20, #0xd90]
0x02F3DBC8: ldr      x8, [x8, #0x398]
0x02F3DBCC: ldr      x9, [x9, #0x350]
0x02F3DBD0: str      x8, [x19, #0x160]
0x02F3DBD4: blr      x9
0x02F3DBD8: ldr      x8, [x19]
0x02F3DBDC: mov      x1, x0
0x02F3DBE0: mov      x0, x19
0x02F3DBE4: mov      w2, wzr
0x02F3DBE8: ldr      x8, [x8, #0x10]
0x02F3DBEC: blr      x8
0x02F3DBF0: ldr      x8, [x19]
0x02F3DBF4: mov      x0, x19
0x02F3DBF8: ldr      x8, [x8, #0x18]
0x02F3DBFC: blr      x8
0x02F3DC00: ldr      x0, [x20, #0xd90]
0x02F3DC04: ldp      x20, x19, [sp, #0x10]
0x02F3DC08: ldr      x30, [sp], #0x20
0x02F3DC0C: ret      
~~~

### Function start 0x2f3e0d4
Hits: [{"pc": "0x2f3e108", "adrp": "0x2f3e100", "target": "0x116e1ab", "label": "VariableVInt3NodeRuntime", "keywords": ["VInt3"], "fde_start": "0x2f3e0d4", "fde_end": "0x2f3e170", "kind": "add", "reg": "x1"}]
~~~asm
0x02F3E0D4: str      x30, [sp, #-0x20]!
0x02F3E0D8: stp      x20, x19, [sp, #0x10]
0x02F3E0DC: adrp     x20, #0x53e7000
0x02F3E0E0: ldr      x0, [x20, #0xd88]
0x02F3E0E4: cbnz     x0, #0x2f3e164
0x02F3E0E8: mov      w0, #0x168
0x02F3E0EC: bl       #0x4b40050
0x02F3E0F0: adrp     x8, #0x5040000
0x02F3E0F4: mov      x19, x0
0x02F3E0F8: ldr      x8, [x8, #0x20]
0x02F3E0FC: cbz      x8, #0x2f3e11c
0x02F3E100: adrp     x1, #0x116e000
0x02F3E104: mov      x0, x19
0x02F3E108: add      x1, x1, #0x1ab
0x02F3E10C: mov      x2, xzr
0x02F3E110: mov      x3, xzr
0x02F3E114: mov      w4, #0x40
0x02F3E118: blr      x8
0x02F3E11C: adrp     x8, #0x5000000
0x02F3E120: adrp     x9, #0x50eb000
0x02F3E124: str      x19, [x20, #0xd88]
0x02F3E128: ldr      x8, [x8, #0x390]
0x02F3E12C: ldr      x9, [x9, #0x350]
0x02F3E130: str      x8, [x19, #0x160]
0x02F3E134: blr      x9
0x02F3E138: ldr      x8, [x19]
0x02F3E13C: mov      x1, x0
0x02F3E140: mov      x0, x19
0x02F3E144: mov      w2, wzr
0x02F3E148: ldr      x8, [x8, #0x10]
0x02F3E14C: blr      x8
0x02F3E150: ldr      x8, [x19]
0x02F3E154: mov      x0, x19
0x02F3E158: ldr      x8, [x8, #0x18]
0x02F3E15C: blr      x8
0x02F3E160: ldr      x0, [x20, #0xd88]
0x02F3E164: ldp      x20, x19, [sp, #0x10]
0x02F3E168: ldr      x30, [sp], #0x20
0x02F3E16C: ret      
~~~

### Function start 0x2f41554
Hits: [{"pc": "0x2f41588", "adrp": "0x2f41580", "target": "0x12028fe", "label": "VInt3ArrayForeachLoopNodeRuntime", "keywords": ["VInt3"], "fde_start": "0x2f41554", "fde_end": "0x2f415f0", "kind": "add", "reg": "x1"}]
~~~asm
0x02F41554: str      x30, [sp, #-0x20]!
0x02F41558: stp      x20, x19, [sp, #0x10]
0x02F4155C: adrp     x20, #0x53e7000
0x02F41560: ldr      x0, [x20, #0xcd0]
0x02F41564: cbnz     x0, #0x2f415e4
0x02F41568: mov      w0, #0x168
0x02F4156C: bl       #0x4b40050
0x02F41570: adrp     x8, #0x5040000
0x02F41574: mov      x19, x0
0x02F41578: ldr      x8, [x8, #0x20]
0x02F4157C: cbz      x8, #0x2f4159c
0x02F41580: adrp     x1, #0x1202000
0x02F41584: mov      x0, x19
0x02F41588: add      x1, x1, #0x8fe
0x02F4158C: mov      x2, xzr
0x02F41590: mov      x3, xzr
0x02F41594: mov      w4, #0x38
0x02F41598: blr      x8
0x02F4159C: adrp     x8, #0x5000000
0x02F415A0: adrp     x9, #0x50eb000
0x02F415A4: str      x19, [x20, #0xcd0]
0x02F415A8: ldr      x8, [x8, #0x2d8]
0x02F415AC: ldr      x9, [x9, #0x350]
0x02F415B0: str      x8, [x19, #0x160]
0x02F415B4: blr      x9
0x02F415B8: ldr      x8, [x19]
0x02F415BC: mov      x1, x0
0x02F415C0: mov      x0, x19
0x02F415C4: mov      w2, wzr
0x02F415C8: ldr      x8, [x8, #0x10]
0x02F415CC: blr      x8
0x02F415D0: ldr      x8, [x19]
0x02F415D4: mov      x0, x19
0x02F415D8: ldr      x8, [x8, #0x18]
0x02F415DC: blr      x8
0x02F415E0: ldr      x0, [x20, #0xcd0]
0x02F415E4: ldp      x20, x19, [sp, #0x10]
0x02F415E8: ldr      x30, [sp], #0x20
0x02F415EC: ret      
~~~

### Function start 0x2f417c4
Hits: [{"pc": "0x2f417f8", "adrp": "0x2f417f0", "target": "0x11e181d", "label": "GlobalVariableVInt3ArrayNodeRuntime", "keywords": ["VInt3"], "fde_start": "0x2f417c4", "fde_end": "0x2f41860", "kind": "add", "reg": "x1"}]
~~~asm
0x02F417C4: str      x30, [sp, #-0x20]!
0x02F417C8: stp      x20, x19, [sp, #0x10]
0x02F417CC: adrp     x20, #0x53e7000
0x02F417D0: ldr      x0, [x20, #0xcc8]
0x02F417D4: cbnz     x0, #0x2f41854
0x02F417D8: mov      w0, #0x168
0x02F417DC: bl       #0x4b40050
0x02F417E0: adrp     x8, #0x5040000
0x02F417E4: mov      x19, x0
0x02F417E8: ldr      x8, [x8, #0x20]
0x02F417EC: cbz      x8, #0x2f4180c
0x02F417F0: adrp     x1, #0x11e1000
0x02F417F4: mov      x0, x19
0x02F417F8: add      x1, x1, #0x81d
0x02F417FC: mov      x2, xzr
0x02F41800: mov      x3, xzr
0x02F41804: mov      w4, #0x38
0x02F41808: blr      x8
0x02F4180C: adrp     x8, #0x5000000
0x02F41810: adrp     x9, #0x50eb000
0x02F41814: str      x19, [x20, #0xcc8]
0x02F41818: ldr      x8, [x8, #0x2d0]
0x02F4181C: ldr      x9, [x9, #0x350]
0x02F41820: str      x8, [x19, #0x160]
0x02F41824: blr      x9
0x02F41828: ldr      x8, [x19]
0x02F4182C: mov      x1, x0
0x02F41830: mov      x0, x19
0x02F41834: mov      w2, wzr
0x02F41838: ldr      x8, [x8, #0x10]
0x02F4183C: blr      x8
0x02F41840: ldr      x8, [x19]
0x02F41844: mov      x0, x19
0x02F41848: ldr      x8, [x8, #0x18]
0x02F4184C: blr      x8
0x02F41850: ldr      x0, [x20, #0xcc8]
0x02F41854: ldp      x20, x19, [sp, #0x10]
0x02F41858: ldr      x30, [sp], #0x20
0x02F4185C: ret      
~~~

### Function start 0x2f45508
Hits: [{"pc": "0x2f4553c", "adrp": "0x2f45534", "target": "0x1194dc5", "label": "ActorRootArrayForeachLoopNodeRuntime", "keywords": ["ActorRoot"], "fde_start": "0x2f45508", "fde_end": "0x2f455a4", "kind": "add", "reg": "x1"}]
~~~asm
0x02F45508: str      x30, [sp, #-0x20]!
0x02F4550C: stp      x20, x19, [sp, #0x10]
0x02F45510: adrp     x20, #0x53e7000
0x02F45514: ldr      x0, [x20, #0xbf0]
0x02F45518: cbnz     x0, #0x2f45598
0x02F4551C: mov      w0, #0x168
0x02F45520: bl       #0x4b40050
0x02F45524: adrp     x8, #0x5040000
0x02F45528: mov      x19, x0
0x02F4552C: ldr      x8, [x8, #0x20]
0x02F45530: cbz      x8, #0x2f45550
0x02F45534: adrp     x1, #0x1194000
0x02F45538: mov      x0, x19
0x02F4553C: add      x1, x1, #0xdc5
0x02F45540: mov      x2, xzr
0x02F45544: mov      x3, xzr
0x02F45548: mov      w4, #0x38
0x02F4554C: blr      x8
0x02F45550: adrp     x8, #0x5000000
0x02F45554: adrp     x9, #0x50eb000
0x02F45558: str      x19, [x20, #0xbf0]
0x02F4555C: ldr      x8, [x8, #0x1f8]
0x02F45560: ldr      x9, [x9, #0x350]
0x02F45564: str      x8, [x19, #0x160]
0x02F45568: blr      x9
0x02F4556C: ldr      x8, [x19]
0x02F45570: mov      x1, x0
0x02F45574: mov      x0, x19
0x02F45578: mov      w2, wzr
0x02F4557C: ldr      x8, [x8, #0x10]
0x02F45580: blr      x8
0x02F45584: ldr      x8, [x19]
0x02F45588: mov      x0, x19
0x02F4558C: ldr      x8, [x8, #0x18]
0x02F45590: blr      x8
0x02F45594: ldr      x0, [x20, #0xbf0]
0x02F45598: ldp      x20, x19, [sp, #0x10]
0x02F4559C: ldr      x30, [sp], #0x20
0x02F455A0: ret      
~~~

### Function start 0x2f45778
Hits: [{"pc": "0x2f457ac", "adrp": "0x2f457a4", "target": "0x11ef056", "label": "GlobalVariableActorRootArrayNodeRuntime", "keywords": ["ActorRoot"], "fde_start": "0x2f45778", "fde_end": "0x2f45814", "kind": "add", "reg": "x1"}]
~~~asm
0x02F45778: str      x30, [sp, #-0x20]!
0x02F4577C: stp      x20, x19, [sp, #0x10]
0x02F45780: adrp     x20, #0x53e7000
0x02F45784: ldr      x0, [x20, #0xbe8]
0x02F45788: cbnz     x0, #0x2f45808
0x02F4578C: mov      w0, #0x168
0x02F45790: bl       #0x4b40050
0x02F45794: adrp     x8, #0x5040000
0x02F45798: mov      x19, x0
0x02F4579C: ldr      x8, [x8, #0x20]
0x02F457A0: cbz      x8, #0x2f457c0
0x02F457A4: adrp     x1, #0x11ef000
0x02F457A8: mov      x0, x19
0x02F457AC: add      x1, x1, #0x56
0x02F457B0: mov      x2, xzr
0x02F457B4: mov      x3, xzr
0x02F457B8: mov      w4, #0x38
0x02F457BC: blr      x8
0x02F457C0: adrp     x8, #0x5000000
0x02F457C4: adrp     x9, #0x50eb000
0x02F457C8: str      x19, [x20, #0xbe8]
0x02F457CC: ldr      x8, [x8, #0x1f0]
0x02F457D0: ldr      x9, [x9, #0x350]
0x02F457D4: str      x8, [x19, #0x160]
0x02F457D8: blr      x9
0x02F457DC: ldr      x8, [x19]
0x02F457E0: mov      x1, x0
0x02F457E4: mov      x0, x19
0x02F457E8: mov      w2, wzr
0x02F457EC: ldr      x8, [x8, #0x10]
0x02F457F0: blr      x8
0x02F457F4: ldr      x8, [x19]
0x02F457F8: mov      x0, x19
0x02F457FC: ldr      x8, [x8, #0x18]
0x02F45800: blr      x8
0x02F45804: ldr      x0, [x20, #0xbe8]
0x02F45808: ldp      x20, x19, [sp, #0x10]
0x02F4580C: ldr      x30, [sp], #0x20
0x02F45810: ret      
~~~

### Function start 0x2fce670
Hits: [{"pc": "0x2fce680", "adrp": "0x2fce67c", "target": "0x118179f", "label": "AGETemplate::ForbidMoveDirectionCmdDuration", "keywords": ["MoveDir"], "fde_start": "0x2fce670", "fde_end": "0x2fce6fc", "kind": "add", "reg": "x1"}]
~~~asm
0x02FCE670: sub      sp, sp, #0x20
0x02FCE674: stp      x30, x19, [sp, #0x10]
0x02FCE678: adrp     x8, #0x50b8000
0x02FCE67C: adrp     x1, #0x1181000
0x02FCE680: add      x1, x1, #0x79f
0x02FCE684: mov      x0, sp
0x02FCE688: stp      xzr, xzr, [sp]
0x02FCE68C: ldr      x8, [x8, #0x3f8]
0x02FCE690: blr      x8
0x02FCE694: adrp     x8, #0x5205000
0x02FCE698: ldr      x8, [x8, #0xe70]
0x02FCE69C: mov      x0, sp
0x02FCE6A0: blr      x8
0x02FCE6A4: mov      x19, x0
0x02FCE6A8: ldrb     w8, [sp, #4]
0x02FCE6AC: tbnz     w8, #0, #0x2fce6c0
0x02FCE6B0: adrp     x8, #0x50b8000
0x02FCE6B4: ldr      x8, [x8, #0x1d0]
0x02FCE6B8: mov      x0, sp
0x02FCE6BC: blr      x8
0x02FCE6C0: mov      x0, x19
0x02FCE6C4: ldp      x30, x19, [sp, #0x10]
0x02FCE6C8: add      sp, sp, #0x20
0x02FCE6CC: ret      
0x02FCE6D0: bl       #0x2236550
0x02FCE6D4: ldrb     w8, [sp, #4]
0x02FCE6D8: mov      x19, x0
0x02FCE6DC: tbnz     w8, #0, #0x2fce6f0
0x02FCE6E0: adrp     x8, #0x50b8000
0x02FCE6E4: ldr      x8, [x8, #0x1d0]
0x02FCE6E8: mov      x0, sp
0x02FCE6EC: blr      x8
0x02FCE6F0: mov      x0, x19
0x02FCE6F4: bl       #0x2231bf0
0x02FCE6F8: bl       #0x2236550
~~~

### Function start 0x2fd1c6c
Hits: [{"pc": "0x2fd1c7c", "adrp": "0x2fd1c78", "target": "0x1194e93", "label": "AGETemplate::ActorPositionChangeEventListenerDuration", "keywords": ["ActorPos"], "fde_start": "0x2fd1c6c", "fde_end": "0x2fd1cf8", "kind": "add", "reg": "x1"}]
~~~asm
0x02FD1C6C: sub      sp, sp, #0x20
0x02FD1C70: stp      x30, x19, [sp, #0x10]
0x02FD1C74: adrp     x8, #0x50b8000
0x02FD1C78: adrp     x1, #0x1194000
0x02FD1C7C: add      x1, x1, #0xe93
0x02FD1C80: mov      x0, sp
0x02FD1C84: stp      xzr, xzr, [sp]
0x02FD1C88: ldr      x8, [x8, #0x3f8]
0x02FD1C8C: blr      x8
0x02FD1C90: adrp     x8, #0x5205000
0x02FD1C94: ldr      x8, [x8, #0xe70]
0x02FD1C98: mov      x0, sp
0x02FD1C9C: blr      x8
0x02FD1CA0: mov      x19, x0
0x02FD1CA4: ldrb     w8, [sp, #4]
0x02FD1CA8: tbnz     w8, #0, #0x2fd1cbc
0x02FD1CAC: adrp     x8, #0x50b8000
0x02FD1CB0: ldr      x8, [x8, #0x1d0]
0x02FD1CB4: mov      x0, sp
0x02FD1CB8: blr      x8
0x02FD1CBC: mov      x0, x19
0x02FD1CC0: ldp      x30, x19, [sp, #0x10]
0x02FD1CC4: add      sp, sp, #0x20
0x02FD1CC8: ret      
0x02FD1CCC: bl       #0x2236550
0x02FD1CD0: ldrb     w8, [sp, #4]
0x02FD1CD4: mov      x19, x0
0x02FD1CD8: tbnz     w8, #0, #0x2fd1cec
0x02FD1CDC: adrp     x8, #0x50b8000
0x02FD1CE0: ldr      x8, [x8, #0x1d0]
0x02FD1CE4: mov      x0, sp
0x02FD1CE8: blr      x8
0x02FD1CEC: mov      x0, x19
0x02FD1CF0: bl       #0x2231bf0
0x02FD1CF4: bl       #0x2236550
~~~
