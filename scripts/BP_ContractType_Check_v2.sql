/* =============================================
   BP Contract Type Check (Simplified)
   ============================================= */

SELECT
    T.T_TIERS AS BP_Code,
    T.T_LIBELLE AS BP_Name,
    CONTRACTTYPE.MUD_VALCHAMP AS ContractType

FROM TIERS T

LEFT JOIN MCHPSUTILISATDATA CONTRACTTYPE
    ON CONTRACTTYPE.MUD_ENTITEMCD = 'CLI'
    AND CONTRACTTYPE.MUD_CLEENTITE = T.T_TIERS
    AND CONTRACTTYPE.MUD_IDCHAMP = 35

WHERE T.T_TIERS IN (
    '3200008367',
    '3200008370',
    '3200008369',
    '3200012899',
    '3200010160',
    '3200008365'
)

ORDER BY T.T_TIERS
