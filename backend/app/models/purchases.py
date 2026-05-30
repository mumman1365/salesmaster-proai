from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Date, Index
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.base import Base

class Purchase(Base):
    __tablename__ = "purchases"
    
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    purchase_date = Column(Date, nullable=False, index=True)
    purchase_number = Column(String(50), nullable=False, index=True)
    
    product_code = Column(String(50), nullable=True, index=True)
    product_name = Column(String(255), nullable=True, index=True)
    product_category = Column(String(100), nullable=True, index=True)
    
    quantity = Column(Float, nullable=False)
    unit_price = Column(Float, nullable=False)
    total_amount = Column(Float, nullable=False)
    discount = Column(Float, default=0)
    
    inventory = Column(Float, nullable=False)
    conversion_ratio = Column(Float, default=1)
    unit_price_at_last_purchase = Column(Float, nullable=True)
    
    supplier_name = Column(String(255), nullable=True, index=True)
    supplier_code = Column(String(50), nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    company = relationship("Company", back_populates="purchases")
    
    __table_args__ = (
        Index('idx_company_product', 'company_id', 'product_code'),
        Index('idx_company_date', 'company_id', 'purchase_date'),
    )
    
    def __repr__(self):
        return f"<Purchase {self.purchase_number}>"
