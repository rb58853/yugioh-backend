# Endpoints
## CRUD
GET /api/v1/
## Yugioh
GET /api/v1/ygo/

### Card CRUD
GET /api/v1/ygo/cards/

### Deck CRUD
GET /api/v1/ygo/decks/

### Archetype CRUD
GET /api/v1/ygo/archetypes/

### Tournament CRUD
GET /api/v1/ygo/tournaments/

# Consults

## 1. Players with more decks
GET /api/v1/ygo/decks/more

## 2. Most popular archetypes
GET /api/v1/ygo/archetypes/popular

## 3. The province/municipality where it is more popular (more players use it) a given archetype.
GET /api/v1/ygo/archetypes/popular/place/?archetype=value

## 3. Extra Popular archetype in a place (municipality or province)
GET /api/v1/ygo/archetypes/archetypes/place/?municipe=value
GET /api/v1/ygo/archetypes/archetypes/place/?province=value

## 4. The champion of a tournament
GET /api/v1/tournaments/champion/?tournament_id=value

## 5. The 𝑛 players with more victories (in a time interval, ordered from greater to lowest).
GET /api/v1/tournaments/champion/date/?start_date=value&end_date=value

## 6. The archetype most used by players in a given tournament.
GET /api/v1/tournaments/archetypes/used/?tournament_id=value

## 7. La cantidad de veces que los arquetipos que han sido el arquetipo del campeón en un grupo de torneos torneos (en un intervalo de tiempo).
GET /api/v1/tournaments/archetypes/champions/?start_date=value&end_date=value

## 8. The province/municipality with more champions (in a time interval).

