
import {Location} from '@angular/common';
import {Component} from '@angular/core';
import {BookService} from '../shared/book.service';
import {ActivatedRoute, Params} from '@angular/router';
import {switchMap} from 'rxjs/internal/operators';

@Component({
  moduleId: module.id,
  selector: 'app-book-new',
  templateUrl: './book-new.component.html',
  styleUrls: ['./book-new.component.css']
})

export class BookNewComponent {
  constructor(private bookService: BookService,
              private route: ActivatedRoute,
              private location: Location) {

  }

  save(title, isbn, year): void {
    if (!this.isValid(title, isbn, year)) {
      return;
    }

    this.route.params.pipe(switchMap((params: Params) => this.bookService.create(isbn, title, year, +params['id'])))
      .subscribe(book => alert(book));

  }

  private isValid(title, isbn, year) {
    if (!title || !isbn || !year) {
      console.log('All input fields are required');
      alert('Please enter a name for the Author');
      return false;
    }
    return true;
  }
}
