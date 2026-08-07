import os
from sqlalchemy import text
from database import engine

def enable_rls_all_tables():
    print("Enabling RLS on all public tables...")
    try:
        with engine.begin() as conn:
            # Get all tables in public schema
            result = conn.execute(text(
                "SELECT tablename FROM pg_tables WHERE schemaname = 'public';"
            ))
            tables = [row[0] for row in result]
            
            for table in tables:
                print(f"Enabling RLS on: {table}")
                conn.execute(text(f'ALTER TABLE "{table}" ENABLE ROW LEVEL SECURITY;'))
                
        print("Successfully enabled RLS on all tables! Supabase security warnings should now be resolved.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    enable_rls_all_tables()
