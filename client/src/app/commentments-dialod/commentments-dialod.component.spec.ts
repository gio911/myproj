import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CommentmentsDialodComponent } from './commentments-dialod.component';

describe('CommentmentsDialodComponent', () => {
  let component: CommentmentsDialodComponent;
  let fixture: ComponentFixture<CommentmentsDialodComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CommentmentsDialodComponent]
    });
    fixture = TestBed.createComponent(CommentmentsDialodComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
