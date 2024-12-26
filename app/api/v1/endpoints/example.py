# from fastapi import APIRouter, HTTPException
# # from app.schemas.example import ExampleSchema
# from app.db.session import get_db
# from app.db.models.example import ExampleModel
# from sqlalchemy.orm import Session

# router = APIRouter()

# @router.post("/examples/", response_model=ExampleSchema)
# def create_example(example: ExampleSchema, db: Session = next(get_db())):
#     db_example = ExampleModel(**example.dict())
#     db.add(db_example)
#     db.commit()
#     db.refresh(db_example)
#     return db_example

# @router.get("/examples/{example_id}", response_model=ExampleSchema)
# def read_example(example_id: int, db: Session = next(get_db())):
#     db_example = db.query(ExampleModel).filter(ExampleModel.id == example_id).first()
#     if db_example is None:
#         raise HTTPException(status_code=404, detail="Example not found")
#     return db_example

# @router.put("/examples/{example_id}", response_model=ExampleSchema)
# def update_example(example_id: int, example: ExampleSchema, db: Session = next(get_db())):
#     db_example = db.query(ExampleModel).filter(ExampleModel.id == example_id).first()
#     if db_example is None:
#         raise HTTPException(status_code=404, detail="Example not found")
#     for key, value in example.dict().items():
#         setattr(db_example, key, value)
#     db.commit()
#     db.refresh(db_example)
#     return db_example

# @router.delete("/examples/{example_id}")
# def delete_example(example_id: int, db: Session = next(get_db())):
#     db_example = db.query(ExampleModel).filter(ExampleModel.id == example_id).first()
#     if db_example is None:
#         raise HTTPException(status_code=404, detail="Example not found")
#     db.delete(db_example)
#     db.commit()
#     return {"detail": "Example deleted"}