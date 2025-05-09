import threading

class InMemoryStorage:
    _instance = None
    _lock = threading.Lock()  # Class-level lock for singleton

    def __new__(cls):
        with cls._lock:  # Ensure only one instance is created safely
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._data = {}
                cls._instance._data_lock = threading.Lock()  # Lock for thread safety in set/get
                cls._instance.current_frame = None  # Store the latest frame
        return cls._instance

    def set_value(self, key: str, value: any) -> None:
        """Store a value with the given key (Thread-safe)."""
        with self._data_lock:
            self._data[key] = value

    def get_value(self, key: str, default=None) -> any:
        """Retrieve a value by key. Returns default if key doesn't exist (Thread-safe)."""
        with self._data_lock:
            return self._data.get(key, default)

    def delete_value(self, key: str) -> bool:
        """Delete a value by key (Thread-safe)."""
        with self._data_lock:
            if key in self._data:
                del self._data[key]
                return True
            return False

    def clear_all(self) -> None:
        """Clear all stored data (Thread-safe)."""
        with self._data_lock:
            self._data.clear()

    def get_all(self) -> dict:
        """Get all stored key-value pairs (Thread-safe)."""
        with self._data_lock:
            return self._data.copy()
