// Fichier de données partagé entre index.html et participant.html
// Les deux pages chargent ce fichier pour avoir les mêmes matchs

const MATCHES_DATA = {
  "tournament": "Copa del Mundo FIFA 2026",
  "format": "48 equipos, 12 grupos de 4 equipos + fase final",
  "totalMatches": 104,
  "matches": [
    {
      "homeTeam": "México",
      "awayTeam": "Sudáfrica",
      "date": "2026-06-11T21:00",
      "stage": "Fase de grupos - Grupo A",
      "group": "A"
    },
    {
      "homeTeam": "Corea del Sur",
      "awayTeam": "Chequia",
      "date": "2026-06-12T04:00",
      "stage": "Fase de grupos - Grupo A",
      "group": "A"
    },
    {
      "homeTeam": "Canadá",
      "awayTeam": "Bosnia y Herzegovina",
      "date": "2026-06-12T21:00",
      "stage": "Fase de grupos - Grupo B",
      "group": "B"
    },
    {
      "homeTeam": "Estados Unidos",
      "awayTeam": "Paraguay",
      "date": "2026-06-13T03:00",
      "stage": "Fase de grupos - Grupo D",
      "group": "D"
    },
    {
      "homeTeam": "Catar",
      "awayTeam": "Suiza",
      "date": "2026-06-13T21:00",
      "stage": "Fase de grupos - Grupo B",
      "group": "B"
    },
    {
      "homeTeam": "Brasil",
      "awayTeam": "Marruecos",
      "date": "2026-06-14T00:00",
      "stage": "Fase de grupos - Grupo C",
      "group": "C"
    },
    {
      "homeTeam": "Haití",
      "awayTeam": "Escocia",
      "date": "2026-06-14T03:00",
      "stage": "Fase de grupos - Grupo C",
      "group": "C"
    },
    {
      "homeTeam": "Australia",
      "awayTeam": "Turquía",
      "date": "2026-06-14T06:00",
      "stage": "Fase de grupos - Grupo D",
      "group": "D"
    },
    {
      "homeTeam": "Alemania",
      "awayTeam": "Curazao",
      "date": "2026-06-14T19:00",
      "stage": "Fase de grupos - Grupo E",
      "group": "E"
    },
    {
      "homeTeam": "Países Bajos",
      "awayTeam": "Japón",
      "date": "2026-06-14T22:00",
      "stage": "Fase de grupos - Grupo F",
      "group": "F"
    },
    {
      "homeTeam": "Costa de Marfil",
      "awayTeam": "Ecuador",
      "date": "2026-06-15T01:00",
      "stage": "Fase de grupos - Grupo E",
      "group": "E"
    },
    {
      "homeTeam": "Suecia",
      "awayTeam": "Túnez",
      "date": "2026-06-15T04:00",
      "stage": "Fase de grupos - Grupo F",
      "group": "F"
    },
    {
      "homeTeam": "España",
      "awayTeam": "Cabo Verde",
      "date": "2026-06-15T18:00",
      "stage": "Fase de grupos - Grupo H",
      "group": "H"
    },
    {
      "homeTeam": "Bélgica",
      "awayTeam": "Egipto",
      "date": "2026-06-15T21:00",
      "stage": "Fase de grupos - Grupo G",
      "group": "G"
    },
    {
      "homeTeam": "Arabia Saudita",
      "awayTeam": "Uruguay",
      "date": "2026-06-16T00:00",
      "stage": "Fase de grupos - Grupo H",
      "group": "H"
    },
    {
      "homeTeam": "Irán",
      "awayTeam": "Nueva Zelanda",
      "date": "2026-06-16T03:00",
      "stage": "Fase de grupos - Grupo G",
      "group": "G"
    },
    {
      "homeTeam": "Francia",
      "awayTeam": "Senegal",
      "date": "2026-06-16T21:00",
      "stage": "Fase de grupos - Grupo I",
      "group": "I"
    },
    {
      "homeTeam": "Irak",
      "awayTeam": "Noruega",
      "date": "2026-06-17T00:00",
      "stage": "Fase de grupos - Grupo I",
      "group": "I"
    },
    {
      "homeTeam": "Argentina",
      "awayTeam": "Argelia",
      "date": "2026-06-17T03:00",
      "stage": "Fase de grupos - Grupo J",
      "group": "J"
    },
    {
      "homeTeam": "Austria",
      "awayTeam": "Jordania",
      "date": "2026-06-17T06:00",
      "stage": "Fase de grupos - Grupo J",
      "group": "J"
    },
    {
      "homeTeam": "Portugal",
      "awayTeam": "RD Congo",
      "date": "2026-06-17T19:00",
      "stage": "Fase de grupos - Grupo K",
      "group": "K"
    },
    {
      "homeTeam": "Inglaterra",
      "awayTeam": "Croacia",
      "date": "2026-06-17T22:00",
      "stage": "Fase de grupos - Grupo L",
      "group": "L"
    },
    {
      "homeTeam": "Ghana",
      "awayTeam": "Panamá",
      "date": "2026-06-18T01:00",
      "stage": "Fase de grupos - Grupo L",
      "group": "L"
    },
    {
      "homeTeam": "Uzbekistán",
      "awayTeam": "Colombia",
      "date": "2026-06-18T04:00",
      "stage": "Fase de grupos - Grupo K",
      "group": "K"
    },
    {
      "homeTeam": "Chequia",
      "awayTeam": "Sudáfrica",
      "date": "2026-06-18T18:00",
      "stage": "Fase de grupos - Grupo A",
      "group": "A"
    },
    {
      "homeTeam": "Suiza",
      "awayTeam": "Bosnia y Herzegovina",
      "date": "2026-06-18T21:00",
      "stage": "Fase de grupos - Grupo B",
      "group": "B"
    },
    {
      "homeTeam": "Canadá",
      "awayTeam": "Catar",
      "date": "2026-06-19T00:00",
      "stage": "Fase de grupos - Grupo B",
      "group": "B"
    },
    {
      "homeTeam": "México",
      "awayTeam": "Corea del Sur",
      "date": "2026-06-19T03:00",
      "stage": "Fase de grupos - Grupo A",
      "group": "A"
    },
    {
      "homeTeam": "Estados Unidos",
      "awayTeam": "Australia",
      "date": "2026-06-19T21:00",
      "stage": "Fase de grupos - Grupo D",
      "group": "D"
    },
    {
      "homeTeam": "Escocia",
      "awayTeam": "Marruecos",
      "date": "2026-06-20T00:00",
      "stage": "Fase de grupos - Grupo C",
      "group": "C"
    },
    {
      "homeTeam": "Brasil",
      "awayTeam": "Haití",
      "date": "2026-06-20T02:30",
      "stage": "Fase de grupos - Grupo C",
      "group": "C"
    },
    {
      "homeTeam": "Turquía",
      "awayTeam": "Paraguay",
      "date": "2026-06-20T05:00",
      "stage": "Fase de grupos - Grupo D",
      "group": "D"
    },
    {
      "homeTeam": "Países Bajos",
      "awayTeam": "Suecia",
      "date": "2026-06-20T19:00",
      "stage": "Fase de grupos - Grupo F",
      "group": "F"
    },
    {
      "homeTeam": "Alemania",
      "awayTeam": "Costa de Marfil",
      "date": "2026-06-20T22:00",
      "stage": "Fase de grupos - Grupo E",
      "group": "E"
    },
    {
      "homeTeam": "Ecuador",
      "awayTeam": "Curazao",
      "date": "2026-06-21T02:00",
      "stage": "Fase de grupos - Grupo E",
      "group": "E"
    },
    {
      "homeTeam": "Túnez",
      "awayTeam": "Japón",
      "date": "2026-06-21T06:00",
      "stage": "Fase de grupos - Grupo F",
      "group": "F"
    },
    {
      "homeTeam": "España",
      "awayTeam": "Arabia Saudita",
      "date": "2026-06-21T18:00",
      "stage": "Fase de grupos - Grupo H",
      "group": "H"
    },
    {
      "homeTeam": "Bélgica",
      "awayTeam": "Irán",
      "date": "2026-06-21T21:00",
      "stage": "Fase de grupos - Grupo G",
      "group": "G"
    },
    {
      "homeTeam": "Uruguay",
      "awayTeam": "Cabo Verde",
      "date": "2026-06-22T00:00",
      "stage": "Fase de grupos - Grupo H",
      "group": "H"
    },
    {
      "homeTeam": "Nueva Zelanda",
      "awayTeam": "Egipto",
      "date": "2026-06-22T03:00",
      "stage": "Fase de grupos - Grupo G",
      "group": "G"
    },
    {
      "homeTeam": "Argentina",
      "awayTeam": "Austria",
      "date": "2026-06-22T19:00",
      "stage": "Fase de grupos - Grupo J",
      "group": "J"
    },
    {
      "homeTeam": "Francia",
      "awayTeam": "Irak",
      "date": "2026-06-22T23:00",
      "stage": "Fase de grupos - Grupo I",
      "group": "I"
    },
    {
      "homeTeam": "Noruega",
      "awayTeam": "Senegal",
      "date": "2026-06-23T02:00",
      "stage": "Fase de grupos - Grupo I",
      "group": "I"
    },
    {
      "homeTeam": "Jordania",
      "awayTeam": "Argelia",
      "date": "2026-06-23T05:00",
      "stage": "Fase de grupos - Grupo J",
      "group": "J"
    },
    {
      "homeTeam": "Portugal",
      "awayTeam": "Uzbekistán",
      "date": "2026-06-23T19:00",
      "stage": "Fase de grupos - Grupo K",
      "group": "K"
    },
    {
      "homeTeam": "Inglaterra",
      "awayTeam": "Ghana",
      "date": "2026-06-23T22:00",
      "stage": "Fase de grupos - Grupo L",
      "group": "L"
    },
    {
      "homeTeam": "Panamá",
      "awayTeam": "Croacia",
      "date": "2026-06-24T01:00",
      "stage": "Fase de grupos - Grupo L",
      "group": "L"
    },
    {
      "homeTeam": "Colombia",
      "awayTeam": "RD Congo",
      "date": "2026-06-24T04:00",
      "stage": "Fase de grupos - Grupo K",
      "group": "K"
    },
    {
      "homeTeam": "Suiza",
      "awayTeam": "Canadá",
      "date": "2026-06-24T21:00",
      "stage": "Fase de grupos - Grupo B",
      "group": "B"
    },
    {
      "homeTeam": "Bosnia y Herzegovina",
      "awayTeam": "Catar",
      "date": "2026-06-24T21:00",
      "stage": "Fase de grupos - Grupo B",
      "group": "B"
    },
    {
      "homeTeam": "Escocia",
      "awayTeam": "Brasil",
      "date": "2026-06-25T00:00",
      "stage": "Fase de grupos - Grupo C",
      "group": "C"
    },
    {
      "homeTeam": "Marruecos",
      "awayTeam": "Haití",
      "date": "2026-06-25T00:00",
      "stage": "Fase de grupos - Grupo C",
      "group": "C"
    },
    {
      "homeTeam": "Chequia",
      "awayTeam": "México",
      "date": "2026-06-25T03:00",
      "stage": "Fase de grupos - Grupo A",
      "group": "A"
    },
    {
      "homeTeam": "Sudáfrica",
      "awayTeam": "Corea del Sur",
      "date": "2026-06-25T03:00",
      "stage": "Fase de grupos - Grupo A",
      "group": "A"
    },
    {
      "homeTeam": "Curazao",
      "awayTeam": "Costa de Marfil",
      "date": "2026-06-25T22:00",
      "stage": "Fase de grupos - Grupo E",
      "group": "E"
    },
    {
      "homeTeam": "Ecuador",
      "awayTeam": "Alemania",
      "date": "2026-06-25T22:00",
      "stage": "Fase de grupos - Grupo E",
      "group": "E"
    },
    {
      "homeTeam": "Japón",
      "awayTeam": "Suecia",
      "date": "2026-06-26T01:00",
      "stage": "Fase de grupos - Grupo F",
      "group": "F"
    },
    {
      "homeTeam": "Túnez",
      "awayTeam": "Países Bajos",
      "date": "2026-06-26T01:00",
      "stage": "Fase de grupos - Grupo F",
      "group": "F"
    },
    {
      "homeTeam": "Turquía",
      "awayTeam": "Estados Unidos",
      "date": "2026-06-26T04:00",
      "stage": "Fase de grupos - Grupo D",
      "group": "D"
    },
    {
      "homeTeam": "Paraguay",
      "awayTeam": "Australia",
      "date": "2026-06-26T04:00",
      "stage": "Fase de grupos - Grupo D",
      "group": "D"
    },
    {
      "homeTeam": "Noruega",
      "awayTeam": "Francia",
      "date": "2026-06-26T21:00",
      "stage": "Fase de grupos - Grupo I",
      "group": "I"
    },
    {
      "homeTeam": "Senegal",
      "awayTeam": "Irak",
      "date": "2026-06-26T21:00",
      "stage": "Fase de grupos - Grupo I",
      "group": "I"
    },
    {
      "homeTeam": "Cabo Verde",
      "awayTeam": "Arabia Saudita",
      "date": "2026-06-27T02:00",
      "stage": "Fase de grupos - Grupo H",
      "group": "H"
    },
    {
      "homeTeam": "Uruguay",
      "awayTeam": "España",
      "date": "2026-06-27T02:00",
      "stage": "Fase de grupos - Grupo H",
      "group": "H"
    },
    {
      "homeTeam": "Egipto",
      "awayTeam": "Irán",
      "date": "2026-06-27T05:00",
      "stage": "Fase de grupos - Grupo G",
      "group": "G"
    },
    {
      "homeTeam": "Nueva Zelanda",
      "awayTeam": "Bélgica",
      "date": "2026-06-27T05:00",
      "stage": "Fase de grupos - Grupo G",
      "group": "G"
    },
    {
      "homeTeam": "Panamá",
      "awayTeam": "Inglaterra",
      "date": "2026-06-27T23:00",
      "stage": "Fase de grupos - Grupo L",
      "group": "L"
    },
    {
      "homeTeam": "Croacia",
      "awayTeam": "Ghana",
      "date": "2026-06-27T23:00",
      "stage": "Fase de grupos - Grupo L",
      "group": "L"
    },
    {
      "homeTeam": "Colombia",
      "awayTeam": "Portugal",
      "date": "2026-06-28T01:30",
      "stage": "Fase de grupos - Grupo K",
      "group": "K"
    },
    {
      "homeTeam": "RD Congo",
      "awayTeam": "Uzbekistán",
      "date": "2026-06-28T01:30",
      "stage": "Fase de grupos - Grupo K",
      "group": "K"
    },
    {
      "homeTeam": "Argelia",
      "awayTeam": "Austria",
      "date": "2026-06-28T04:00",
      "stage": "Fase de grupos - Grupo J",
      "group": "J"
    },
    {
      "homeTeam": "Jordania",
      "awayTeam": "Argentina",
      "date": "2026-06-28T04:00",
      "stage": "Fase de grupos - Grupo J",
      "group": "J"
    },
    {
      "homeTeam": "2A",
      "awayTeam": "2B",
      "date": "2026-06-28T21:00",
      "stage": "Dieciseisavos de final"
    },
    {
      "homeTeam": "1F",
      "awayTeam": "2C",
      "date": "2026-06-29T15:00",
      "stage": "Dieciseisavos de final"
    },
    {
      "homeTeam": "1E",
      "awayTeam": "3° ABCDF",
      "date": "2026-06-29T18:30",
      "stage": "Dieciseisavos de final"
    },
    {
      "homeTeam": "1C",
      "awayTeam": "2F",
      "date": "2026-06-29T22:00",
      "stage": "Dieciseisavos de final"
    },
    {
      "homeTeam": "1A",
      "awayTeam": "3° CEFHI",
      "date": "2026-06-30T15:00",
      "stage": "Dieciseisavos de final"
    },
    {
      "homeTeam": "2E",
      "awayTeam": "2I",
      "date": "2026-06-30T19:00",
      "stage": "Dieciseisavos de final"
    },
    {
      "homeTeam": "1I",
      "awayTeam": "3° CDFGH",
      "date": "2026-06-30T23:00",
      "stage": "Dieciseisavos de final"
    },
    {
      "homeTeam": "1D",
      "awayTeam": "3° BEFIJ",
      "date": "2026-07-01T14:00",
      "stage": "Dieciseisavos de final"
    },
    {
      "homeTeam": "1L",
      "awayTeam": "3° EHIJK",
      "date": "2026-07-01T18:00",
      "stage": "Dieciseisavos de final"
    },
    {
      "homeTeam": "1G",
      "awayTeam": "3° AEHIJ",
      "date": "2026-07-01T22:00",
      "stage": "Dieciseisavos de final"
    },
    {
      "homeTeam": "1H",
      "awayTeam": "2J",
      "date": "2026-07-02T14:00",
      "stage": "Dieciseisavos de final"
    },
    {
      "homeTeam": "1B",
      "awayTeam": "3° EFGIJ",
      "date": "2026-07-02T17:00",
      "stage": "Dieciseisavos de final"
    },
    {
      "homeTeam": "2K",
      "awayTeam": "2L",
      "date": "2026-07-02T21:00",
      "stage": "Dieciseisavos de final"
    },
    {
      "homeTeam": "1K",
      "awayTeam": "3° DEIJL",
      "date": "2026-07-03T03:30",
      "stage": "Dieciseisavos de final"
    },
    {
      "homeTeam": "2D",
      "awayTeam": "2G",
      "date": "2026-07-03T20:00",
      "stage": "Dieciseisavos de final"
    },
    {
      "homeTeam": "1J",
      "awayTeam": "2H",
      "date": "2026-07-04T00:00",
      "stage": "Dieciseisavos de final"
    },
    {
      "homeTeam": "V73",
      "awayTeam": "V75",
      "date": "2026-07-04T19:00",
      "stage": "Octavos de final"
    },
    {
      "homeTeam": "V74",
      "awayTeam": "V77",
      "date": "2026-07-04T23:00",
      "stage": "Octavos de final"
    },
    {
      "homeTeam": "V79",
      "awayTeam": "V80",
      "date": "2026-07-05T02:00",
      "stage": "Octavos de final"
    },
    {
      "homeTeam": "V76",
      "awayTeam": "V78",
      "date": "2026-07-05T22:00",
      "stage": "Octavos de final"
    },
    {
      "homeTeam": "V81",
      "awayTeam": "V82",
      "date": "2026-07-06T14:00",
      "stage": "Octavos de final"
    },
    {
      "homeTeam": "V83",
      "awayTeam": "V84",
      "date": "2026-07-06T21:00",
      "stage": "Octavos de final"
    },
    {
      "homeTeam": "V86",
      "awayTeam": "V88",
      "date": "2026-07-07T18:00",
      "stage": "Octavos de final"
    },
    {
      "homeTeam": "V85",
      "awayTeam": "V87",
      "date": "2026-07-07T22:00",
      "stage": "Octavos de final"
    },
    {
      "homeTeam": "V89",
      "awayTeam": "V90",
      "date": "2026-07-09T22:00",
      "stage": "Cuartos de final"
    },
    {
      "homeTeam": "V93",
      "awayTeam": "V94",
      "date": "2026-07-10T21:00",
      "stage": "Cuartos de final"
    },
    {
      "homeTeam": "V91",
      "awayTeam": "V92",
      "date": "2026-07-11T23:00",
      "stage": "Cuartos de final"
    },
    {
      "homeTeam": "V95",
      "awayTeam": "V96",
      "date": "2026-07-12T03:00",
      "stage": "Cuartos de final"
    },
    {
      "homeTeam": "V97",
      "awayTeam": "V98",
      "date": "2026-07-14T20:00",
      "stage": "Semifinales"
    },
    {
      "homeTeam": "V99",
      "awayTeam": "V100",
      "date": "2026-07-15T02:00",
      "stage": "Semifinales"
    },
    {
      "homeTeam": "P101",
      "awayTeam": "P102",
      "date": "2026-07-18T21:00",
      "stage": "Finales"
    },
    {
      "homeTeam": "V101",
      "awayTeam": "V102",
      "date": "2026-07-19T21:00",
      "stage": "Finales"
    }

  ]
};
