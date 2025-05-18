# PROYEK DATA ENGINEER

- Hari 4 : Automasi ETL dengan Apache Nifi

## Konfigurasi Flow

### 1. **Processor**:

- `GetFile`:
  - Input Directory: `C:\Users\ASUS\Documents\data-engineer-project\hari_4`
  - File Filter: `.*\.csv`
- `PutDatabaseRecord`:
  - Connection: `DBCPConnectionPool`
  - Table Name: `penjualan`

### 2. **Database Setup**:

```sql
CREATE TABLE penjualan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tanggal DATE,
    produk VARCHAR(100),
    quantity INT,
    harga DECIMAL(12,2),
    region VARCHAR(50)
);
```

## Screenshot

- Diagram : 'images/flow-nifi.drawio.png'
- SQL : 'images/mysql_result.png'
- flow : 'images/nifi_flow.png'

## Result

- Template nifi : nifi_flow_penjualan.html
- SQL : penjualan.sql
