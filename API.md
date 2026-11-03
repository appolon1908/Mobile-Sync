# API wiring

The sync service executes authorized synchronization jobs.

Triggered by:
- POST /v1/devices/{device_id}/sync/contacts
- POST /v1/devices/{device_id}/sync/media

It uses scoped provider credentials from a secret reference, emits job status/audit events, and does not ingest passwords or banking credentials.