/* =============================================
   Diagnostic: Raw data for ZZ018 User Fields (ETA)
   ============================================= */

SELECT
    MUD_ENTITEMCD,
    MUD_CLEENTITE,
    MUD_IDCHAMP,
    MUD_VALCHAMP

FROM MCHPSUTILISATDATA

WHERE MUD_ENTITEMCD = 'ETA'
    AND MUD_CLEENTITE = 'ZZ018'
    AND MUD_IDCHAMP BETWEEN 1 AND 6
