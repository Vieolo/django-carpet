# Change Log

## v0.2.1 (2024-06-26)
- Fixed the error of `APIResponse` when the request object has no token

## v0.2.0 (2024-06-11)
- Added `is_production` and `is_testing` to `end`
- Added the `data` argument to the `generate_response` which mixes the data dict with the response dict without needing to manually set the key and values of response after generation

#### Breaking Changes
- All the arguments of `generate_response` after `result` must be named. e.g. `operation="object creation"`

## v0.1.14 (2024-03-24)
- Improved the `number_validation` function

## v0.1.13 (2024-01-26)
- Added filter function to `VieoloResponse`

## v0.1.12 (2024-01-26)
- Improved `boolean_validation`

## v0.1.11 (2023-12-30)
- Improved `VieoloResponse`

## v0.1.10 (2023-12-30)
- Improved `VieoloResponse`

## v0.1.9 (2023-12-29)
- Added date time validator

## v0.1.8 (2023-12-20)
- Fixed the limit of `paginator`

## v0.1.7 (2023-12-20)
- Fixed the serializer callback of `paginator`

## v0.1.4 (2023-11-10)
- Improved package

## v0.1.2 (2023-11-10)
- Fixed the export

## v0.1.0 (2023-11-10)
- Initial Release