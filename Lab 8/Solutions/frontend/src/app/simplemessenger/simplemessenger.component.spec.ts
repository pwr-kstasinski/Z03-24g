import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SimplemessengerComponent } from './simplemessenger.component';

describe('SimplemessengerComponent', () => {
  let component: SimplemessengerComponent;
  let fixture: ComponentFixture<SimplemessengerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SimplemessengerComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SimplemessengerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
